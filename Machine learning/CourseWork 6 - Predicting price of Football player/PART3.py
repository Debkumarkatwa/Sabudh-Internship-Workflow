"""
PART 3 : HYPERPARAMETER TUNING
Predicting the Price of a Football Player
-----------------------------------------
This script performs GridSearchCV on top models (Ridge, Lasso,
Random Forest, Gradient Boosting) to find the best hyperparameters.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# =====================================================
# 1. LOAD CLEANED DATA
# =====================================================
df = pd.read_csv("football_players_cleaned.csv")
df = df.dropna(subset=["market_value_num"])

# keep only numeric columns
X = df.select_dtypes(include=[np.number]).drop(columns=["market_value_num"], errors="ignore")
X = X.replace([np.inf, -np.inf], np.nan).fillna(X.mean())
X = X.loc[:, X.std() > 0]
y = df["market_value_num"]

print(f"\nDataset ready: X={X.shape}, y={y.shape}")

# =====================================================
# 2. SPLIT & SCALE
# =====================================================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# =====================================================
# 3. GRID SEARCH SETUPS
# =====================================================
grids = {
    "Ridge": (Ridge(), {
        "alpha": [0.001, 0.01, 0.1, 1.0, 10, 100]
    }),
    "Lasso": (Lasso(max_iter=10000), {
        "alpha": [0.0001, 0.001, 0.01, 0.1, 1.0]
    }),
    "RandomForest": (RandomForestRegressor(random_state=42), {
        "n_estimators": [50, 100, 200],
        "max_depth": [None, 5, 10, 20],
        "min_samples_split": [2, 5, 10]
    }),
    "GradientBoosting": (GradientBoostingRegressor(random_state=42), {
        "n_estimators": [100, 200],
        "learning_rate": [0.01, 0.05, 0.1, 0.2],
        "max_depth": [2, 3, 5]
    })
}

# =====================================================
# 4. PERFORM GRID SEARCH
# =====================================================
results = []

for name, (model, params) in grids.items():
    print(f"\n🔍 Tuning {name}...")
    use_scaled = name in ["Ridge", "Lasso"]

    gs = GridSearchCV(
        estimator=model,
        param_grid=params,
        scoring="r2",
        cv=5,
        n_jobs=-1,
        verbose=0
    )

    gs.fit(X_train_scaled if use_scaled else X_train,
           y_train)

    best_model = gs.best_estimator_
    preds = best_model.predict(X_test_scaled if use_scaled else X_test)

    r2 = r2_score(y_test, preds)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    mae = mean_absolute_error(y_test, preds)

    print(f"Best Params: {gs.best_params_}")
    print(f"Test R²: {r2:.4f}, RMSE: {rmse:.4f}, MAE: {mae:.4f}")

    results.append([name, gs.best_params_, round(r2, 4), round(rmse, 4), round(mae, 4)])

# =====================================================
# 5. SUMMARY & SAVE
# =====================================================
summary = pd.DataFrame(results, columns=["Model", "Best_Params", "R2_Score", "RMSE", "MAE"])
summary = summary.sort_values(by="R2_Score", ascending=False)
print("\n----- HYPERPARAMETER TUNING RESULTS -----\n")
print(summary.to_string(index=False))

summary.to_csv("hyperparameter_tuning_results.csv", index=False)
print("\nResults saved as hyperparameter_tuning_results.csv")
