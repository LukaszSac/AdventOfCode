from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DayNineTaskOneSolver(Solver):
    __history_fetching_size = 25

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = self.__get_processed_input(parsed_input_data)

    @staticmethod
    def __get_processed_input(parsed_input_data):
        data_casted_to_ints = list(map(int, parsed_input_data))
        return data_casted_to_ints

    def __get_number_not_adding_to_2_before_it(self):
        previous_numbers = set()
        masons_numbers = self._data
        tail_to_delete = list()
        i = 0
        for i in range(0,self.__history_fetching_size):
            tail_to_delete.append(masons_numbers[i])
            previous_numbers.add(masons_numbers[i])
        while True:
            i += 1
            number_to_check = masons_numbers[i]
            sum_checked_out = False
            for previous_number in previous_numbers:
                if number_to_check - previous_number in previous_numbers:
                    tail_to_delete.append(number_to_check)
                    number_to_delete = tail_to_delete.pop(0)
                    previous_numbers.remove(number_to_delete)
                    previous_numbers.add(number_to_check)
                    sum_checked_out = True
                    break
            if sum_checked_out is False:
                return number_to_check

    def get_solution(self):
        if self._data is None:
            raise DataNotLoadedException
        return self.__get_number_not_adding_to_2_before_it()
