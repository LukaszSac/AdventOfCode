from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DayFiveTaskTwoSolver(Solver):

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

    def __get_missing_seat_id(self):
        seats = {}
        for seat_id in range(129 * 8):
            seats[seat_id] = {'is_boarded': False}
        for seat_code in self._data:
            seat_id = self.__get_seat_id(seat_code)
            seats[seat_id]['is_boarded'] = True
        for seat_id in range(128 * 8):
            if seats.get(seat_id - 1) is None or seats.get(seat_id + 1) is None:
                continue
            is_before_seat_boarded = seats.get(seat_id - 1)['is_boarded']
            is_this_seat_boarded = seats.get(seat_id)['is_boarded']
            is_next_seat_boarded = seats.get(seat_id + 1)['is_boarded']
            if is_before_seat_boarded is True and is_this_seat_boarded is False and is_next_seat_boarded is True:
                return seat_id

    def get_solution(self):
        if self._data is None:
            raise DataNotLoadedException
        return self.__get_missing_seat_id()