# Natural Computing coursework
Patryk Kuchta - s2595201
## Problem 1

Specification of the problem chosen:
I have decided to work on minimising the output of the provided Rastrigin function, where all dimensions are
searched within -5.12 to 5.12.

It is important to note that an inspection of this function on a graph quickly reveals that this function can
easily 'trap' any algorithm into a local optimum hence the expectations for the performance of the algorithm 
cannot be too high in this case.

The algorithm I have chosen is the Particle Swarm Optimization algorithm.

### Question a)

**Fitness**

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
the algorithm I have written is aimed at maximising the fitness.

My methodology for finding the optimal population size will for each population size tested (starting from 1)
record the number of iterations before reaching an acceptable solution (more on that later), but only if all 
the dimensions are within the search space, until reaching the population of 60.

**Acceptable solutions**

Acceptable solutions have been selected based on running the PSO algorithm for the same problem but with 
generous population of 100, 300 iterations and this algorithm has been run for 10 times to select the best
output of all 10 of the tests.

Because there is a high chance that PSO will be unable to find an optimum this good (especially for small 
populations), run the algorithm 100 times and if it is able to find a good enough optimum, its number of
iterations will be taken into considerations and average over all successful runs. If it is unable to find
the optimal value it will be recorded in the success rate.

Using this methodology, the best optimum found for 5 dimensions had the fitness of `-3.233616069943885`
therefore the fitness that be required for the solution to be deemed as good enough will be `-9.700848209831655`.

**Findings**

> TODO redo this bit with new data

Based on these plots
```
insert plots here
```
The testing points that 29 is an optimal population value for this problem. The success rate was at a local
peak at 0.66, which means 2 out of 3 runs were successful and finding this optimum, and it only took 149 
iterations on average. Of course higher populations produce better numbers but have a much higher computational
cost.

Please note that populations size below 4, have never produced a satisfying output, therefore the data and
plots start from population 4.

### Question b)

To answer this task I will examine what are the optimal values for the following problem complexities (numbers
of dimensions of the solution): 2, 3, 4, 5, 6, 7.

One adjustment to the previous approach will be tho limit the maximum population size in the search to 60, as
this is the range that the optimal values will likely occur.

Based on a run of PSO algorithm with generous computational power (just like in task a), the best solutions 
found are:

```
2D: -0.49747968580168944
3D: -0.7462195287025324
4D: -0.994959371603386
5D: -3.233616069943885
6D: -3.4823559128459323
7D: -5.721012612624037
```

Because Rastrigin is quite challenging, I will assume that anything better than ```3 * best_optimum_found```
can be considered a good enough solution therefore minimal solution at which the algorithm will stop iterating
will be:

```
2D: -1.4924390574050683
3D: -2.238658586107597
4D: -2.984878114810158
5D: -9.700848209831655
6D: -10.447067738537797
7D: -17.16303783787211
```

> TODO continue

## Question 2

Encoding, will be in a k^2 binary vector where each scalar denotes whether a given value in the games matrix
should be deleted or not (deletion = 0, retention = 1), and ought to be read as

``` Deletion_of(x,y) = Encoding_vector(k*y + x)  ```

(i.e. flattening the matrix into a vector)

This makes the mutations simple, as they could simply be based on bit flipping, and the fitness_evaluation is
also quite computationally simple, which is great as this operation will be performed often.

> TODO discuss the parameters here 

### Question a)

> TODO This question

### Question b)

A fitness function better suited for larger instances of the problem would be a fitness function that will
tell the model when it is getting closer to the correct solution as this will allow it to select better solutions
for the future generations. One algorithm capable of doing that is this:

```python
def evaluate_fitness(self, solution: np.ndarray) -> float:
    solution_sums = self.game.calculate_the_sums_given_solution(solution)

    row_wise_errors_squared = (self.game.correct_sums['rows'] - solution_sums[0]) ** 2
    column_wise_errors_squared = (self.game.correct_sums['cols'] - solution_sums[1]) ** 2

    # because we are minimising the error we multiply by -1
    return (np.sum(row_wise_errors_squared) + np.sum(column_wise_errors_squared)) * -1
```

The fitness in this function is defined as the sum of square differences between the correct sums and
the sums that the given solution gives. Because again the algorithm use maximises fitness, this number
has to be multiplied by -1 in order for the algorithm to work properly.





