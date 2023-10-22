from geneticProgrammingProblem import GeneticProgrammingProblem


def sum(x, y): return x + y


def difference(x, y): return x - y


def multiplication(x, y): return x * y


possible_function = [sum, difference, multiplication]
possible_functions_labels = ['add', 'dif', 'mul']
possible_constants = [1, 2, 3, 4, 5]
max_input_length = 3


def generate_data(number_of_data, window_size):

    # fibbonaci
    sequence = [1, 1]

    while len(sequence) < number_of_data + window_size:
        sequence.append(sequence[-1] + sequence[-2])

    data = []

    for index in range(window_size, len(sequence)):
        data.append([sequence[index-window_size:index], sequence[index]])

    return data


problem = GeneticProgrammingProblem(
    possible_function,
    possible_functions_labels,
    possible_constants,
    5,
    generate_data(20, max_input_length),
    max_input_length)










