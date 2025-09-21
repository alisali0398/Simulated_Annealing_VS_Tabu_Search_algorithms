# Simulated_Annealing_VS_Tabu_Search_algorithms
SA VS TS test case

The purpose of this case study is to solve a 10-node Travel Salesman Problem (TSP): find the shortest tour which starts from node 1, visits 
each node once, and returns to node 1 with the shortest distance.

The distance matrix is provided below. This problem is symmetric so the distance from city i to city j is the same as that from city j and city i.

<img width="915" height="281" alt="image" src="https://github.com/user-attachments/assets/21917d4e-2843-4c82-b281-846446e3448b" />

## Exhaustive enumeration (EE) 

Since the tour must start at the node 1 and visit each of the remaining 9 nodes exactly once, the total number of possible routes is 9! = 362880 permutations. As it is 
almost impossible to evaluate all permutations manually, a Python code was written to perform the exhaustive search. 
