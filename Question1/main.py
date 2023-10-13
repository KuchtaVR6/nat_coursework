from particleSwarmOptimisation import ParticleSwarmOptimization
from problemDefinition import NDimensionalRastriginProblem

five_dim_problem = NDimensionalRastriginProblem(5, (-5.12, 5.12))


# q 1 a

def run_the_model_with_generous_params(problem):
    best_found = None

    for i in range(0, 10):
        model = ParticleSwarmOptimization(problem, 0.8, 2, 2, 100)
        model.run_for_n_iterations(300)

        if best_found is None or best_found[1] < model.global_best[1]:
            best_found = model.global_best

    return best_found


def look_for_optimal_population_size(problem, minium_acceptable_fitness, max_population):
    for population_size in range(1, max_population + 1):
        number_of_successes = 0

        no_improvement_limit = 25
        evaluation_budget = 1000000
        overall_evaluations_performed = 0

        while overall_evaluations_performed <= evaluation_budget:
            test_model = ParticleSwarmOptimization(problem, 0.85, 3.5, 0.5,
                                                   population_size)
            solution_found = False
            best_fitness_history = []

            for iteration in range(1, 500):
                test_model.run_for_n_iterations(1)

                if problem.check_if_solution_valid(test_model.global_best[0]):
                    current_fitness = problem.evaluate_fitness(test_model.global_best[0])
                    if (len(best_fitness_history) >= no_improvement_limit and
                            best_fitness_history[-no_improvement_limit] == current_fitness):
                        break
                    best_fitness_history.append(current_fitness)

                    if current_fitness > minium_acceptable_fitness:
                        solution_found = True
                        break

                if test_model.evaluations_performed + overall_evaluations_performed > evaluation_budget:
                    break

            overall_evaluations_performed += test_model.evaluations_performed

            if solution_found:
                number_of_successes += 1

        print(population_size, ';', number_of_successes)


# print(run_the_model_with_generous_params(five_dim_problem))
# look_for_optimal_population_size(five_dim_problem, -3, 100)

# best_found_optimas = []
# min_acceptable_optimas = []
#
# start_from = 2
#
# for problem_dimensionality in range(start_from, 8):
#     problem = NDimensionalRastriginProblem(problem_dimensionality, (-5.12, 5.12))
#     best_optima = run_the_model_with_generous_params(problem)[1]
#     best_found_optimas.append(best_optima)
#     min_acceptable_optimas.append(best_optima*3)
#
# print('best found')
# print(best_found_optimas)
# print('minimum accepted')
# print(min_acceptable_optimas)

min_acceptable_optimas = [-1.4924390574050683, -2.238658586107597, -2.984878114810158, -9.700848209831655,
                          -10.447067738537797, -17.16303783787211]
start_from = 3
end_on = 5

for problem_dimensionality in range(start_from, end_on + 1):
    problem = NDimensionalRastriginProblem(problem_dimensionality, (-5.12, 5.12))
    print(problem_dimensionality, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    look_for_optimal_population_size(problem, min_acceptable_optimas[problem_dimensionality - 2], 60)
    print(problem_dimensionality, '<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')



