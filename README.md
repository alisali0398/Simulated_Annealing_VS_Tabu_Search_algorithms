# Simulated_Annealing_VS_Tabu_Search_algorithms
SA VS TS test case

The purpose of this case study is to solve a 10-node Travel Salesman Problem (TSP): find the shortest tour which starts from node 1, visits 
each node once, and returns to node 1 with the shortest distance.

The distance matrix is provided below. This problem is symmetric so the distance from city i to city j is the same as that from city j and city i.

<img width="915" height="281" alt="image" src="https://github.com/user-attachments/assets/21917d4e-2843-4c82-b281-846446e3448b" />

## Exhaustive enumeration (EE) 

Since the tour must start at the node 1 and visit each of the remaining 9 nodes exactly once, the total number of possible routes is 9! = 362880 permutations. As it is almost impossible to evaluate all permutations manually, a Python code was written to perform the exhaustive search. 

EE code can be found in a separate file.

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

SA produced a near optimum solution with significantly lower function evaluations, which means SA provide relatively high quality results within limited computational effort. 

SA code can be found in a separate file. 


## Special modification made and the algorithmic parameters (TS): 

* Tabu tenure:
  
The tabu tenure is set to 10 iterations 

* Frequency penalty:
  
The penalty is computed as a weighted sum of the move frequencies, scaled by a factor of 0.1


* How many times was the objective function (total distance computation) evaluated to find the optimal solution? 

The objective function was evaluated 18501 times. The number of iterations is 500, each iteration checks 36 neighbors, and for each one, the total route cost is computed. An additional evaluation is made for the accepted solution after each iteration and once at the start.

* How close is your result compared to the global optimal solution?

The best solution found by TS has a total cost of 592, while the global optimal solution found by EE is 592. 

Difference from optimum: 592 − 592 = 0

Relative deviation is 0%, the result is the same as for EE. 

TS fully explored the solution space and successfully escape local minimum, ultimately discovering the globally optimal tour. Although the TS required 18501 evaluations, algorithm achieved the best result and accuracy. 

TS code can be found in a separate file.

## Comparison between EE vs SA vs TS 
Exhaustive Enumeration (EE) guarantees the global optimum solution (cost 592) but requires a high number of evaluations — 362880. Simulated Annealing (SA) found 
a near optimal solution (cost 612) with only 2758 evaluations, resulting in a 3.38% deviation from the optimum. Tabu Search (TS) matched the global optimum (cost 
592) using 18501 evaluations, leveraging memory based strategies to escape local minima. Overall, EE is exact but computationally expensive, SA is efficient but 
approximate, and TS combines high accuracy with strong performance, making it the most balanced approach. 

Comparison code can be found in a separate file.
