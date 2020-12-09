from advent.solver.day_1.task_1 import DayOneTaskOneSolver
from advent.solver.day_1.task_2 import DayOneTaskTwoSolver
from advent.solver.day_2.task_1 import DayTwoTaskOneSolver
from advent.solver.day_2.task_2 import DayTwoTaskTwoSolver
from advent.solver.day_3.task_1 import DayThreeTaskOneSolver
from advent.solver.day_3.task_2 import DayThreeTaskTwoSolver
from advent.solver.day_4.task_1 import DayFourTaskOneSolver
from advent.solver.day_4.task_2 import DayFourTaskTwoSolver
from advent.solver.day_5.task_1 import DayFiveTaskOneSolver
from advent.solver.day_5.task_2 import DayFiveTaskTwoSolver
from advent.solver.day_6.task_1 import DaySixTaskOneSolver
from advent.solver.day_6.task_2 import DaySixTaskTwoSolver
from advent.solver.day_7.task_1 import DaySevenTaskOneSolver
from advent.solver.day_7.task_2 import DaySevenTaskTwoSolver
from advent.solver.day_8.task_1 import DayEightTaskOneSolver
from advent.solver.day_8.task_2 import DayEightTaskTwoSolver
from advent.solver.day_9.task_1 import DayNineTaskOneSolver
from advent.solver.day_9.task_2 import DayNineTaskTwoSolver

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

    @staticmethod
    def get_day_3_task_1_solution():
        input_file_dir = './resources/inputs/day3input.txt'
        solver = DayThreeTaskOneSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} encountered trees'

    @staticmethod
    def get_day_3_task_2_solution():
        input_file_dir = './resources/inputs/day3input.txt'
        solver = DayThreeTaskTwoSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} multiplicity of encountered trees with given walking strategies'

    @staticmethod
    def get_day_4_task_1_solution():
        input_file_dir = './resources/inputs/day4input.txt'
        solver = DayFourTaskOneSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} passports are valid'

    @staticmethod
    def get_day_4_task_2_solution():
        input_file_dir = './resources/inputs/day4input.txt'
        solver = DayFourTaskTwoSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} passports are valid'

    @staticmethod
    def get_day_5_task_1_solution():
        input_file_dir = './resources/inputs/day5input.txt'
        solver = DayFiveTaskOneSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} is the highest seat id'

    @staticmethod
    def get_day_5_task_2_solution():
        input_file_dir = './resources/inputs/day5input.txt'
        solver = DayFiveTaskTwoSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} is the missing seat id'

    @staticmethod
    def get_day_6_task_1_solution():
        input_file_dir = './resources/inputs/day6input.txt'
        solver = DaySixTaskOneSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} is the sum of distinctly yes answered questions in each group'

    @staticmethod
    def get_day_6_task_2_solution():
        input_file_dir = './resources/inputs/day6input.txt'
        solver = DaySixTaskTwoSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} is the sum of yes answered questions by all in each group'

    @staticmethod
    def get_day_7_task_1_solution():
        input_file_dir = './resources/inputs/day7input.txt'
        solver = DaySevenTaskOneSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} is the number of bag regulations eventually containing shiny gold bag'

    @staticmethod
    def get_day_7_task_2_solution():
        input_file_dir = './resources/inputs/day7input.txt'
        solver = DaySevenTaskTwoSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} is the number of required bags inside shiny bags'

    @staticmethod
    def get_day_8_task_1_solution():
        input_file_dir = './resources/inputs/day8input.txt'
        solver = DayEightTaskOneSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} is the accumulator value when program begins to loop'

    @staticmethod
    def get_day_8_task_2_solution():
        input_file_dir = './resources/inputs/day8input.txt'
        solver = DayEightTaskTwoSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} is the accumulator value when program terminates after getting fixed'

    @staticmethod
    def get_day_9_task_1_solution():
        input_file_dir = './resources/inputs/day9input.txt'
        solver = DayNineTaskOneSolver()
        solver.load_and_process_data(input_file_dir)
        solution = solver.get_solution()
        return f'{solution} is the number which is not summing up to 2 of previous 25 numbers'

    @staticmethod
    def get_day_9_task_2_solution():
        input_file_dir = './resources/inputs/day9input.txt'
        solver = DayNineTaskTwoSolver()
        desired_number = 375054920
        solver.load_and_process_data_with_argument(input_file_dir, desired_number)
        solution = solver.get_solution()
        return f'{solution} is the number which is not summing of lowest and biggest number of subset that adds to {desired_number}'


