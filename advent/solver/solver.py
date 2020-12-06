from advent.solver.exception import FunctionNotYetImplemented


class Solver:
    _data = None

    def get_solution(self):
        raise FunctionNotYetImplemented

    def load_and_process_data(self, input_file_dir):
        raise FunctionNotYetImplemented

    @staticmethod
    def _get_parsed_input_data(input_file_dir):
        with open(input_file_dir, 'r') as input_file:
            input_string_lines = input_file.read()[:-1].split('\n')
        return input_string_lines


