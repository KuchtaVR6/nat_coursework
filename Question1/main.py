from particleSwarmOptimisation import ParticleSwarmOptimization
from problemDefinition import NDimensionalRastriginProblem

problem = NDimensionalRastriginProblem(2, (-5.12, 5.12))
model = ParticleSwarmOptimization(problem, 0.7, 2, 2, 25)

model.run_for_n_iterations(50, verbose=True)

print(model.global_best)
