from genericGeneticAlgorithm import GenericGeneticAlgorithm

class GeneticAlgorithmForGP(GenericGeneticAlgorithm):
    def crossover_two_genomes(self, genome1, genome2):
        raise Exception("This method is abstract")
