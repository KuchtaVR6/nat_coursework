from sumpleteGame import SumpleteGame
from problemDefinition import SumpleteProblem, SumpleteProblemSubtaskA
from geneticAlgorithmForVectorProblems import GeneticAlgorithmForVectorProblems

matrix_size = 3

game = SumpleteGame(matrix_size)

sumpleteProblemSubtaskA = SumpleteProblemSubtaskA(game)
sumpleteProblem = SumpleteProblem(game)

def search_for_good_params():
    for population_size in range(100, 401, 10):
        game = SumpleteGame(matrix_size)
        sumpleteProblem = SumpleteProblemSubtaskA(game)

        for mutation_rate_times_ten in range(1, 10, 1):
            mutation_rate = mutation_rate_times_ten / 10
            for crossover_rate_times_ten in range(1, 10, 1):
                budget = 100000

                crossover_rate = crossover_rate_times_ten / 10

                solution_reached_counter = 0

                overall_evaluation_performed = 0

                while overall_evaluation_performed < budget:
                    genetic_algorithm = GeneticAlgorithmForVectorProblems(sumpleteProblem, population_size,
                                                                          mutation_rate, crossover_rate)

                    for generations in range(0, 50):
                        genetic_algorithm.compute_n_generations(1)

                        if sumpleteProblem.check_if_correct_solution(genetic_algorithm.best_solution_ever[0]):
                            solution_reached_counter += 1
                            break

                        if overall_evaluation_performed + genetic_algorithm.evaluations_performed > budget:
                            break

                    overall_evaluation_performed += genetic_algorithm.evaluations_performed

                print(population_size, ";", mutation_rate, ";", crossover_rate, ";", solution_reached_counter)

'''subtask a'''

# for dimensionality in range(2, 7):
#     dim_game = SumpleteGame(dimensionality)
#     dim_problemClass = SumpleteProblemSubtaskA(dim_game)
#
#     solutions_found = 0
#
#     for reset in range(0, 100):
#         model = GeneticAlgorithmForVectorProblems(dim_problemClass, 300, 0.5, 0.5)
#
#         model.compute_n_generations(50)
#
#         if model.best_solution_ever[1] == 1:
#             solutions_found += 1
#
#     print(f'{dimensionality}D:{solutions_found}')

'''subtask b'''

for dimensionality in range(2, 7):
    dim_game = SumpleteGame(dimensionality)
    dim_problemClass = SumpleteProblem(dim_game)

    solutions_found = 0

    for reset in range(0, 100):
        model = GeneticAlgorithmForVectorProblems(dim_problemClass,
                                                  150, 0.2, 0.8)

        model.compute_n_generations(100)

        if dim_problemClass.check_if_correct_solution(model.best_solution_ever[0]):
            solutions_found += 1

    print(f'{dimensionality}D:{solutions_found}')