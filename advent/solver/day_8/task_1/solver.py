from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DayEightTaskOneSolver(Solver):
    __known_commands = {}

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = self.__get_processed_input(parsed_input_data)
        self.__define_commands()

    @staticmethod
    def __get_processed_input(parsed_input_data):
        program = list()
        for raw_line in parsed_input_data:
            command, arg = raw_line.split(" ", 1)
            arg = int(arg)
            program.append((command, arg))
        return program

    def __define_commands(self):
        def nop(arg, cursor, acc):
            return cursor + 1, acc

        def acc(arg, cursor, acc):
            return cursor + 1, acc + arg

        def jmp(arg, cursor, acc):
            return cursor + arg, acc

        self.__known_commands = {'nop': nop, 'acc': acc, 'jmp': jmp}

    def __get_acc_when_program_begins_to_loop(self):
        acc = 0
        cursor = 0
        known_cursor_values = set()
        program = self._data
        while cursor not in known_cursor_values:
            known_cursor_values.add(cursor)
            command, arg = program[cursor]
            cursor, acc = self.__known_commands[command](arg, cursor, acc)
        return acc

    def get_solution(self):
        if self._data is None:
            raise DataNotLoadedException
        return self.__get_acc_when_program_begins_to_loop()
