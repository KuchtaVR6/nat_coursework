# Natural Computing coursework
Patryk Kuchta - s2595201
## Problem 1

Specification of the problem selected:
I have decided to work on minimising the output of the provided Rastrigin function, where all dimensions are
searched within -5.12 to 5.12.

It is important to note that an inspection of this function on a graph quickly reveals that this function can
easily 'trap' any algorithm into a local optimum. Therefore, the expectations for the performance of the algorithm 
cannot be too high in this case.

The algorithm I have chosen is the Particle Swarm Optimization algorithm.

**Fitness Function**

First, I have fixed the difficulty of the problem to five dimensions. The cost function is defined as:
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
Which is the output of the Rastrigin function, with the added penalties, which is the summed squared difference between the search space boundary and the value for each dimension that has left the search boundary. Penalties will always equal 0 if all dimensions are within the search space. This number is multiplied by * -1, because the algorithm I have written is aimed at maximising fitness.

**Acceptable solutions**

Acceptable solutions have been selected based on running the PSO algorithm for the same problem but with a generous population of 100, 300 iterations, and this algorithm has been run for 10 times to select the best output of all 10 of the tests.

Using this methodology, the best optimum found for 5 dimensions had the fitness of `-3.233616069943885` therefore the fitness that be required for the solution to be deemed as good enough will be `-9.700848209831655`, as this will be 3 times the best solution found and this allows the testing to observe and reward 'quite good' solutions not just best possible.

**Parameter selection**

My methodology for finding the parameters will for each population size test (starting from 1) to run the model and record the number of iterations before reaching an acceptable solution, until reaching the population of 60. Please note that for most test the behaviour for small populations is quite random and luck-based, due to the behaviour of the PSO algorithm in those cases.

Because there is a high chance that PSO will be unable to find an optimum this good (especially for small populations), the algorithm is run 100 times, and if it is able to find a good enough optimum, its number of iterations will be taken into the overall average. Otherwise, the failure to find the optimum  will be recorded in the success rate.

> TODO add the paper

The search for a set of optimum parameters has been started by researching the effects of different parameters in terms of particle behaviour and divergence `insert the paper here`, assuming no prior knowledge of the problem the behaviour of both zigzagging and oscillating will could be useful to the problem. To achieve this behaviour, the values of inertia will be kept close to 1, whilst the sum of the forces kept equal to 4. Running the algorithm for a set of very generic parameters (inertia = 0.7, both forces = 2), quickly revealed that the algorithm makes rather slow progress, the global best would be stuck on the current perceived global best for while. 

*Alpha values*

This points to the issue that in this problem there is need to de-emphasize exploitation and focus more on exploration. This pointed first to increasing the personal best force, whilst sacrificing the global best.

> TODO add the graphs

These tests show that increasing the importance of the personal_best has lead to large improvements in the algorithm, but they are coming with the expense of the success rate. Based on these findings, all considerations going forward will use the personal_best_force = 3.5 and global_best_force = 0.5, as these values give a good balance between relatively reliably getting an answer and optimising the number of iterations.

*Inertia*

Similar tests have been performed for different inertia, the findings are:

> TODO add the graphs

In the case of inertia, there is no more clear benefit in changing the value as any improvement in the success rate comes at the expense of the average required number of iterations. Inertia of 0.85 will be used as it has shown good performance in terms of average iterations required, and did not cause the success rate to go too low like in the case of inertia = 0.7.

### Question a)

**Modified test set up**

These tests will be run slightly differently as it will be preferable to produce one metric for each population size rather than a more nuanced two values in the tests for the parameters. In these tests each test of a given population size (still searched between 1 and 100), will be given an equal `budget` for the maximum number of evaluations of the fitness it can perform. Additionally, the model will only be restarted if the progress in the algorithm stops improving* without reaching an acceptable optimum or as soon as the acceptable optimum is reached. The metric for the comparison will be how many times the model was able to reach the acceptable optimum within its evaluation budget. This metric will neatly combine computational cost and the costs associated with not converging with the perceived performance. For simplicity, this metric will be referred to as optimal convergences given k evaluations. The budget has been set to `k = 1 000 000` as this is the largest number feasible with my limited computational power.

*Small note about going over budget, for simplicity going over-budget within an iteration of the algorithm is allowed, but the algorithm will be stopped right after. Although it does introduce as small advantage for bigger populations, it should not be significant to the testing.

The asterix* next to stop improving is because it is difficult to determine when a model is not making progress. Therefore, for the purposes of these test 'stops improving' will be approximated as the model has not made any improvements to the fitness in more than 25 iterations.

**Findings**

For the Rastrigin problem represented in five dimensions, the result of the tests can be reported in this way
```
insert plots here
```
This plot suggests that values between 10 and 34 can be all considered optimal. The data produced is quite noisy, and drawing a single point as definetely the optimal would be ill-judged. If tasked with choosing only one value, the choice of value 20, which is where the maximum performance has been reached, would be a sensible values. However, there is it would be hard to concretely prove that it is better than any other values from 10 to 34.

### Question b)

To answer this task, I will examine what are the optimal values for the following problem complexities (numbers
of dimensions of the solution): 3, 4, 5, 6, 7.

Based on a run of PSO algorithm with generous computational power (just like in task a), the best solutions 
found are:

```
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
3D: -2.238658586107597
4D: -2.984878114810158
5D: -9.700848209831655
6D: -10.447067738537797
7D: -17.16303783787211
```

Please note that as the method for selecting the value is not perfect, it cannot be assumed that thresholds are all representing a proportional or equivalent difficulty for the program. It maybe even argued that the selection method for these values could be a bit more lenient for the higher dimensionality problems.

The tests performed for this section are the same for the previous task.

The testing has produced these results:

> TODO insert plots
 
As this evaluation method and the algorithm tested tend to produce noisy data, a smoothed version of the graph may be easier to analyse:

For all dimensions, except for the dimensionality of three, it is visible that the set of optimal population sizes, stays relatively stable at around populations between 10 and 30. This is because the dynamics of the group, which rely on each of the particles to be drawn to 2 previous optimas, will over time particles will become very similar over time if the set of particles is large enough. Therefore, we are able to observe the slow decrease in the metric as we raise the population as each new particle has a higher chance of not contributing by the virtue of becoming too similar to other particles. This means at one point each new particle becomes less of a benefit and more of a computational burden. This behaviour is kept with the number of dimensions raising because the impact of the group dynamics and the force does not increase nor decrease with respect to the number of dimensions.

The exception is 3 dimensions, where I believe the added computation burden of a growing population was offset by purely increasing the chances of landing on a solution by luck rather than by utilising group dynamics, which makes sense given the whole search space is (10.24)^3, which makes getting a lucky solution quite a frequent occurrence. However its worth noting that even in those peculiar circumstances, the choice of a population from the set 10–30 would still yield good performance in comparison to the rest of the option (although not best). 

## Question 2

Encoding will be achieved by the use of a k^2 binary vector where each scalar denotes whether a given value in the games' matrix should be deleted or not (deletion = 0, retention = 1), and ought to be read as

``` Deletion_of(x,y) = Encoding_vector(k*y + x)  ```

(i.e. flattening the matrix into a vector)

This makes the mutations simple, as they could simply be based on bit flipping, and the fitness_evaluation is also quite computationally simple, which is great as this operation will be performed often.

**Parameter selection**

For this problem, the ranges for possible parameters have been constrained into the following ranges:
- population_size from 100 to 400, with step 10 (i.e. 100, 110, 120..., 390, 400)
- mutation_rate from 0.1 to 0.9, with step 0.1 (i.e. 0.1, 0.2, 0.3..., 0.8, 0.9)
- crossover_rate from 0.1 to 0.9, with step 0.1 (i.e. 0.1, 0.2, 0.3..., 0.8, 0.9)

For each pair of parameters, the genetic algorithm will be run for a number of iterations, until exhausting the given budget of evaluations, restarting after finding a correct solution or when the number of iterations goes above a 20. The final performance metric will be the number of times that the genetic algorithm has reached the correct solution.

This is quite constraining, but it should be able to produce at least meaningful information pointing to better parameters or in the best cases, a good set of parameters.

> TODO talk about selection and mutation

### Question a)

Firstly, selecting the parameters for this problem will be useful. To select the parameters, the 3 x 3 version of the problem will be used so that the computations are a bit faster. The First observations are that given a budget of 100 000 evaluations, the algorithm was still struggling to find the solutions for many parameters. Here are the top 40 best performing parameters tuples.

> TODO insert the tuples here
 
This shows that there is a lot of variances in the mutation_rate and crossover_rate for tuples that still performed well. This points to the fact that in the current state the algorithm doesn't get much of a benefit from crossover and mutations. Mutations nor crossover_rate. One thing that is quite consistent is that the larger population sizes have performed better.

At this point, a selection of a large population (e.g. 300) and any mutation/crossover rate could be chosen.

But this testing done in order to produce an optimal tuple of parameters shows the issues with this fitness function in general, which is that the genetic algorithm has no way of knowing which solutions are better, if they aren't the correct solution (if one of them is, then the algorithm is done regardless). This makes it so that a larger population size necessitates more random initialisations is better as the algorithm is basically reduced in its functionality to just a random search. Mutations even if they happen often are not really useful as it is better to just create a new random solution, rather than mutate an existing one if only thing we know about it is that it is incorrect. Similar argument shows that crossover is not helpful either as the algorithm doesn't know which genomes to cross over as from its point of view they are all equally bad. 

Here are the findings for multiple dimensionality of the problem (using parameters 300, 0.5, 0.5, and 300 iterations, 100 times (each time with a new model (i.e. resetting)). The number represents the number of times the model has reached the correct solution.    

```
2D:100
3D:100
4D:12
5D:0
6D:0
```
 
This shows that as the dimensionality of the problem grows this fitness function becomes more of an issue as random search becomes less and less feasible as we increase the problems complexity.

### Question b)

**Proposed fitness function**

A fitness function better suited for larger instances of the problem will be a fitness function:
- that will tell the model when it is getting closer to the correct solutions
- that will reward getting the correct sum in each dimension
this will allow it to select solutions that are in theory closer to the correct answer for the future generations. This scheme can be represented using the code below:

```python
def evaluate_fitness(self, solution: np.ndarray) -> float:
    solution_sums = self.game.calculate_the_sums_given_solution(solution)

    row_wise_errors_squared = (self.game.correct_sums['rows'] - solution_sums[0]) ** 2
    column_wise_errors_squared = (self.game.correct_sums['cols'] - solution_sums[1]) ** 2

    reaching_zero_reward = (len(row_wise_errors_squared[row_wise_errors_squared == 0]) +
                            len(column_wise_errors_squared[column_wise_errors_squared == 0])) * 4

    # because we are minimising the error, we multiply by -1
    return (np.sum(row_wise_errors_squared) + np.sum(column_wise_errors_squared)) * -1 + reaching_zero_reward
```

The fitness in this function is defined as the negative sum of square differences between the correct sums and
the sums that the given solution gives, plus a +4 reward for each sum that the solution gets correctly. 

**Parameter selection**

To choose the parameters, the analysis was the same as in the previous subtask. However, it after a quick test this fitness function has proven that the number of allowed interactions before the default restarting to 200, because with this fitness function the algorithm is able to make progress for longer.

The best performance has been reached for population_size 150, mutation rate 0.1, and crossover_rate 0.9, and many of the best parameter tuples it mutation_rate was between 0.1 - 0.3 and the crossover_rate 0.7–0.9, and the population_size within 120 to 190. Therefore, to limit the effect of noise which might have been the reason for the best tuple, the final parameters chosen will be:

```
population_size = 150
mutation_rate = 0.2
crossover_rate = 0.8
```

And the results are:

```
2D:91
3D:92
4D:89
5D:33
6D:18
```

### Question c)

Different parameters pairs affect the solution. Crossover rate will tend to create solution that are combinations of low deletion of small values that iteratively get closer to the correct solution. One could consider these solutions as 'not-optimal' as then will have more deletions than other solutions (this is assuming that there is more than one solution which is not always the case for a given game). Population size and mutation rate will tend to create more random solution that can be both considered 'optimal' or 'not-optimal'.

## Problem 3






