from problemClass import ProblemWithMutationScheme
import random


class GeneticProgrammingProblem(ProblemWithMutationScheme):

    def __init__(
            self,
            possible_functions,
            function_labels,
            possible_constants,
            max_solution_depth,
            training_data,
            input_vector_length=1
    ):
        super().__init__(0)

        self.possible_functions = possible_functions
        self.possible_constants = possible_constants
        self.input_vector_length = input_vector_length
        self.max_solution_depth = max_solution_depth
        self.training_data = training_data

        self.name_to_function_map = dict(zip(function_labels, possible_functions))

    def generate_random_solution(self):
        new_solution = MathematicalFunctionTreeNode(self, 'input-0')
        new_solution.grow_randomly(self.max_solution_depth)
        return new_solution

    def evaluate_fitness(self, solution) -> float:

        sum_of_squared_errors = 0

        for input, target in self.training_data:
            output = solution.calculate(input)

            sum_of_squared_errors += (target - output) ** 2

        return -1 * sum_of_squared_errors

    def mutate_solution(self, solution):
        new_solution = solution.make_copy()

        new_solution.mutate(0.3)

        return new_solution

class MathematicalFunctionTreeNode:
    def __init__(self, problem: GeneticProgrammingProblem, stored, left=None, right=None):
        self.stored = stored
        self.left = left
        self.right = right

        self.problem = problem

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
            function = self.problem.name_to_function_map[function_label]
            return function(self.left.calculate(inputs), self.right.calculate(inputs))

    def grow_randomly(self, wanted_depth):
        if wanted_depth == 1:
            if random.random() < 0.5:
                self.stored = 'constant-' + str(
                    self.problem.possible_constants[
                        random.randint(0, len(self.problem.possible_constants) - 1)
                    ])
            else:
                self.stored = 'input-' + str(random.randint(0, self.problem.input_vector_length - 1))
        elif wanted_depth > 1:
            self.stored = 'function-' + self.problem.possible_functions[
                random.randint(0, len(self.problem.possible_functions) - 1)]

            new_left = MathematicalFunctionTreeNode(self.problem, 'input-0')
            new_right = MathematicalFunctionTreeNode(self.problem, 'input-0')

            new_left.grow_randomly(wanted_depth - 1)
            new_right.grow_randomly(wanted_depth - 1)

            self.left = new_left
            self.right = new_right

    def get_depth(self):
        left_depth = 0
        right_depth = 0

        if self.left:
            left_depth = self.left.get_depth()
        if self.right:
            right_depth = self.right.get_depth()

        return 1 + max(left_depth, right_depth)

    def get_volume(self):
        left_volume = 0
        right_volume = 0

        if self.left:
            left_volume = self.left.get_volume()
        if self.right:
            right_volume = self.right.get_volume()

        return 1 + left_volume + right_volume

    def mutate(self, mutation_prob):

        dice_roll = random.random()

        if dice_roll < mutation_prob:
            self.grow_randomly(2)
        else:
            if self.left:
                self.left.mutate(mutation_prob)
            if self.right:
                self.right.mutate(mutation_prob)

    def make_copy(self):
        copy = MathematicalFunctionTreeNode(self.problem, self.stored)
        if self.left:
            copy.left = self.left.make_copy()
        if self.right:
            copy.right = self.right.make_copy()
        return copy

    def cut_and_return_copy(self, index):
        if index == 0:
            return self.make_copy()
        else:
            index -= 1
            if self.left:
                left_volume = self.left.get_volume()
                if index < left_volume:
                    return self.left.cut_and_return_copy(index)
                else:
                    index -= left_volume
            if self.right:
                right_volume = self.right.get_volume()
                if index < right_volume:
                    return self.right.cut_and_return_copy(index)
            raise IndexError

    # does not work for replacing the root
    def insert_tree(self, index, inserted_tree):
        if index == 0:
            raise IndexError
        elif index == 1:
            self.left = inserted_tree
            return
        else:
            index -= 1
            if self.left:
                left_volume = self.left.get_volume()
                if index < left_volume:
                    return self.left.insert_tree(index, inserted_tree)
                else:
                    index -= left_volume
            if index == 0:
                self.right = inserted_tree
                return
            elif self.right:
                right_volume = self.right.get_volume()
                if index < right_volume:
                    return self.right.insert_tree(index, inserted_tree)
            raise IndexError

    def crossover(self, other, crossover_prob):
        dice_roll = random.random()
        if dice_roll < crossover_prob:
            self_cut_index = random.randint(1, self.get_volume())
            other_cut_index = random.randint(1, other.get_volume())

            inserted_tree = other.cut_and_return_copy(other_cut_index)
            self.insert_tree(self_cut_index, inserted_tree)
