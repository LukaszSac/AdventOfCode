from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DayTwoTaskTwoSolver(Solver):
    import re

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = self.__get_processed_input(parsed_input_data)

    def __parse_row_of_data(self, line_of_data):
        return self.re.match(r'(\d+)-(\d+)\s(\w):\s(.*)', line_of_data).groups()

    def __get_processed_input(self, parsed_input_data):
        list_of_data = list(map(self.__parse_row_of_data, parsed_input_data))

        def cast_values_in_tuple(raw_data_tuple):
            first, second, req, pw = raw_data_tuple
            return int(first), int(second), req, pw

        return list(map(cast_values_in_tuple, list_of_data))

    @staticmethod
    def __is_password_correct(data_tuple):
        first_position_of_character, second_position_of_character, character_required, password = data_tuple
        if (password[first_position_of_character - 1] == character_required) != (password[second_position_of_character - 1] == character_required):
            return True
        else:
            return False

    def __get_how_many_passwords_are_correct(self):
        if self._data is None:
            raise DataNotLoadedException
        how_many_passwords_are_correct = 0
        for data_tuple in self._data:
            if self.__is_password_correct(data_tuple):
                how_many_passwords_are_correct += 1
        return how_many_passwords_are_correct

    def get_solution(self):
        return self.__get_how_many_passwords_are_correct()