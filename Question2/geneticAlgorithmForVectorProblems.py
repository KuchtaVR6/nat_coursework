import numpy as np

from problemClass import ProblemWithMutationScheme
from genericGeneticAlgorithm import GenericGeneticAlgorithm


class GeneticAlgorithmForVectorProblems(GenericGeneticAlgorithm):

    def crossover_two_genomes(self, genome1, genome2):
        genome_length = len(genome1)
        start, end = np.sort(np.random.randint(0, genome_length, 2))

        child_solution = np.zeros(genome_length)

        for index in range(genome_length):
            if start <= index <= end:
                child_solution[index] = genome1[index]
            else:
                child_solution[index] = genome2[index]

        return child_solution

    def best_solution_currently(self):
        self.sort_population_by_fitness()
        best_solution = self.current_population[0]
        return best_solution, self.problem.evaluate_fitness(best_solution)






