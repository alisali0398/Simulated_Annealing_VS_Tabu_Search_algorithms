import itertools
import numpy as np
import matplotlib.pyplot as plt

def route_length(route, matrix):
    """Compute the total route cost, including return to the starting city."""
    return sum(matrix[route[i], route[i + 1]] for i in range(len(route) - 1)) + matrix[route[-1], route[0]]

def exhaustive_search(matrix):
    """Find the global optimum by checking all route permutations."""
    n = len(matrix)
    nodes = list(range(1, n))  # City 0 is fixed as the start
    min_cost = float('inf')
    best_route = None
    eval_count = 0

    for perm in itertools.permutations(nodes):
        route = [0] + list(perm)
        cost = route_length(route, matrix)
        eval_count += 1
        if cost < min_cost:
            min_cost = cost
            best_route = route

    return best_route, min_cost, eval_count

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

# Run exhaustive search
ex_route, ex_cost, ex_evals = exhaustive_search(q3_matrix)
print("Exhaustive route (1-based):", [x + 1 for x in ex_route])
print("Minimum cost:", ex_cost)
print("Total evaluations:", ex_evals)
