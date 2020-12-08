from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DaySevenTaskTwoSolver(Solver):
    import re
    __known_bags_contain_number = {}

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = self.__get_processed_input(parsed_input_data)

    def __get_processed_input(self, parsed_input_data):
        bag_regulations = {}
        for bag_regulation in parsed_input_data:
            outer_bag, raw_string_containments = bag_regulation.split(" bags contain ")
            raw_containments = self.re.findall(r'(?:,\s)?(\d*?\s(?:\w+\s\w+))\sbag(?:s)?', raw_string_containments)
            if len(raw_containments) == 0:
                containments = None
            else:
                containments = {}
                for containment in raw_containments:
                    number, color = containment.split(' ', 1)
                    containments.update({color: int(number)})
            bag_regulations.update({outer_bag: containments})
        return bag_regulations

    def __how_many_bags_inside(self, color_of_bag):
        if self._data[color_of_bag] is None:
            return 0
        if color_of_bag in self.__known_bags_contain_number.keys():
            return self.__known_bags_contain_number
        bags_inside = 0
        for bag_color, bag_number in self._data[color_of_bag].items():
            if bag_color in self.__known_bags_contain_number.keys():
                how_many_bags_inside = self.__known_bags_contain_number[bag_color]
            else:
                how_many_bags_inside = self.__how_many_bags_inside(bag_color)
                self.__known_bags_contain_number.update({bag_color: how_many_bags_inside})
            bags_inside += how_many_bags_inside*bag_number + bag_number
        return bags_inside

    def __get_how_many_individual_bags_in_shiny_golden_bag(self):
        return self.__how_many_bags_inside('shiny gold')

    def get_solution(self):
        if self._data is None:
            raise DataNotLoadedException
        self.__known_bags_contain_number.clear()
        return self.__get_how_many_individual_bags_in_shiny_golden_bag()
