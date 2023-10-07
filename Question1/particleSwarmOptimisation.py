import math
import random
from problemClass import Problem
import numpy as np


# This is the Particle Swarm Optimization
class ParticleSwarmOptimization:
    def __init__(
            self,
            problem: Problem,
            inertia: float,
            personal_best_gravity: float,
            global_best_gravity: float,
            population_size: int):
        self.problem = problem
        self.inertia = inertia
        self.personal_best_gravity = personal_best_gravity
        self.global_best_gravity = global_best_gravity
        self.population_size = population_size

        self.iterations_computed = 0
        self.global_best = [[0 for _ in range(problem.number_of_dimensions)], -math.inf]

        # generate particles and give them one character labels
        self.particles = [Particle(self, chr(index + 65)) for index in range(population_size)]

    def __perform_an_iteration(self, verbose):
        # private
        for particle in self.particles:
            current_fitness = particle.get_fitness_and_update_personal_best()
            # using the best_ever scheme update the global best
            if current_fitness > self.global_best[1]:
                # take the copy of the position (to avoid reference issues)
                self.global_best = [list(particle.position), current_fitness]

        if verbose:
            print('>>gen_' + str(self.iterations_computed) + '_best_fit|'
                  + str(self.global_best[1]) + '|at|' + str(self.global_best[0]))

        for particle in self.particles:
            particle.update_velocities()
            particle.change_position()

        self.iterations_computed += 1

    def run_for_n_iterations(self, iterations: int, verbose=False):
        for _ in range(iterations):
            self.__perform_an_iteration(verbose)


class Particle:
    def __init__(self, swarm: ParticleSwarmOptimization, label='label not set'):
        self.swarm = swarm
        self.label = label
        self.position = swarm.problem.generate_random_solution()
        self.velocity = np.zeros(swarm.problem.number_of_dimensions)
        # based on the initialization from the slides
        self.personal_best = swarm.global_best

    def get_fitness_and_update_personal_best(self):
        own_current_fitness = self.swarm.problem.evaluate_fitness(self.position)

        if self.personal_best[1] < own_current_fitness:
            self.personal_best = [self.position, own_current_fitness]

        return own_current_fitness

    def update_velocities(self):
        r_value = random.random()
        self.velocity = (self.velocity * self.swarm.inertia
                         + self.swarm.personal_best_gravity * r_value * (self.personal_best[0] - self.position)
                         + self.swarm.global_best_gravity * r_value * (self.swarm.global_best[0] - self.position))

    def change_position(self):
        self.position += self.velocity
