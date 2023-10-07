import math
import random

import numpy as np

# This is the Particle Swarm Optimization

''' Setting up the problem '''

problem_dimensions = 2
min_generated_pos = -5.12
max_generated_pos = 5.12


def variable_rastrign_function(input_vector):
    number_of_dims = len(input_vector)

    overall_sum = 0

    for input_scalar in input_vector:
        overall_sum += input_scalar ** 2 + 10 * math.cos(2 * math.pi * input_scalar)

    return 10 * number_of_dims + overall_sum


def evaluate_the_fitness(given_solution, check_if_within_min_max=False):
    copy_of_given_solution = np.copy(given_solution)

    penalties = 0

    if check_if_within_min_max:
        # apply a penalty for values over max
        penalties += copy_of_given_solution[copy_of_given_solution > max_generated_pos] ** 2
        # apply a penalty for values below min
        penalties += copy_of_given_solution[copy_of_given_solution < min_generated_pos] ** 2

    # we are trying to minimise penalties and the function therefore fitness will be * -1
    return (variable_rastrign_function(copy_of_given_solution) + penalties) * -1


''' Setting up the algorithm '''

velocity_inertia = 0.7
personal_best_gravity = 2
global_best_gravity = 2

global_best = [[0 for _ in range(problem_dimensions)], -math.inf]

population_size = 1000


class Particle:
    def __init__(self, label='label not set'):
        self.label = label
        self.position = np.random.rand(problem_dimensions) * (max_generated_pos - min_generated_pos) + min_generated_pos
        self.velocity = np.zeros(problem_dimensions)
        # based on the initialization from the slides
        self.personal_best = global_best

    def get_fitness_and_update_personal_best(self):
        own_current_fitness = evaluate_the_fitness(self.position)

        if self.personal_best[1] < own_current_fitness:
            self.personal_best = [self.position, own_current_fitness]

        return own_current_fitness

    def update_velocities(self):
        r_value = random.random()
        self.velocity = self.velocity * velocity_inertia + \
                        personal_best_gravity * r_value * (self.personal_best[0] - self.position) + \
                        global_best_gravity * r_value * (global_best[0] - self.position)

    def change_position(self):
        self.position += self.velocity

    def __str__(self):
        return 'pos:' + ';'.join(self.position.astype(str).tolist())


# generate particles

particles = [Particle(chr(index + 65)) for index in range(population_size)]


def generational_loop(number_of_generations):
    # todo fix the line below
    global global_best
    for current_generation in range(number_of_generations):
        for particle in particles:
            current_fitness = particle.get_fitness_and_update_personal_best()
            # using the best_ever scheme update the global best
            if current_fitness > global_best[1]:
                # take the copy of the position (to avoid reference issues)
                global_best = [list(particle.position), current_fitness]

        print('>>gen_' + str(current_generation) + '_best_fit|' + str(global_best[1]) + '|at|' + str(global_best[0]))

        for particle in particles:
            particle.update_velocities()
            particle.change_position()

        if global_best[1] > -0.0001:
            return global_best

    return global_best


print('Best solution is:', generational_loop(200))
