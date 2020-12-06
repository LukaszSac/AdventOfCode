from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DayTwoTaskOneSolver(Solver):
    import re

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = self.__get_processed_input(parsed_input_data)

    def __parse_row_of_data(self, line_of_data):
        return self.re.match(r'(\d+)-(\d+)\s(\w):\s(.*)', line_of_data).groups()

    def __get_processed_input(self, parsed_input_data):
        list_of_data = list(map(self.__parse_row_of_data, parsed_input_data))

        def cast_values_in_tuple(tp):
            least, most, req, pw = tp
            return int(least), int(most), req, pw

        return list(map(cast_values_in_tuple, list_of_data))

    @staticmethod
    def __is_password_correct(least_amount_of_characters, most_amount_of_characters, character_required, password):
        occurrences = 0
        for character in password:
            if character == character_required:
                occurrences += 1
        if int(least_amount_of_characters) <= occurrences <= most_amount_of_characters:
            return True
        else:
            return False

    def __get_how_many_passwords_are_correct(self):
        if self._data is None:
            raise DataNotLoadedException
        how_many_passwords_are_correct = 0
        for least_amount_of_characters, most_amount_of_characters, character_required, password in self._data:
            if self.__is_password_correct(least_amount_of_characters, most_amount_of_characters, character_required, password):
                how_many_passwords_are_correct += 1
        return how_many_passwords_are_correct

    def get_solution(self):
        return self.__get_how_many_passwords_are_correct()