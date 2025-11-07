"""
PART 1 : EXPLORATORY DATA ANALYSIS
Predicting the price of a Football Player
-----------------------------------------
This script loads the dataset, cleans numeric columns, and uses Seaborn
to visualize distributions, correlations, and relationships with market value.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# 1. LOAD AND INSPECT DATA
# ==============================
df = pd.read_csv("Data set__1682565729-62fcaa4ea2bc0b6439d2306a.csv")

print("\n----- Basic Info -----")
print(df.info())
print("\nShape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())

# ==============================
# 2. CLEAN NUMERIC COLUMNS
# ==============================
def clean_numeric_column(series):
    """Convert strings like '€5.5M', '£200K' into numbers"""
    if series.dtype == object:
        s = series.str.replace('[€£$,]', '', regex=True)
        s = s.str.replace('K', '000')
        s = s.str.replace('M', '000000')
        s = s.str.replace(',', '').str.strip()
        return pd.to_numeric(s, errors='coerce')
    return series

for col in ['market_value', 'page_views', 'fpl_value', 'fpl_sel', 'fpl_points', 'age']:
    if col in df.columns:
        df[col + '_clean'] = clean_numeric_column(df[col])

df['market_value_num'] = df['market_value_clean']
print("\nAfter cleaning, numeric summary:\n")
print(df[[c for c in df.columns if c.endswith('_clean')]].describe().T)

# ==============================
# 3. BASIC DESCRIPTIVE STATS
# ==============================
print("\nMarket Value Summary:")
print(df['market_value_num'].describe())

# ==============================
# 4. CORRELATION HEATMAP
# ==============================
num_cols = ['age_clean', 'page_views_clean', 'fpl_value_clean', 'fpl_sel_clean',
            'fpl_points_clean', 'market_value_num']
num_cols = [c for c in num_cols if c in df.columns]

plt.figure(figsize=(7, 5))
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix (Numeric Features)")
plt.tight_layout()
plt.show()

# ==============================
# 5. DISTRIBUTION OF MARKET VALUE
# ==============================
plt.figure(figsize=(8, 4))
sns.histplot(df['market_value_num'], kde=True)
plt.title("Market Value Distribution")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 4))
sns.histplot(np.log1p(df['market_value_num']), kde=True)
plt.title("Log(1 + Market Value) Distribution")
plt.tight_layout()
plt.show()

# ==============================
# 6. BOX & SCATTER PLOTS
# ==============================
categorical_vars = ['position_cat', 'region', 'big_club', 'new_signing', 'position']
for col in categorical_vars:
    if col in df.columns:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=col, y='market_value_num', data=df)
        plt.title(f"Market Value by {col}")
        plt.xticks(rotation=30)
        plt.yscale('symlog')
        plt.tight_layout()
        plt.show()

# Scatterplots
for x, label in [('page_views_clean', 'Page Views'),
                 ('fpl_value_clean', 'FPL Value'),
                 ('fpl_points_clean', 'FPL Points')]:
    if x in df.columns:
        plt.figure(figsize=(6, 4))
        sns.scatterplot(x=x, y='market_value_num', data=df)
        plt.xlabel(label)
        plt.ylabel("Market Value")
        plt.title(f"Market Value vs {label}")
        plt.tight_layout()
        plt.show()

# ==============================
# 7. SAVE CLEANED DATA
# ==============================
df.to_csv("football_players_cleaned.csv", index=False)
print("\nCleaned dataset saved as football_players_cleaned.csv")
