"""
PART 5 : GENETIC ALGORITHM (Feature Weight Optimization for KNN)
Predicting the Price of a Football Player
-----------------------------------------
This script implements a Genetic Algorithm to optimize feature weights
for K-Nearest Neighbors Regressor. Includes diversity maintenance
(random immigrants strategy).
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score
import random

# ==============================
# 1. LOAD DATA
# ==============================
df = pd.read_csv("football_players_cleaned.csv")
df = df.dropna(subset=["market_value_num"])

X = df.select_dtypes(include=[np.number]).drop(columns=["market_value_num"], errors="ignore")
X = X.replace([np.inf, -np.inf], np.nan).fillna(X.mean())
X = X.loc[:, X.std() > 0]
y = df["market_value_num"]

print(f"\nDataset ready for GA: X={X.shape}, y={y.shape}")

# ==============================
# 2. TRAIN-TEST SPLIT
# ==============================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
n_features = X_train_scaled.shape[1]

# ==============================
# 3. GA PARAMETERS
# ==============================
POP_SIZE = 20
N_GENERATIONS = 30
MUTATION_RATE = 0.2
CROSSOVER_RATE = 0.7
ELITE_SIZE = 4
IMMIGRANT_RATE = 0.1  # Random immigrants for diversity
K = 5  # KNN neighbors

# ==============================
# 4. HELPER FUNCTIONS
# ==============================
def evaluate_fitness(weights):
    """Compute fitness as R² score of weighted KNN model."""
    weighted_train = X_train_scaled * weights
    weighted_test = X_test_scaled * weights

    model = KNeighborsRegressor(n_neighbors=K)
    model.fit(weighted_train, y_train)
    preds = model.predict(weighted_test)
    return r2_score(y_test, preds)

def create_individual():
    """Random individual = random weights between 0 and 1."""
    return np.random.rand(n_features)

def mutate(individual):
    """Randomly alter genes."""
    for i in range(n_features):
        if random.random() < MUTATION_RATE:
            individual[i] = np.clip(individual[i] + np.random.normal(0, 0.1), 0, 1)
    return individual

def crossover(parent1, parent2):
    """Single-point crossover."""
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, n_features - 1)
        child1 = np.concatenate((parent1[:point], parent2[point:]))
        child2 = np.concatenate((parent2[:point], parent1[point:]))
        return child1, child2
    return parent1.copy(), parent2.copy()

# ==============================
# 5. INITIAL POPULATION
# ==============================
population = [create_individual() for _ in range(POP_SIZE)]

# ==============================
# 6. EVOLUTION LOOP
# ==============================
for gen in range(N_GENERATIONS):
    fitness = np.array([evaluate_fitness(ind) for ind in population])
    best_idx = np.argmax(fitness)
    print(f"Generation {gen+1}/{N_GENERATIONS} | Best R²: {fitness[best_idx]:.4f}")

    # Elitism: preserve top ELITE_SIZE individuals
    sorted_indices = np.argsort(fitness)[::-1]
    new_pop = [population[i].copy() for i in sorted_indices[:ELITE_SIZE]]

    # Crossover
    while len(new_pop) < POP_SIZE:
        parents = random.sample(list(range(ELITE_SIZE)), 2)
        child1, child2 = crossover(population[parents[0]], population[parents[1]])
        new_pop.append(mutate(child1))
        if len(new_pop) < POP_SIZE:
            new_pop.append(mutate(child2))

    # Random immigrants (diversity)
    n_immigrants = int(IMMIGRANT_RATE * POP_SIZE)
    for _ in range(n_immigrants):
        new_pop[random.randint(ELITE_SIZE, POP_SIZE - 1)] = create_individual()

    population = new_pop

# ==============================
# 7. FINAL RESULTS
# ==============================
final_fitness = np.array([evaluate_fitness(ind) for ind in population])
best_idx = np.argmax(final_fitness)
best_weights = population[best_idx]
best_score = final_fitness[best_idx]

print("\n----- FINAL GA RESULTS -----")
print(f"Best R² Score: {best_score:.4f}")
print(f"Best Feature Weights:\n{best_weights}")

# Save best weights
np.savetxt("best_knn_weights.csv", best_weights, delimiter=",")
print("\nBest weights saved as best_knn_weights.csv")
