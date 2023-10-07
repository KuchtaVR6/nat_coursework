from sumpleteGame import SumpleteGame
from problemDefinition import SumpleteProblem, SumpleteProblemSubtaskA

matrix_size = 5

game = SumpleteGame(matrix_size)

sumpleteProblemSubtaskA = SumpleteProblemSubtaskA(game)
sumpleteProblem = SumpleteProblem(game)

print(sumpleteProblem.evaluate_fitness(game.deletion_mask),
      sumpleteProblemSubtaskA.evaluate_fitness(game.deletion_mask))
