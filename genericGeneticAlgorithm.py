import numpy as np
import sys
sys.path.append("/problemClass.py")
from problemClass import ProblemWithMutationScheme


class GenericGeneticAlgorithm:

    def __init__(
            self,
            problem: ProblemWithMutationScheme,
            population_size: int,
            mutation_probability: float,
            crossover_probability: float
    ):
        self.problem = problem
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.crossover_probability = crossover_probability

        self.generations_computed = 0
        self.current_population = [problem.generate_random_solution() for _ in range(population_size)]
        self.best_solution_ever = [self.current_population[0], problem.evaluate_fitness(self.current_population[0])]
        self.evaluations_performed = 0

    def sort_population_by_fitness(self):
        """ Descending fitness """
        self.current_population.sort(key=self.problem.evaluate_fitness, reverse=True)
        self.evaluations_performed += self.population_size

        current_best = self.current_population[0]
        current_best_fitness = self.problem.evaluate_fitness(self.current_population[0])
        if current_best_fitness > self.best_solution_ever[1]:
            self.best_solution_ever = [current_best, current_best_fitness]

    def select_and_replenish_population(self, elitism=0):
        self.sort_population_by_fitness()

        current_population_size = len(self.current_population)
        number_of_vacant_spaces = self.population_size - elitism

        individual_fitness = np.zeros(current_population_size)

        for index in range(current_population_size):
            genome = self.current_population[index]
            individual_fitness[index] = self.problem.evaluate_fitness(genome)

        # some problems yield negative fitness, this is bad for probabilities, therefore, we normalise
        positive_fitness = individual_fitness - np.min(individual_fitness)

        # in theory at this point all fitness could equal zero, therefore for calculation safety
        if np.all(positive_fitness == 0):
            positive_fitness[:] = 1

        probabilities = positive_fitness / np.sum(positive_fitness)

        mating_pool_indexes = np.random.choice(
            current_population_size, number_of_vacant_spaces, p=probabilities)

        mating_pool = []

        for index in mating_pool_indexes:
            mating_pool.append(self.current_population[index])

        self.current_population = self.current_population[:elitism]

        for index in range(len(mating_pool)):
            random_score = np.random.rand()
            if random_score < self.crossover_probability:
                self.current_population.append(
                    self.crossover_two_genomes(mating_pool[index], mating_pool[-index]))
            else:
                self.current_population.append(mating_pool[index])

    def crossover_two_genomes(self, genome1, genome2):
        raise Exception("This method is abstract")

    def mutate_solutions(self):
        mutation_flags = np.random.rand(self.population_size) < self.mutation_probability
        for index in range(self.population_size):
            if mutation_flags[index]:
                self.current_population[index] = self.problem.mutate_solution(self.current_population[index])

    def compute_generation(self):
        self.select_and_replenish_population()
        self.mutate_solutions()
        self.generations_computed += 1

    def best_solution_currently(self):
        self.sort_population_by_fitness()
        best_solution = self.current_population[0]
        return best_solution, self.problem.evaluate_fitness(best_solution)

    def compute_n_generations(self, number_of_generations: int, verbose=False):
        for generation in range(number_of_generations):
            self.compute_generation()
            if verbose:
                print('>>gen_' + str(self.generations_computed) + '_best_fit|'
                      + str(self.best_solution_currently()[1]))

    def compute_until_fit(self, termination_max=300):
        for generation in range(termination_max):
            self.compute_generation()
            if self.best_solution_ever[1] == 0:
                return self.evaluations_performed
        return -1






