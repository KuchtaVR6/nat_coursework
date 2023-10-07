import numpy as np


class Problem:
    """ A generic class for representing problems,
    for which solutions are vectors and fitness can be represented as a scalar """

    def __init__(self, number_of_dimensions):
        self.number_of_dimensions = number_of_dimensions

    def generate_random_solution(self) -> np.ndarray:
        # to be overwritten
        raise Exception("This method is abstract")

    def evaluate_fitness(self, solution: np.ndarray) -> float:
        # to be overwritten
        raise Exception("This method is abstract")
