"""
PART 2 : MODEL BUILDING
Predicting the Price of a Football Player
-----------------------------------------
This script loads the cleaned dataset, extracts usable numeric features,
and builds multiple regression models to predict market value.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# ==============================
# 1. LOAD AND PREPARE DATA
# ==============================
df = pd.read_csv("football_players_cleaned.csv")

# Ensure target exists
if "market_value_num" not in df.columns:
    raise ValueError("Target column 'market_value_num' not found in dataset. Run Part 1 first.")

df = df.dropna(subset=["market_value_num"])

# ------------------------------
# Select numeric features only
# ------------------------------
# Convert any object columns that might be numeric-like
for col in df.columns:
    if df[col].dtype == object:
        df[col] = pd.to_numeric(df[col], errors='ignore')

# Select numeric columns and drop non-informative ones (std = 0)
X = df.select_dtypes(include=[np.number]).drop(columns=["market_value_num"], errors="ignore")
X = X.loc[:, X.std() > 0]  # remove constant columns
y = df["market_value_num"]

print(f"\nInitial numeric shape: X={X.shape}, y={y.shape}")

# Replace inf and NaN safely
X = X.replace([np.inf, -np.inf], np.nan)
X = X.fillna(X.mean())

# Drop any column that’s still all NaN
X = X.dropna(axis=1, how='all')

print(f"After cleaning columns: X={X.shape}, y={y.shape}")

# ==============================
# 2. TRAIN-TEST SPLIT
# ==============================
if len(X) < 5:
    raise ValueError("Not enough valid samples left to train. Check numeric cleaning.")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==============================
# 3. DEFINE MODELS
# ==============================
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Lasso Regression": Lasso(alpha=0.01, max_iter=10000),
    "KNN Regressor": KNeighborsRegressor(n_neighbors=5),
    "SVR (RBF Kernel)": SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(random_state=42)
}

# ==============================
# 4. TRAIN AND EVALUATE
# ==============================
results = []

for name, model in models.items():
    # Use scaled data where needed
    if name in ["Linear Regression", "Ridge Regression", "Lasso Regression",
                "KNN Regressor", "SVR (RBF Kernel)"]:
        model.fit(X_train_scaled, y_train)
        preds = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, preds))
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    results.append([name, round(rmse, 2), round(mae, 2), round(r2, 3)])

# ==============================
# 5. DISPLAY RESULTS
# ==============================
results_df = pd.DataFrame(results, columns=["Model", "RMSE", "MAE", "R2_Score"])
results_df = results_df.sort_values(by="R2_Score", ascending=False)

print("\n----- MODEL PERFORMANCE SUMMARY -----\n")
print(results_df.to_string(index=False))

results_df.to_csv("model_performance_summary.csv", index=False)
best_model = results_df.iloc[0]["Model"]
print(f"\nBest Performing Model: {best_model}")
print("\nResults saved as model_performance_summary.csv")
