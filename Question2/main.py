from sumpleteGame import SumpleteGame
from problemDefinition import SumpleteProblem, SumpleteProblemSubtaskA
from geneticAlgorithm import GeneticAlgorithm

matrix_size = 5

game = SumpleteGame(matrix_size)

sumpleteProblemSubtaskA = SumpleteProblemSubtaskA(game)
sumpleteProblem = SumpleteProblem(game)

genetic_algorithm = GeneticAlgorithm(sumpleteProblem, 10, 0.2, 0.4)

for _ in range(30):
    print('current best', genetic_algorithm.best_solution_currently()[1])
    genetic_algorithm.compute_generation()

print('current best', genetic_algorithm.best_solution_currently()[1])
