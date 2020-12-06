from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DayFourTaskTwoSolver(Solver):
    from enum import Enum
    import re

    class __field_types(Enum):
        MANDATORY = 1
        OPTIONAL = 2

    def __init__(self):
        self.__allowed_keys = {'byr': {'field_type': self.__field_types.MANDATORY}, 'iyr': {'field_type': self.__field_types.MANDATORY}, 'eyr': {'field_type': self.__field_types.MANDATORY}, 'hgt': {'field_type': self.__field_types.MANDATORY},
                               'hcl': {'field_type': self.__field_types.MANDATORY}, 'ecl': {'field_type': self.__field_types.MANDATORY}, 'pid': {'field_type': self.__field_types.MANDATORY}, 'cid': {'field_type': self.__field_types.OPTIONAL}}
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
        if not (1920 <= int(passport['byr']) <= 2002):
            return False
        if not (2010 <= int(passport['iyr']) <= 2020):
            return False
        if not (2020 <= int(passport['eyr']) <= 2030):
            return False
        if passport['hgt'][-2:] not in ['cm', 'in']:
            return False
        if passport['hgt'][-2:] == 'cm':
            if not (150 <= int(passport['hgt'][:-2]) <= 193):
                return False
        elif not (59 <= int(passport['hgt'][:-2]) <= 76):
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