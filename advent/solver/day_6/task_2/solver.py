from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DaySixTaskTwoSolver(Solver):
    @staticmethod
    def _get_parsed_input_data(input_file_dir):
        with open(input_file_dir, 'r') as input_file:
            input_string_lines = input_file.read()[:-1].split('\n\n')
        return input_string_lines

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = self.__get_processed_input(parsed_input_data)

    @staticmethod
    def __get_processed_input(parsed_input_data):
        def map_into_list_of_answers(answer_group):
            answers = list()
            for person_answers in answer_group.split('\n'):
                answers.append(person_answers)
            return answers
        formatted_passport_data = list(map(map_into_list_of_answers, parsed_input_data))
        return formatted_passport_data

    @staticmethod
    def __get_distinct_number_of_yes_answered_questions_by_all(answer_group):
        yes_answered_questions_by_all = set()
        for yes_answered_question in answer_group[0]:
            yes_answered_questions_by_all.add(yes_answered_question)
        for person_answers in answer_group:
            new_yes_answered_questions_by_all = set()
            for previously_existing_question in yes_answered_questions_by_all:
                if previously_existing_question in person_answers:
                    new_yes_answered_questions_by_all.add(previously_existing_question)
            yes_answered_questions_by_all = new_yes_answered_questions_by_all
        return len(yes_answered_questions_by_all)

    def __get_sum_of_number_of_yes_answered_questions_by_all_in_each_group(self):
        sum_of_number_of_yes_answered_questions_by_all_in_each_group = 0
        for answer_group in self._data:
            sum_of_number_of_yes_answered_questions_by_all_in_each_group += self.__get_distinct_number_of_yes_answered_questions_by_all(answer_group)
        return sum_of_number_of_yes_answered_questions_by_all_in_each_group

    def get_solution(self):
        if self._data is None:
            raise DataNotLoadedException
        return self.__get_sum_of_number_of_yes_answered_questions_by_all_in_each_group()
