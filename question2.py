import numpy as np

'''Generating a Sumplete problem'''

matrix_size = 4
deletion_rate = 1/3

# generating the board
board = np.random.randint(1, 10, size=(matrix_size, matrix_size))

# generating the deletion_mask (i.e. which cells to delete for the correct answer)
# 0 stands for the value ought to be deleted, 1 for it should be retained
deletion_mask = np.zeros((matrix_size, matrix_size))
scores_deletion = np.random.rand(matrix_size, matrix_size)
deletion_mask[scores_deletion < deletion_rate] = 1

# generating the sums
board_without_deleted_values = board * deletion_mask
correct_column_sums = board_without_deleted_values.sum(axis=0)
correct_row_sums = board_without_deleted_values.sum(axis=1)

'''
    Encoding, will be in a k^2 binary vector where each scalar denotes denotes whether
    a given value should be deleted or not (deletion = 0, retention = 1), and ought to be read as
    
    Deletion_of(x,y) = Encoding_vector(k*y + x) (i.e. flattening the matrix into a vector)
'''


# generating random solutions
def generate_solution() -> np.ndarray:
    return np.random.randint(0, 2, size=matrix_size*matrix_size)


def calculate_the_sums_given_solution(solution_vector : np.ndarray) -> [np.ndarray, np.ndarray]:
    solution_mask = solution_vector.reshape((matrix_size, matrix_size))
    board_without_suggested_deleted_values = board * solution_mask

    solution_column_sums = board_without_suggested_deleted_values.sum(axis=0)
    solution_row_sums = board_without_suggested_deleted_values.sum(axis=1)
    return [solution_row_sums, solution_column_sums]


# defining the fitness functions
def fitness_for_subtask_a(solution_vector : np.ndarray):
    solution_sums = calculate_the_sums_given_solution(solution_vector)

    return int(np.array_equal(solution_sums[0], correct_row_sums)
               and np.array_equal(solution_sums[1], correct_column_sums))


def fitness_for_subtask_b(solution_vector : np.ndarray):
    solution_sums = calculate_the_sums_given_solution(solution_vector)

    row_wise_errors_squared = (correct_row_sums - solution_sums[0]) ** 2
    column_wise_errors_squared = (correct_column_sums - solution_sums[1]) ** 2

    # because we are minimising the error we multiply by -1
    return (np.sum(row_wise_errors_squared) + np.sum(column_wise_errors_squared)) * -1


population_size = 20

population = [generate_solution() for _ in range(population_size)]

for genome in population:
    print(fitness_for_subtask_a(genome), fitness_for_subtask_b(genome))

perfect_genome = deletion_mask.flatten()

print(fitness_for_subtask_a(perfect_genome), fitness_for_subtask_b(perfect_genome))