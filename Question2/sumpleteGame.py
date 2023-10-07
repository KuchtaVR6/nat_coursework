import math

import numpy as np


class SumpleteGame:
    """ Each instance is a sumplete game generated randomly given matrix size, optionally deletion_rate """
    def __init__(self, matrix_size: int, deletion_rate=1/3):
        self.matrix_size = matrix_size
        self.board = np.random.randint(1, 10, size=(matrix_size, matrix_size))

        self.deletion_mask = np.zeros((matrix_size, matrix_size))
        scores_deletion = np.random.rand(matrix_size, matrix_size)
        self.deletion_mask[scores_deletion < deletion_rate] = 1

        self.correct_sums = {}
        board_without_deleted_values = self.board * self.deletion_mask
        self.correct_sums['cols'] = board_without_deleted_values.sum(axis=0)
        self.correct_sums['rows'] = board_without_deleted_values.sum(axis=1)

    def calculate_the_sums_given_solution(self, solution_vector: np.ndarray) -> [np.ndarray, np.ndarray]:
        solution_mask = solution_vector.reshape((self.matrix_size, self.matrix_size))
        board_without_suggested_deleted_values = self.board * solution_mask

        solution_column_sums = board_without_suggested_deleted_values.sum(axis=0)
        solution_row_sums = board_without_suggested_deleted_values.sum(axis=1)
        return [solution_row_sums, solution_column_sums]