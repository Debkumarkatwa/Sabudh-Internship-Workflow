"""
PART 4 : MODEL SELECTION + MODEL SAVING
Predicting the Price of a Football Player
-----------------------------------------
Performs K-Fold Cross-Validation to compare models and
selects the best one, then saves it as best_model.pkl for deployment.
"""

import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import KFold, cross_validate
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import make_scorer, mean_squared_error, mean_absolute_error, r2_score

# ==============================
# 1. LOAD CLEANED DATA
# ==============================
df = pd.read_csv("football_players_cleaned.csv")
df = df.dropna(subset=["market_value_num"])

X = df.select_dtypes(include=[np.number]).drop(columns=["market_value_num"], errors="ignore")
X = X.replace([np.inf, -np.inf], np.nan).fillna(X.mean())
X = X.loc[:, X.std() > 0]
y = df["market_value_num"]

print(f"\nDataset ready for model selection: X={X.shape}, y={y.shape}")

# Standardize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==============================
# 2. DEFINE MODELS
# ==============================
models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0),
    "Lasso Regression": Lasso(alpha=0.01, max_iter=10000),
    "Random Forest": RandomForestRegressor(n_estimators=200, random_state=42),
    "Gradient Boosting": GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, max_depth=3, random_state=42)
}

# ==============================
# 3. CROSS VALIDATION
# ==============================
cv = KFold(n_splits=5, shuffle=True, random_state=42)

scoring = {
    'r2': 'r2',
    'neg_rmse': 'neg_root_mean_squared_error',
    'neg_mae': 'neg_mean_absolute_error'
}

results = []

for name, model in models.items():
    print(f"\n⏳ Evaluating {name}...")
    use_scaled = name in ["Linear Regression", "Ridge Regression", "Lasso Regression"]

    scores = cross_validate(
        model,
        X_scaled if use_scaled else X,
        y,
        cv=cv,
        scoring=scoring,
        n_jobs=-1
    )

    mean_r2 = scores['test_r2'].mean()
    mean_rmse = -scores['test_neg_rmse'].mean()
    mean_mae = -scores['test_neg_mae'].mean()

    print(f"Average R² = {mean_r2:.4f}, RMSE = {mean_rmse:.4f}, MAE = {mean_mae:.4f}")
    results.append([name, model, use_scaled, mean_r2, mean_rmse, mean_mae])

# ==============================
# 4. SELECT & SAVE BEST MODEL
# ==============================
summary = pd.DataFrame(
    [[r[0], r[3], r[4], r[5]] for r in results],
    columns=["Model", "Mean_R2", "Mean_RMSE", "Mean_MAE"]
).sort_values(by="Mean_R2", ascending=False)

print("\n----- CROSS VALIDATION SUMMARY -----\n")
print(summary.to_string(index=False))

best_name, best_r2 = summary.iloc[0]["Model"], summary.iloc[0]["Mean_R2"]
print(f"\n✅ Selected Final Model: {best_name} (R²={best_r2:.4f})")

# Retrieve the actual model object & whether it used scaled data
best_tuple = [r for r in results if r[0] == best_name][0]
final_model = best_tuple[1]
use_scaled = best_tuple[2]

# Train final model on full dataset
final_model.fit(X_scaled if use_scaled else X, y)

# Save model and scaler for deployment
joblib.dump(final_model, "best_model.pkl")
joblib.dump(scaler, "scaler.pkl")

summary.to_csv("model_selection_results.csv", index=False)
print("\n✅ Model saved as 'best_model.pkl'")
print("✅ Scaler saved as 'scaler.pkl'")
print("✅ Results saved as 'model_selection_results.csv'")
