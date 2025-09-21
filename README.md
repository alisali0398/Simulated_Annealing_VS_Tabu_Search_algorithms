# Simulated_Annealing_VS_Tabu_Search_algorithms
SA VS TS test case

The purpose of this case study is to solve a 10-node Travel Salesman Problem (TSP): find the shortest tour which starts from node 1, visits 
each node once, and returns to node 1 with the shortest distance.

The distance matrix is provided below. This problem is symmetric so the distance from city i to city j is the same as that from city j and city i.

<img width="915" height="281" alt="image" src="https://github.com/user-attachments/assets/21917d4e-2843-4c82-b281-846446e3448b" />

## Exhaustive enumeration (EE) 

Since the tour must start at the node 1 and visit each of the remaining 9 nodes exactly once, the total number of possible routes is 9! = 362880 permutations. As it is almost impossible to evaluate all permutations manually, a Python code was written to perform the exhaustive search. 

## Special modification made and the algorithmic parameters (SA): 

* Cooling schedule:

Geometrical cooling schedule T(k) = t<sub>0</sub> * α<sup>k</sup>, where t<sub>0</sub> = 1000 and α = 0.995

* Stopping criterium:

The process continues until the temperature drops below T<sub>min</sub>= 0.001

* Number of iterations at specific temperature: 

The algorithm performs one solution update per temperature step. 

* How many times was the objective function (total distance computation) evaluated to find the optimal solution? 

The objective function was evaluated 2758 times. Each evaluation corresponds to a proposed new solution during the optimization process. 

* How close is your result compared to the global optimal solution?
  
The best solution found by SA has a total cost of 612, while the global optimal solution found by EE is 592. 

Difference from optimum: 612 − 592 = 20

Relative deviation: 20/592 ∗ 100 = 3.38% above the global optimum 

