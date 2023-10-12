from particleSwarmOptimisation import ParticleSwarmOptimization
from problemDefinition import NDimensionalRastriginProblem

problem = NDimensionalRastriginProblem(5, (-5.12, 5.12))
model = ParticleSwarmOptimization(problem, 0.9, 2, 2, 25)

for population_size in range(1, 100):
    iterations_sum = 0
    trials_passed = 0

    for trial in range(1, 100):
        test_model = ParticleSwarmOptimization(problem, 0.9, 2, 2, population_size)
        solution_found = False

        for iteration in range(1, 2000):
            test_model.run_for_n_iterations(1)
            if problem.check_if_solution_valid(test_model.global_best[0]):
                if problem.evaluate_fitness(test_model.global_best[0]) > -8:
                    solution_found = True
                    break
        if solution_found:
            iterations_sum += iteration
            trials_passed += 1

    if trials_passed > 0:
        print('for population_size', population_size, 'average iterations', iterations_sum / trials_passed, 'trials passed are', trials_passed)

print(model.global_best)
