# Natural Computing coursework
Patryk Kuchta - s2595201
## Problem 1

Specification of the problem chosen:
I have decided to work on minimising the output of the provided Rastrigin function, where all dimensions are
searched within -5.12 to 5.12.

The algorithm I have chosen is the Particle Swarm Optimization algorithm.

### Question a)

First I have fixed the difficulty of the problem to 5 dimensions. The cost function is defined as:
```python
def evaluate_fitness(self, solution: np.ndarray) -> float:
    penalties = 0

    # apply a penalty for values over max
    penalties += np.sum(solution[solution > self.solution_boundary[1]] ** 2)
    # apply a penalty for values below min
    penalties += np.sum(solution[solution < self.solution_boundary[0]] ** 2)

    # we are trying to minimise penalties and the function therefore fitness will be * -1
    return (NDimensionalRastriginProblem.__variable_rastrigin_function(solution) + penalties) * -1
```
Which is the output of the Rastrigin function, with the added penalties, which is the summed squared difference 
between the search space boundary and the value for each dimension that has left the search boundary. Penalties
will always equal 0 if all dimensions are within the search space. This number is multiplied by * -1, because
the algorithm I have written tries to maximise the fitness.

My methodology for finding the optimal population size will for each population size tested (starting from 1)
record the number of iterations before reaching an acceptable (which I will be anything that is more than -8),
but with all the dimensions within the search space.

Because there is a high chance that PSO will be unable to find an optimum this good (especially for small 
populations), run the algorithm 100 times and if it is able to find a good enough optimum, its number of
iterations will be taken into considerations and average over all successful runs. If it is unable to find
the optimal value it will be recorded in the success rate.

Based on these plots
```
insert plots here
```
The testing points that 29 is an optimal population value for this problem. The success rate was at a local
peak at 0.66, which means 2 out of 3 runs were successful and finding this optimum, and it only took 149 
iterations on average. Of course higher populations produce better numbers but have a much higher computational
cost.
