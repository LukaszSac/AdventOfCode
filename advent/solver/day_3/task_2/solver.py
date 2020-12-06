from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DayThreeTaskTwoSolver(Solver):
    __walking_strategies = list()

    def __init__(self):
        self.__load_walking_strategies()

    def __load_walking_strategies(self):
        def add_traversal(right_step, down_step):
            self.__walking_strategies.append({'right_step': right_step, 'down_step': down_step, 'encountered_trees': 0})
        add_traversal(1, 1)
        add_traversal(3, 1)
        add_traversal(5, 1)
        add_traversal(7, 1)
        add_traversal(1, 2)

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = parsed_input_data

    @staticmethod
    def _get_parsed_input_data(input_file_dir):
        with open(input_file_dir, 'r') as input_file:
            input_string_lines = input_file.read()[1:-1].split('\n')
        return input_string_lines

    def __get_how_many_tree_collisions(self, walking_strategy):
        tree_layout = self._data
        x_pos = walking_strategy['right_step']
        tree_collision_counter = 0
        y_pos = walking_strategy['down_step']
        while y_pos < len(tree_layout):
            if tree_layout[y_pos][x_pos % 31] == '#':
                tree_collision_counter += 1
            x_pos += walking_strategy['right_step']
            y_pos += walking_strategy['down_step']
        return tree_collision_counter

    def __get_multiplicity_of_walking_strategies(self):
        for walking_strategy in self.__walking_strategies:
            walking_strategy['encountered_trees'] = self.__get_how_many_tree_collisions(walking_strategy)
        multiplicity_of_encountered_trees = 1
        for walking_strategy in self.__walking_strategies:
            multiplicity_of_encountered_trees *= walking_strategy['encountered_trees']
        return multiplicity_of_encountered_trees

    def get_solution(self):
        if self._data is None:
            raise DataNotLoadedException
        return self.__get_multiplicity_of_walking_strategies()
