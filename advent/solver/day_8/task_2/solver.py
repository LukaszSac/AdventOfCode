from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DayEightTaskTwoSolver(Solver):
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

    def __run_program_line(self, acc, cursor):
        program = self._data
        command, arg = program[cursor]
        new_cursor, new_acc = self.__known_commands[command](arg, cursor, acc)
        return new_cursor, new_acc

    def __does_program_begin_to_loop(self, cursor, acc, known_cursor_values):
        program = self._data
        while cursor not in known_cursor_values:
            known_cursor_values.add(cursor)
            cursor, acc = self.__run_program_line(acc, cursor)
            if cursor == len(program):
                return False, acc
        return True, acc

    def __get_acc_after_program_terminates(self):
        cursor = 0
        acc = 0
        known_cursor_values = set()
        program = self._data
        while True:
            if cursor == len(program):
                break
            command, arg = program[cursor]
            if command == 'acc':
                known_cursor_values.add(cursor)
                cursor, acc = self.__run_program_line(acc, cursor)
            else:
                if command == 'jmp':
                    new_cursor, _ = self.__known_commands['nop'](arg, cursor, acc)
                else:
                    new_cursor, _ = self.__known_commands['jmp'](arg, cursor, acc)
                has_looped, new_acc = self.__does_program_begin_to_loop(new_cursor, acc, known_cursor_values.copy())
                if has_looped is False:
                    acc = new_acc
                    break
                cursor, acc = self.__run_program_line(acc, cursor)
        return acc

    def get_solution(self):
        if self._data is None:
            raise DataNotLoadedException
        return self.__get_acc_after_program_terminates()
