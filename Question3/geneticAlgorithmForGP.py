from genericGeneticAlgorithm import GenericGeneticAlgorithm


class GeneticAlgorithmForGP(GenericGeneticAlgorithm):
    def crossover_two_genomes(self, genome1, genome2):
        new_genome = genome1.make_copy()
        new_genome.crossover(genome2, )
        return new_genome
