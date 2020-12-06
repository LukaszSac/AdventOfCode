from advent.solver.exception import DataNotLoadedException, SolutionNotFoundException
from advent.solver import Solver


class DayOneTaskTwoSolver(Solver):
    def __init__(self, desired_sum):
        self.__desired_sum = desired_sum

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        processed_input_data = self.__get_processed_input(parsed_input_data)
        self._data = processed_input_data

    @staticmethod
    def __get_processed_input(input_data):
        return sorted(list(map(int, input_data)))

    def __get_two_numbers_summing_to_desired_sum(self, desired_sum, left_index, right_index):
        if self._data is None:
            raise DataNotLoadedException
        sum_of_numbers = self._data[left_index] + self._data[right_index]
        while left_index < right_index:
            if self._data[left_index] + self._data[right_index] < desired_sum:
                left_index += 1
            elif self._data[left_index] + self._data[right_index] > desired_sum:
                right_index -= 1
            else:
                return self._data[left_index], self._data[right_index]
        raise SolutionNotFoundException

    def __get_three_numbers_summing_to_desired_sum(self):
        right_index = 2
        while self._data[right_index] < self.__desired_sum:
            desired_sum_complement = self.__desired_sum - self._data[right_index]
            try:
                first_number, second_number = self.__get_two_numbers_summing_to_desired_sum(desired_sum_complement, 0, right_index - 1)
                return first_number, second_number, self._data[right_index]
            except SolutionNotFoundException:
                right_index += 1
        raise SolutionNotFoundException

    def get_solution(self):
        first_number, second_number, third_number = self.__get_three_numbers_summing_to_desired_sum()
        return first_number * second_number * third_number