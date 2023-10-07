import math
import numpy as np
from problemClass import Problem


class NDimensionalRastriginProblem(Problem):

    def __init__(self, number_of_dimensions: int, solution_boundary=(-1, 1)):
        super().__init__(number_of_dimensions)
        if solution_boundary[0] >= solution_boundary[1]:
            raise Exception('Solution boundary defined incorrectly')

        self.solution_boundary = solution_boundary

    def generate_random_solution(self):
        return (np.random.rand(self.number_of_dimensions) *
                (self.solution_boundary[1] - self.solution_boundary[0]) + self.solution_boundary[0])

    def evaluate_fitness(self, solution: np.ndarray) -> float:
        penalties = 0

        # apply a penalty for values over max
        penalties += np.sum(solution[solution > self.solution_boundary[1]] ** 2)
        # apply a penalty for values below min
        penalties += np.sum(solution[solution < self.solution_boundary[0]] ** 2)

        # we are trying to minimise penalties and the function therefore fitness will be * -1
        return (NDimensionalRastriginProblem.__variable_rastrigin_function(solution) + penalties) * -1

    def __variable_rastrigin_function(input_vector: np.ndarray) -> float:
        # private static
        number_of_dims = len(input_vector)

        overall_sum = 0

        for input_scalar in input_vector:
            overall_sum += input_scalar ** 2 + 10 * math.cos(2 * math.pi * input_scalar)

        return 10 * number_of_dims + overall_sum
