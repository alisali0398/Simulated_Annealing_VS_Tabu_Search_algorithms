import numpy as np
import matplotlib.pyplot as plt
import random

def route_length(route, matrix):
    """Compute the total route cost, including return to the starting city."""
    return sum(matrix[route[i], route[i + 1]] for i in range(len(route) - 1)) + matrix[route[-1], route[0]]

def simulated_annealing(matrix, T_start=1000, T_end=1e-3, alpha=0.995):
    """Simulated Annealing algorithm for TSP using random swaps and geometric cooling."""
    n = len(matrix)
    route = list(range(n))
    random.shuffle(route[1:])  # keep city 0 fixed at the start
    cost = route_length(route, matrix)

    best_route = route[:]
    best_cost = cost

    T = T_start
    cost_history = [cost]
    eval_count = 1

    while T > T_end:
        # Pick two random cities to swap (excluding start city)
        i, j = random.sample(range(1, n), 2)
        new_route = route[:]
        new_route[i], new_route[j] = new_route[j], new_route[i]
        new_cost = route_length(new_route, matrix)
        eval_count += 1

        delta = new_cost - cost
        # Accept if better or with probability based on temperature
        if delta < 0 or random.random() < np.exp(-delta / T):
            route = new_route
            cost = new_cost
            if cost < best_cost:
                best_route = new_route[:]
                best_cost = cost

        cost_history.append(cost)
        T *= alpha

    return best_route, best_cost, cost_history, eval_count


# Distance matrix (10x10, symmetric TSP)
q3_matrix = np.array([
    [0, 76, 91, 61, 71, 55, 54, 78, 59, 96],
    [76, 0, 60, 82, 64, 64, 51, 82, 99, 87],
    [91, 60, 0, 67, 92, 98, 68, 64, 74, 76],
    [61, 82, 67, 0, 95, 95, 88, 83, 74, 69],
    [71, 64, 92, 95, 0, 67, 54, 94, 57, 91],
    [55, 64, 98, 95, 67, 0, 62, 71, 85, 71],
    [54, 51, 68, 88, 54, 62, 0, 100, 66, 73],
    [78, 82, 64, 83, 94, 71, 100, 0, 50, 85],
    [59, 99, 74, 74, 57, 85, 66, 50, 0, 61],
    [96, 87, 76, 69, 91, 71, 73, 85, 61, 0]
])

# Run SA
sa_route, sa_cost, sa_history, sa_evals = simulated_annealing(q3_matrix)

print("SA route (1-based):", [x + 1 for x in sa_route])
print("Minimum cost found:", sa_cost)
print("Total evaluations:", sa_evals)

# Plot convergence
plt.plot(sa_history)
plt.title("Simulated Annealing Convergence")
plt.xlabel("Iteration")
plt.ylabel("Route cost")
plt.grid(True)
plt.show()
