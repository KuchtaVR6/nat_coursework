from problemClass import ProblemWithMutationScheme
import random

# class GeneticProgrammingProblem(ProblemWithMutationScheme):
#
#     def __init__(self):

def sum(x, y): return x + y


def difference(x, y): return x - y


def multiplication(x, y): return x * y


possible_functions = ['add', 'dif', 'mul']
possible_constants = ['1', '2', '3', '4', '5']
max_input_length = 3

name_to_function_map = {
    'add': sum,
    'dif': difference,
    'mul': multiplication
}


class MathematicalFunctionTreeNode:
    def __init__(self, stored, left=None, right=None):
        self.stored = stored
        self.left = left
        self.right = right

    def __str__(self):
        final = self.stored
        left_output = ""
        right_output = ""

        if self.left:
            left_output = str(self.left)
            left_array = left_output.split("\n")
            left_output = ""
            for line in left_array:
                left_output += "\n" + "     " + line
        if self.right:
            right_output = str(self.right)
            right_array = right_output.split("\n")
            right_output = ""
            for line in right_array:
                right_output += "\n" + "     " + line

        return final + left_output + right_output

    def calculate(self, inputs):
        if 'input-' in self.stored:
            return inputs[int(self.stored[6:])]
        elif 'constant-' in self.stored:
            return float(self.stored[9:])
        elif 'function-' in self.stored:
            function_label = self.stored[9:]
            function = name_to_function_map[function_label]
            return function(self.left.calculate(inputs), self.right.calculate(inputs))

    def grow_randomly(self, wanted_depth):
        if wanted_depth == 1:
            if random.random() < 0.5:
                self.stored = 'constant-'+possible_constants[random.randint(0, len(possible_constants) - 1)]
            else:
                self.stored = 'input-'+str(random.randint(0, max_input_length - 1))
        elif wanted_depth > 1:
            self.stored = 'function-'+possible_functions[random.randint(0, len(possible_functions) - 1)]

            new_left = MathematicalFunctionTreeNode('input-0')
            new_right = MathematicalFunctionTreeNode('input-0')

            new_left.grow_randomly(wanted_depth-1)
            new_right.grow_randomly(wanted_depth-1)

            self.left = new_left
            self.right = new_right
