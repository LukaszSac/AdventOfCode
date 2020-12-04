from advent.resolver.exception import DataNotLoadedException, SolutionNotFoundException, FunctionNotYetImplemented


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


class DayOneTaskOneSolver(Solver):
    def __init__(self, desired_sum):
        self.__desired_sum = desired_sum

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        processed_input_data = self.__get_processed_input(parsed_input_data)
        self._data = processed_input_data

    @staticmethod
    def __get_processed_input(input_data):
        return sorted(list(map(int, input_data)))

    def __get_numbers_summing_to_desired_sum(self):
        if self._data is None:
            raise DataNotLoadedException
        left_index = 0
        right_index = len(self._data) - 1
        sum_of_numbers = self._data[left_index] + self._data[right_index]
        while sum_of_numbers != self.__desired_sum:
            if sum_of_numbers > self.__desired_sum:
                right_index -= 1
            else:
                left_index += 1
            sum_of_numbers = self._data[left_index] + self._data[right_index]
            if sum_of_numbers == self.__desired_sum:
                return self._data[left_index], self._data[right_index]
        raise SolutionNotFoundException

    def get_solution(self):
        first_number, second_number = self.__get_numbers_summing_to_desired_sum()
        return first_number * second_number


class DayOneTaskTwoSolver(Solver):
    def __init__(self, desired_sum):
        self.__desired_sum = desired_sum

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        processed_input_data = self.__get_processed_input(parsed_input_data)
        self._data = processed_input_data

    @staticmethod
    def __get_processed_input(input_data):
        return sorted(list(map(int, input_data)))

    def __get_two_numbers_summing_to_desired_sum(self, desired_sum, left_index, right_index):
        if self._data is None:
            raise DataNotLoadedException
        sum_of_numbers = self._data[left_index] + self._data[right_index]
        while left_index < right_index:
            if self._data[left_index] + self._data[right_index] < desired_sum:
                left_index += 1
            elif self._data[left_index] + self._data[right_index] > desired_sum:
                right_index -= 1
            else:
                return self._data[left_index], self._data[right_index]
        raise SolutionNotFoundException

    def __get_three_numbers_summing_to_desired_sum(self):
        right_index = 2
        while self._data[right_index] < self.__desired_sum:
            desired_sum_complement = self.__desired_sum - self._data[right_index]
            try:
                first_number, second_number = self.__get_two_numbers_summing_to_desired_sum(desired_sum_complement, 0, right_index-1)
                return first_number, second_number, self._data[right_index]
            except SolutionNotFoundException:
                right_index += 1
        raise SolutionNotFoundException

    def get_solution(self):
        first_number, second_number, third_number = self.__get_three_numbers_summing_to_desired_sum()
        return first_number * second_number * third_number


class DayTwoTaskOneSolver(Solver):
    import re

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = self.__get_processed_input(parsed_input_data)

    def __parse_row_of_data(self, line_of_data):
        return self.re.match(r'(\d+)-(\d+)\s(\w):\s(.*)', line_of_data).groups()

    def __get_processed_input(self, parsed_input_data):
        list_of_data = list(map(self.__parse_row_of_data, parsed_input_data))

        def cast_values_in_tuple(tp):
            least, most, req, pw = tp
            return int(least), int(most), req, pw
        return list(map(cast_values_in_tuple, list_of_data))

    @staticmethod
    def __is_password_correct(least_amount_of_characters, most_amount_of_characters, character_required, password):
        occurrences = 0
        for character in password:
            if character == character_required:
                occurrences += 1
        if int(least_amount_of_characters) <= occurrences <= most_amount_of_characters:
            return True
        else:
            return False

    def __get_how_many_passwords_are_correct(self):
        if self._data is None:
            raise DataNotLoadedException
        how_many_passwords_are_correct = 0
        for least_amount_of_characters, most_amount_of_characters, character_required, password in self._data:
            if self.__is_password_correct(least_amount_of_characters, most_amount_of_characters, character_required, password):
                how_many_passwords_are_correct += 1
        return how_many_passwords_are_correct

    def get_solution(self):
        return self.__get_how_many_passwords_are_correct()


class DayTwoTaskTwoSolver(Solver):
    import re

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = self.__get_processed_input(parsed_input_data)

    def __parse_row_of_data(self, line_of_data):
        return self.re.match(r'(\d+)-(\d+)\s(\w):\s(.*)', line_of_data).groups()

    def __get_processed_input(self, parsed_input_data):
        list_of_data = list(map(self.__parse_row_of_data, parsed_input_data))

        def cast_values_in_tuple(raw_data_tuple):
            first, second, req, pw = raw_data_tuple
            return int(first), int(second), req, pw
        return list(map(cast_values_in_tuple, list_of_data))

    @staticmethod
    def __is_password_correct(data_tuple):
        first_position_of_character, second_position_of_character, character_required, password = data_tuple
        if (password[first_position_of_character - 1] == character_required) != (password[second_position_of_character - 1] == character_required):
            return True
        else:
            return False

    def __get_how_many_passwords_are_correct(self):
        if self._data is None:
            raise DataNotLoadedException
        how_many_passwords_are_correct = 0
        for data_tuple in self._data:
            if self.__is_password_correct(data_tuple):
                how_many_passwords_are_correct += 1
        return how_many_passwords_are_correct

    def get_solution(self):
        return self.__get_how_many_passwords_are_correct()


class DayFourTaskOneSolver(Solver):
    from enum import Enum

    class __field_types(Enum):
        MANDATORY = 1
        OPTIONAL = 2

    def __init__(self):
        self.__allowed_keys = {'byr': {'field_type': self.__field_types.MANDATORY}, 'iyr': {'field_type': self.__field_types.MANDATORY}, 'eyr': {'field_type': self.__field_types.MANDATORY}, 'hgt': {'field_type': self.__field_types.MANDATORY}, 'hcl': {'field_type': self.__field_types.MANDATORY}, 'ecl': {'field_type': self.__field_types.MANDATORY}, 'pid': {'field_type': self.__field_types.MANDATORY}, 'cid': {'field_type': self.__field_types.OPTIONAL}}
        self.__count_of_mandatory_fields = 0
        for value in self.__allowed_keys.values():
            if value['field_type'] == self.__field_types.MANDATORY:
                self.__count_of_mandatory_fields += 1

    @staticmethod
    def _get_parsed_input_data(input_file_dir):
        with open(input_file_dir, 'r') as input_file:
            input_string_lines = input_file.read()[:-1].split('\n\n')
        return input_string_lines

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = self.__get_processed_input(parsed_input_data)

    def __get_count_of_mandatory_fields_in_passport(self, passport):
        count = 0
        for key in passport.keys():
            if self.__allowed_keys[key]['field_type'] == self.__field_types.MANDATORY:
                count += 1
        return count

    def __get_processed_input(self, passport_raw_string_list):
        def map_into_dictionary(formatted_passport_string):
            passport_dict = {}
            for entry in formatted_passport_string.split(' '):
                key, value = entry.split(':')
                if self.__allowed_keys[key]:
                    passport_dict.update({key: value})
            return passport_dict

        def format_passport_data(raw_passport_data):
            return raw_passport_data.replace('\n', ' ')

        formatted_passport_data = list(map(map_into_dictionary, list(map(format_passport_data, passport_raw_string_list))))
        return formatted_passport_data

    def __is_passport_valid(self, passport):
        count_of_mandatory_fields_in_passport = self.__get_count_of_mandatory_fields_in_passport(passport)
        if count_of_mandatory_fields_in_passport == self.__count_of_mandatory_fields:
            return True
        else:
            return False

    def get_solution(self):
        if self._data is None:
            raise DataNotLoadedException
        count_of_valid_passports = 0
        for passport in self._data:
            if self.__is_passport_valid(passport):
                count_of_valid_passports += 1
        return count_of_valid_passports


class DayFourTaskTwoSolver(Solver):
    from enum import Enum
    import re

    class __field_types(Enum):
        MANDATORY = 1
        OPTIONAL = 2

    def __init__(self):
        self.__allowed_keys = {'byr': {'field_type': self.__field_types.MANDATORY}, 'iyr': {'field_type': self.__field_types.MANDATORY}, 'eyr': {'field_type': self.__field_types.MANDATORY}, 'hgt': {'field_type': self.__field_types.MANDATORY}, 'hcl': {'field_type': self.__field_types.MANDATORY}, 'ecl': {'field_type': self.__field_types.MANDATORY}, 'pid': {'field_type': self.__field_types.MANDATORY}, 'cid': {'field_type': self.__field_types.OPTIONAL}}
        self.__count_of_mandatory_fields = 0
        for value in self.__allowed_keys.values():
            if value['field_type'] == self.__field_types.MANDATORY:
                self.__count_of_mandatory_fields += 1

    @staticmethod
    def _get_parsed_input_data(input_file_dir):
        with open(input_file_dir, 'r') as input_file:
            input_string_lines = input_file.read()[:-1].split('\n\n')
        return input_string_lines

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = self.__get_processed_input(parsed_input_data)

    def __get_count_of_mandatory_fields_in_passport(self, passport):
        count = 0
        for key in passport.keys():
            if self.__allowed_keys[key]['field_type'] == self.__field_types.MANDATORY:
                count += 1
        return count

    def __get_processed_input(self, passport_raw_string_list):
        def map_into_dictionary(formatted_passport_string):
            passport_dict = {}
            for entry in formatted_passport_string.split(' '):
                key, value = entry.split(':')
                if self.__allowed_keys[key]:
                    passport_dict.update({key: value})
            return passport_dict

        def format_passport_data(raw_passport_data):
            return raw_passport_data.replace('\n', ' ')

        formatted_passport_data = list(map(map_into_dictionary, list(map(format_passport_data, passport_raw_string_list))))
        return formatted_passport_data

    def __is_passport_valid(self, passport):
        count_of_mandatory_fields_in_passport = self.__get_count_of_mandatory_fields_in_passport(passport)
        if count_of_mandatory_fields_in_passport != self.__count_of_mandatory_fields:
            return False
        if not(1920 <= int(passport['byr']) <= 2002):
            return False
        if not(2010 <= int(passport['iyr']) <= 2020):
            return False
        if not(2020 <= int(passport['eyr']) <= 2030):
            return False
        if passport['hgt'][-2:] not in ['cm', 'in']:
            return False
        if passport['hgt'][-2:] == 'cm':
            if not(150 <= int(passport['hgt'][:-2]) <= 193):
                return False
        elif not(59 <= int(passport['hgt'][:-2]) <= 76):
            return False
        if passport['hcl'][0] != '#':
            return False
        if not self.re.match(r'^[0-9a-f]{6}$', passport['hcl'][1:]):
            return False
        if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        if not self.re.match(r'^\d{9}$', passport['pid']):
            return False
        return True

    def get_solution(self):
        if self._data is None:
            raise DataNotLoadedException
        count_of_valid_passports = 0
        for passport in self._data:
            if self.__is_passport_valid(passport):
                count_of_valid_passports += 1
        return count_of_valid_passports

