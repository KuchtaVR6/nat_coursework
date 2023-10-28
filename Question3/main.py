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
            sequence.append(sequence[-1] ** 2 - sequence[-1] + 1)

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
        data.append([sequence[index - window_size:index], sequence[index]])

    return data


max_solution_depth = 5

problem_fibonacci = GeneticProgrammingProblem(
    possible_function,
    possible_functions_labels,
    possible_constants,
    max_solution_depth,
    generate_data(20, max_input_length, sequence_name='fibonacci'),
    max_input_length)

problem_pell = GeneticProgrammingProblem(
    possible_function,
    possible_functions_labels,
    possible_constants,
    max_solution_depth,
    generate_data(20, max_input_length, sequence_name='pell'),
    max_input_length)

problem_perrin = GeneticProgrammingProblem(
    possible_function,
    possible_functions_labels,
    possible_constants,
    max_solution_depth,
    generate_data(20, max_input_length, sequence_name='perrin'),
    max_input_length)

problem_sylvester = GeneticProgrammingProblem(
    possible_function,
    possible_functions_labels,
    possible_constants,
    max_solution_depth,
    generate_data(6, max_input_length, sequence_name='sylvester'),
    max_input_length)

problem_function = GeneticProgrammingProblem(
    possible_function,
    possible_functions_labels,
    possible_constants,
    max_solution_depth,
    generate_data(40, max_input_length, sequence_name='function'),
    max_input_length)

problem_label = ['fib', 'per', 'syl', 'fun']
problems = [problem_fibonacci, problem_perrin, problem_sylvester]

for index in range(len(problems)):
    print("==================")
    print(problem_label[index])
    trials_failed = 0
    convergence_in = 0

    for trail in range(100):
        algorithm = GeneticAlgorithmForGP(problems[index], 11, 0.3, 0.7)

        output = algorithm.compute_until_fit()

        if output == -1:
            trials_failed += 1
        else:
            print("-----------")
            print(problem_label[index])
            print(algorithm.best_solution_ever[0])
            print("-----------")
            convergence_in += output

    successes = 100 - trials_failed

    if successes == 0:
        print(f"{0};{successes}")
    else:
        print(
            f"{int(convergence_in / successes)};{successes}")


# print("population;mutation_rate;crossover_rate;average_solution_cost;success_rate")
# for population_size in range(1, 101, 10):
#     for mutation_prob_times_10 in range(1, 10):
#         mutation_prob = mutation_prob_times_10 / 10
#         for crossover_prob_times_10 in range(1, 10):
#             crossover_prob = crossover_prob_times_10 / 10
#
#             convergence_in = 0
#             trials_failed = 0
#
#             for trials in range(0, 100):
#                 algorithm = GeneticAlgorithmForGP(problem_pell, population_size, mutation_prob, crossover_prob)
#
#                 output = algorithm.compute_until_fit()
#
#                 if output == -1:
#                     trials_failed += 1
#                 else:
#                     convergence_in += output
#
#             successes = 100 - trials_failed
#
#             if successes == 0:
#                 print(f"{population_size};{mutation_prob};{crossover_prob};{0};{successes}")
#             else:
#                 print(
#                     f"{population_size};{mutation_prob};{crossover_prob};{int(convergence_in / successes)};{successes}")
