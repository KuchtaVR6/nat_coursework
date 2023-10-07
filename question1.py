import math
import random

import numpy as np

# This is the Particle Swarm Optimization

''' Setting up the problem '''

problem_dimensions = 2
min_generated_pos = 0
max_generated_pos = 3


def evaluate_the_fitness(given_solution):
    copy_of_given_solution = np.copy(given_solution)

    # entries above 9, assign a penalty to them
    copy_of_given_solution[copy_of_given_solution > 9] *= -2

    return np.sum(copy_of_given_solution)


''' Setting up the algorithm '''

velocity_inertia = 0.7
personal_best_gravity = 3
global_best_gravity = 1

global_best = [[0, 0, 0, 0, 0], -math.inf]

population_size = 20


class Particle:
    def __init__(self, label='label not set'):
        self.label = label
        self.position = np.random.rand(problem_dimensions) * (max_generated_pos - min_generated_pos) + min_generated_pos
        self.velocity = np.zeros(problem_dimensions)
        # making a copy of global_best
        self.personal_best = [[0, 0, 0, 0, 0], -math.inf]

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
        return self.label+';'+';'.join(self.position.astype(str).tolist())


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

        print('>>gen_'+str(current_generation)+'_best_fit|'+str(global_best[1])+'|at|'+str(global_best[0]))

        for particle in particles:
            particle.update_velocities()
            particle.change_position()

    return global_best


print('Best solution is:', generational_loop(20))
