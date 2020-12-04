from advent.resolver import DayOneTaskOneSolver, DayOneTaskTwoSolver, DayTwoTaskOneSolver, DayTwoTaskTwoSolver


class AdventOfCode2020Solver:
    def __init__(self):
        pass

    @staticmethod
    def get_day_1_task_1_solution():
        input_file_dir = './resources/inputs/day1input.txt'
        desired_sum = 2020
        solver = DayOneTaskOneSolver(desired_sum)
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'Numbers multiplicity of 2 numbers summing to desired number {desired_sum} is {solution}'

    @staticmethod
    def get_day_1_task_2_solution():
        input_file_dir = './resources/inputs/day1input.txt'
        desired_sum = 2020
        solver = DayOneTaskTwoSolver(desired_sum)
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'Numbers multiplicity of 3 numbers summing to desired number {desired_sum} is {solution}'

    @staticmethod
    def get_day_2_task_1_solution():
        input_file_dir = './resources/inputs/day2input.txt'
        solver = DayTwoTaskOneSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} passwords are correct'

    @staticmethod
    def get_day_2_task_2_solution():
        input_file_dir = './resources/inputs/day2input.txt'
        solver = DayTwoTaskTwoSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} passwords are correct'


