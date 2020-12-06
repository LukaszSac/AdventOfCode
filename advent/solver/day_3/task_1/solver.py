from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DayThreeTaskOneSolver(Solver):
    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = parsed_input_data

    def __get_how_many_tree_collisions(self):
        tree_layout = self._data
        x_pos = 3
        tree_collision_counter = 0
        y_pos = 1
        while y_pos < len(tree_layout):
            if tree_layout[y_pos][x_pos % 31] == '#':
                tree_collision_counter += 1
            x_pos += 3
            y_pos += 1
        return tree_collision_counter

    def get_solution(self):
        if self._data is None:
            raise DataNotLoadedException
        return self.__get_how_many_tree_collisions()