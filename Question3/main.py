from geneticProgrammingProblem import GeneticProgrammingProblem
from geneticAlgorithmForGP import GeneticAlgorithmForGP


def sum(x, y): return x + y


def difference(x, y): return x - y


def multiplication(x, y): return x * y


possible_function = [sum, difference, multiplication]
possible_functions_labels = ['add', 'dif', 'mul']
possible_constants = [1, 2, 3, 4, 5]
max_input_length = 4


def generate_data(number_of_data, window_size, sequence_name='fibonacci'):
    sequence = []

    if sequence_name == 'fibonacci':
        sequence = [1, 1]

        while len(sequence) < number_of_data + window_size:
            sequence.append(sequence[-1] + sequence[-2])

    elif sequence_name == 'sylvester':
        # the values are large enough to cause overflow issues
        sequence = [2]

        while len(sequence) < number_of_data + window_size:
            sequence.append(sequence[-1]**2 - sequence[-1] + 1)

    elif sequence_name == 'pell':
        sequence = [0, 1]

        while len(sequence) < number_of_data + window_size:
            sequence.append(2 * sequence[-1] + sequence[-2])

    elif sequence_name == 'perrin':
        sequence = [3, 0, 2]

        while len(sequence) < number_of_data + window_size:
            sequence.append(sequence[-2] + sequence[-3])

    data = []

    for index in range(window_size, len(sequence)):
        data.append([sequence[index-window_size:index], sequence[index]])

    return data


problem = GeneticProgrammingProblem(
    possible_function,
    possible_functions_labels,
    possible_constants,
    3,
    generate_data(20, max_input_length, sequence_name='perrin'),
    max_input_length)


algorithm = GeneticAlgorithmForGP(problem, 60, 0.2, 0.3)

print(algorithm.best_solution_ever[0], "\n", algorithm.best_solution_ever[1], "\n")

algorithm.compute_n_generations(300)

print(algorithm.best_solution_ever[0], "\n", algorithm.best_solution_ever[1], "\n")









