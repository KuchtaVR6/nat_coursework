import numpy as np

from problemClass import ProblemWithMutationScheme


class GeneticAlgorithm:

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

    def sort_population_by_fitness(self):
        """ Descending fitness """
        self.current_population.sort(key=self.problem.evaluate_fitness, reverse=True)

    def select_and_replenish_population(self, elitism=0):
        self.sort_population_by_fitness()

        current_population_size = len(self.current_population)
        number_of_vacant_spaces = self.population_size - elitism

        individual_fitness = np.zeros(current_population_size)

        for index in range(current_population_size):
            genome = self.current_population[index]
            individual_fitness[index] = self.problem.evaluate_fitness(genome)

        # some problems yield negative fitness, this is bad for probabilities, therefore we normalize
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
                    GeneticAlgorithm.__crossover_two_genomes(mating_pool[index], mating_pool[-index]))
            else:
                self.current_population.append(mating_pool[index])

    def __crossover_two_genomes(genome1, genome2) -> np.ndarray:
        # private static
        genome_length = len(genome1)
        start, end = np.sort(np.random.randint(0, genome_length, 2))

        child_solution = np.zeros(genome_length)

        for index in range(genome_length):
            if start <= index <= end:
                child_solution[index] = genome1[index]
            else:
                child_solution[index] = genome2[index]

        return child_solution

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
        for _ in range(number_of_generations):
            self.compute_generation()
            if verbose:
                print('>>gen_' + str(self.generations_computed) + '_best_fit|'
                      + str(self.best_solution_currently()[1]))






