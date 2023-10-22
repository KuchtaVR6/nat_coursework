import numpy as np


class Problem:
    """ A generic abstract class for representing problems,
    for which solutions are vectors and fitness can be represented as a scalar """

    def __init__(self, number_of_dimensions):
        self.number_of_dimensions = number_of_dimensions

    def generate_random_solution(self):
        # to be overwritten
        raise Exception("This method is abstract")

    def evaluate_fitness(self, solution) -> float:
        # to be overwritten
        raise Exception("This method is abstract")


class ProblemWithMutationScheme(Problem):
    """ Abstract class, adding the mutation functionality"""
    def mutate_solution(self, solution: np.ndarray) -> np.ndarray:
        # to be overwritten
        raise Exception("This method is abstract")
