import math
import numpy as np

''' Setting up the problem '''

problem_dimensions = 5


def evaluate_the_fitness(given_solution):
    given_solution[given_solution > 9] *= -2

    return np.sum(given_solution)


''' Setting up the algorithm '''

residual_velocity = 0.7
personal_best_gravity = 2
global_best_gravity = 2

global_best = [[0, 0, 0, 0, 0], -math.inf]

population_size = 20


# Particle Swarm Optimization


class Particle:
    def __init__(self):
        self.position = np.random.rand(5) * 10
        self.velocity = 0
        self.personal_best = global_best  # correct?

    def get_fitness(self):
        current_fitness = evaluate_the_fitness(self.position)

        if self.personal_best[1] < current_fitness:
            self.personal_best = [self.position, current_fitness]

        return current_fitness

    def __str__(self):
        return 'I am a particle at ' + str(self.position) + \
            '. My current velocity is ' + str(self.velocity) + '!'


# generate random solutions

particles = [Particle for _ in range(population_size)]


def update_global_best():
    for particle in particles:
        global global_best
        current_fitness = particle.get_fitness()
        if current_fitness > global_best[1]:
            global_best = [particle.location, particle.get_fitness()]
