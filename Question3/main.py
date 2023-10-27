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
    generate_data(20, max_input_length, sequence_name='pell'),
    max_input_length)

print("population;mutation_rate;crossover_rate;average_solution_cost;success_rate")

for population_size in range(1, 101, 10):
    for mutation_prob_times_10 in range(1, 10):
        mutation_prob = mutation_prob_times_10 / 10
        for crossover_prob_times_10 in range(1, 10):
            crossover_prob = crossover_prob_times_10 / 10

            convergence_in = 0
            trials_failed = 0

            for trials in range(0, 100):
                algorithm = GeneticAlgorithmForGP(problem, population_size, mutation_prob, crossover_prob)

                output = algorithm.compute_until_fit()

                if output == -1:
                    trials_failed += 1
                else:
                    convergence_in += output

            successes = 100-trials_failed

            if successes == 0:
                print(f"{population_size};{mutation_prob};{crossover_prob};{0};{successes}")
            else:
                print(
                    f"{population_size};{mutation_prob};{crossover_prob};{int(convergence_in / successes)};{successes}")








