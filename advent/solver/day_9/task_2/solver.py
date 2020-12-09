from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DayNineTaskTwoSolver(Solver):
    __sum_to_find = None

    def load_and_process_data_with_argument(self, input_file_dir, sum_to_find):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = self.__get_processed_input(parsed_input_data)
        self.__sum_to_find = sum_to_find

    @staticmethod
    def __get_processed_input(parsed_input_data):
        data_casted_to_ints = list(map(int, parsed_input_data))
        return data_casted_to_ints

    def __get_right_index_of_numbers_adding_up_to_sum(self, left_index):
        sum_of_range = self._data[left_index]
        right_index = left_index
        while sum_of_range < self.__sum_to_find:
            right_index += 1
            sum_of_range += self._data[right_index]
        if sum_of_range == self.__sum_to_find:
            return left_index, right_index
        else:
            return None, None

    def __get_sum_of_lowest_and_largest_number_of_subset_that_sums_up_to_desired_number(self):
        left_index = 0
        while self._data[left_index] != self.__sum_to_find:
            subset_left_index, subset_right_index = self.__get_right_index_of_numbers_adding_up_to_sum(left_index)
            if subset_left_index is not None:
                subset = self._data[subset_left_index: subset_right_index + 1]
                return min(subset) + max(subset)
            else:
                left_index += 1

    def get_solution(self):
        if self._data is None:
            raise DataNotLoadedException
        if self.__sum_to_find is None:
            raise DataNotLoadedException
        return self.__get_sum_of_lowest_and_largest_number_of_subset_that_sums_up_to_desired_number()
