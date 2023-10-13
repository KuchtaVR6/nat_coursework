from sumpleteGame import SumpleteGame
from problemDefinition import SumpleteProblem, SumpleteProblemSubtaskA
from geneticAlgorithm import GeneticAlgorithm

matrix_size = 5

game = SumpleteGame(matrix_size)

sumpleteProblemSubtaskA = SumpleteProblemSubtaskA(game)
sumpleteProblem = SumpleteProblem(game)

# todo current algorithm can loose the best solution
# todo extra reward for reaching 0 in the fitness

genetic_algorithm = GeneticAlgorithm(sumpleteProblem, 200, 0.1, 0.4)

genetic_algorithm.compute_n_generations(1000, verbose=True)

print('Final solution is:', genetic_algorithm.best_solution_currently())
