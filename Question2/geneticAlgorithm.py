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

        probabilities = individual_fitness / np.sum(individual_fitness)

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
        if start == end:
            end = np.random.randint(start+1, genome_length, 1)[0]

        print('start and end', start, end)
        child_solution = np.zeros(genome_length)

        for index in range(genome_length):
            if start <= index <= end:
                child_solution[index] = genome1[index]
            else:
                child_solution[index] = genome2[index]

        return child_solution

    def mutate_solutions(self):
        # todo
        pass

    def compute_generation(self):
        #print(self.current_population)
        self.select_and_replenish_population()
        self.mutate_solutions()
        self.generations_computed += 1
        #print(self.current_population)

    def best_solution_currently(self):
        self.sort_population_by_fitness()
        return self.current_population[0], self.problem.evaluate_fitness(self.current_population[0])




