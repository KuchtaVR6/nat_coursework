from geneticProgrammingProblem import MathematicalFunctionTreeNode

left = MathematicalFunctionTreeNode('function-mul', MathematicalFunctionTreeNode('input-0'), MathematicalFunctionTreeNode('constant-2'))
right = MathematicalFunctionTreeNode('function-add', MathematicalFunctionTreeNode('input-1'), MathematicalFunctionTreeNode('input-2'))

final = MathematicalFunctionTreeNode('function-dif', left, right)

print(final.calculate([3,2,1]))

print(final)

random_test = MathematicalFunctionTreeNode('input-0')

random_test.grow_randomly(4)

print(random_test)