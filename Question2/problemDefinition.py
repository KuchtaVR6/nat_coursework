import numpy as np
from problemClass import ProblemWithMutationScheme
from sumpleteGame import SumpleteGame


class BinaryVectorProblemWithMutationScheme(ProblemWithMutationScheme):
    """ Abstract class for binary problems """

    def __init__(self, solution_vector_length: int):
        super().__init__(solution_vector_length)

    def generate_random_solution(self) -> np.ndarray:
        return np.random.randint(0, 2, size=self.number_of_dimensions)

    def mutate_solution(self, solution: np.ndarray) -> np.ndarray:
        index_to_swap = np.random.randint(0, self.number_of_dimensions, 1)[0]
        solution[index_to_swap] = 1 - solution[index_to_swap]  # swaps the binary value
        return solution


class SumpleteProblem(BinaryVectorProblemWithMutationScheme):
    """ Class for the Sumplete Problem, this uses the more robust fitness method from subtask b """

    '''
        Encoding, will be in a k^2 binary vector where each scalar denotes denotes whether
        a given value should be deleted or not (deletion = 0, retention = 1), and ought to be read as

        Deletion_of(x,y) = Encoding_vector(k*y + x) (i.e. flattening the matrix into a vector)
    '''

    def __init__(self, game: SumpleteGame):
        super().__init__(game.matrix_size ** 2)
        self.game = game

    def evaluate_fitness(self, solution: np.ndarray) -> float:
        solution_sums = self.game.calculate_the_sums_given_solution(solution)

        row_wise_errors_squared = (self.game.correct_sums['rows'] - solution_sums[0]) ** 2
        column_wise_errors_squared = (self.game.correct_sums['cols'] - solution_sums[1]) ** 2

        # because we are minimising the error we multiply by -1
        return (np.sum(row_wise_errors_squared) + np.sum(column_wise_errors_squared)) * -1


class SumpleteProblemSubtaskA(SumpleteProblem):
    """ A version of the SumpleteProblem for subtask A (fitness function overwritten) """

    def evaluate_fitness(self, solution: np.ndarray) -> float:
        solution_sums = self.game.calculate_the_sums_given_solution(solution)

        return int(np.array_equal(solution_sums[0], self.game.correct_sums['rows'])
                   and np.array_equal(solution_sums[1], self.game.correct_sums['cols']))
