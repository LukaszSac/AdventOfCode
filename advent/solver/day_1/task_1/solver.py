from advent.solver.exception import DataNotLoadedException, SolutionNotFoundException
from advent.solver import Solver


class DayOneTaskOneSolver(Solver):
    def __init__(self, desired_sum):
        self.__desired_sum = desired_sum

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        processed_input_data = self.__get_processed_input(parsed_input_data)
        self._data = processed_input_data

    @staticmethod
    def __get_processed_input(input_data):
        return sorted(list(map(int, input_data)))

    def __get_numbers_summing_to_desired_sum(self):
        if self._data is None:
            raise DataNotLoadedException
        left_index = 0
        right_index = len(self._data) - 1
        sum_of_numbers = self._data[left_index] + self._data[right_index]
        while sum_of_numbers != self.__desired_sum:
            if sum_of_numbers > self.__desired_sum:
                right_index -= 1
            else:
                left_index += 1
            sum_of_numbers = self._data[left_index] + self._data[right_index]
            if sum_of_numbers == self.__desired_sum:
                return self._data[left_index], self._data[right_index]
        raise SolutionNotFoundException

    def get_solution(self):
        first_number, second_number = self.__get_numbers_summing_to_desired_sum()
        return first_number * second_number