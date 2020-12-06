from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DaySixTaskOneSolver(Solver):
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
    def __get_distinct_number_of_yes_answered_questions(answer_group):
        yes_answered_questions = {}
        for person_answers in answer_group:
            for yes_answered_question in person_answers:
                yes_answered_questions.update({yes_answered_question: 1})
        return sum(yes_answered_questions.values())

    def __get_sum_of_distinct_number_of_yes_answered_questions_in_each_group(self):
        sum_of_distinct_number_of_yes_answered_questions = 0
        for answer_group in self._data:
            sum_of_distinct_number_of_yes_answered_questions += self.__get_distinct_number_of_yes_answered_questions(answer_group)
        return sum_of_distinct_number_of_yes_answered_questions

    def get_solution(self):
        if self._data is None:
            raise DataNotLoadedException
        return self.__get_sum_of_distinct_number_of_yes_answered_questions_in_each_group()
