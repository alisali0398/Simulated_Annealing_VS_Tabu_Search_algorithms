import itertools
import random
import numpy as np
import matplotlib.pyplot as plt
import collections

def route_length(route, matrix):
    """Compute the total route cost, including return to the starting city."""
    return sum(matrix[route[i], route[i + 1]] for i in range(len(route) - 1)) + matrix[route[-1], route[0]]


# Exhaustive Search
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

# Simulated Annealing
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

# Tabu Search
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

# Run all algorithms
# EE
ex_route, ex_cost, ex_evals = exhaustive_search(q3_matrix)
print("Exhaustive Search -> Best cost:", ex_cost, "| Route:", [x+1 for x in ex_route], "| Evaluations:", ex_evals)

# SA
sa_route, sa_cost, sa_history, sa_evals = simulated_annealing(q3_matrix)
print("Simulated Annealing -> Best cost:", sa_cost, "| Route:", [x+1 for x in sa_route], "| Evaluations:", sa_evals)

# TS
ts_route, ts_cost, ts_history, ts_evals = tabu_search(q3_matrix)
print("Tabu Search -> Best cost:", ts_cost, "| Route:", [x+1 for x in ts_route], "| Evaluations:", ts_evals)


# Plot
plt.figure(figsize=(10, 5))
plt.plot(sa_history, label="Simulated Annealing")
plt.plot(ts_history, label="Tabu Search")
plt.axhline(y=ex_cost, color="r", linestyle="--", label="Exhaustive Optimum")
plt.title("Comparison of SA vs Tabu vs Exhaustive")
plt.xlabel("Iteration")
plt.ylabel("Route Cost")
plt.legend()
plt.grid(True)
plt.show()
