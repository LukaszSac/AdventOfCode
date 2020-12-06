from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DayFiveTaskOneSolver(Solver):

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = parsed_input_data
        self.__define_config()
        pass

    @staticmethod
    def __get_lower_half(lower_number, higher_number):
        difference = higher_number - lower_number
        difference = int(difference / 2)
        return lower_number, higher_number - difference - 1

    @staticmethod
    def __get_upper_half(lower_number, higher_number):
        difference = higher_number - lower_number
        difference = int(difference / 2)
        return lower_number + difference + 1, higher_number

    def __define_config(self):
        self.__config = {
            'F': self.__get_lower_half,
            'B': self.__get_upper_half,
            'L': self.__get_lower_half,
            'R': self.__get_upper_half
        }
        pass

    def __get_seat_id(self, seat_code):
        row_code = seat_code[:-3]
        column_code = seat_code[-3:]
        lower_number = 0
        higher_number = 127
        for partition in row_code:
            lower_number, higher_number = self.__config[partition](lower_number, higher_number)
        row_number = int(lower_number)
        lower_number = 0
        higher_number = 7
        for partition in column_code:
            lower_number, higher_number = self.__config[partition](lower_number, higher_number)
        column_number = int(lower_number)
        return row_number * 8 + column_number

    def __get_highest_seat_id(self):
        max_seat_id = 0
        for seat_code in self._data:
            seat_id = self.__get_seat_id(seat_code)
            if seat_id > max_seat_id:
                max_seat_id = seat_id
        return max_seat_id

    def get_solution(self):
        if self._data is None:
            raise DataNotLoadedException
        return self.__get_highest_seat_id()