import collections
import random
import numpy as np

def route_length(route, matrix):
    """Compute the total route cost, including return to the starting city."""
    return sum(matrix[route[i], route[i + 1]] for i in range(len(route) - 1)) + matrix[route[-1], route[0]]

def tabu_search(matrix, max_iter=500, tabu_tenure=10, penalty_weight=0.1):
    """Tabu Search for TSP using swap-based neighborhood and frequency penalty."""
    n = len(matrix)
    current_route = list(range(n))
    random.shuffle(current_route[1:])  # keep city 0 fixed
    best_route = current_route[:]
    best_cost = route_length(current_route, matrix)
    current_cost = best_cost

    tabu_list = {}
    frequency = collections.defaultdict(int)
    cost_history = [best_cost]
    eval_count = 1  # Count initial route evaluation

    for iteration in range(max_iter):
        best_candidate = None
        best_candidate_cost = float('inf')
        best_move = None

        for i in range(1, n):
            for j in range(i + 1, n):
                candidate = current_route[:]
                candidate[i], candidate[j] = candidate[j], candidate[i]
                move = (min(candidate[i], candidate[j]), max(candidate[i], candidate[j]))

                base_cost = route_length(candidate, matrix)
                eval_count += 1

                # frequency-based penalty
                freq_penalty = penalty_weight * (frequency[candidate[i]] + frequency[candidate[j]])
                penalized_cost = base_cost + freq_penalty

                # admissibility check (aspiration criterion: allow tabu if better than best_cost)
                if (move not in tabu_list or penalized_cost < best_cost) and penalized_cost < best_candidate_cost:
                    best_candidate = candidate
                    best_candidate_cost = penalized_cost
                    best_move = move

        # update current solution
        if best_candidate is None:
            break  # no candidate found
        current_route = best_candidate
        current_cost = route_length(current_route, matrix)
        eval_count += 1

        # update best solution
        if current_cost < best_cost:
            best_cost = current_cost
            best_route = current_route[:]

        # update tabu list and frequency
        if best_move:
            tabu_list[best_move] = iteration + tabu_tenure
            frequency[best_move[0]] += 1
            frequency[best_move[1]] += 1

        # clear expired tabu moves
        tabu_list = {move: expiry for move, expiry in tabu_list.items() if expiry > iteration}

        cost_history.append(current_cost)

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

# Run Tabu Search
ts_route, ts_cost, ts_history, ts_evals = tabu_search(q3_matrix)

print("Tabu Search route (1-based):", [x + 1 for x in ts_route])
print("Minimum cost found:", ts_cost)
print("Total evaluations:", ts_evals)

import matplotlib.pyplot as plt
plt.plot(ts_history)
plt.title("Tabu Search Convergence")
plt.xlabel("Iteration")
plt.ylabel("Route cost")
plt.grid(True)
plt.show()
