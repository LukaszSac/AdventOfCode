from advent.solver.exception import DataNotLoadedException
from advent.solver import Solver


class DaySevenTaskOneSolver(Solver):
    import re
    __known_bags_to_contain_gold = set()

    def load_and_process_data(self, input_file_dir):
        parsed_input_data = self._get_parsed_input_data(input_file_dir)
        self._data = self.__get_processed_input(parsed_input_data)

    def __get_processed_input(self, parsed_input_data):
        bag_regulations = {}
        for bag_regulation in parsed_input_data:
            outer_bag, raw_containments = bag_regulation.split(" bags contain ")
            containments = self.re.findall(r'(?:,\s)?(?:\d*?\s)((?:\w+\s\w+))\sbag(?:s)?', raw_containments)
            if len(containments) == 0:
                containments = None
            bag_regulations.update({outer_bag: containments})
        return bag_regulations

    def __is_shiny_bag_in_this_bag(self, color_of_bag):
        if self._data[color_of_bag] is None:
            return False
        if "shiny gold" in self._data[color_of_bag]:
            self.__known_bags_to_contain_gold.add(color_of_bag)
            return True
        for bag_color in self._data[color_of_bag]:
            if bag_color in self.__known_bags_to_contain_gold:
                self.__known_bags_to_contain_gold.add(color_of_bag)
                return True
            is_shiny_in_there = self.__is_shiny_bag_in_this_bag(bag_color)
            if is_shiny_in_there is True:
                self.__known_bags_to_contain_gold.add(color_of_bag)
                return True
            else:
                continue
        return False

    def __get_how_many_bags_can_evetually_contain_shiny_gold(self):
        for color_of_bag_regulation in self._data.keys():
            self.__is_shiny_bag_in_this_bag(color_of_bag_regulation)
        return len(self.__known_bags_to_contain_gold)

    def get_solution(self):
        if self._data is None:
            raise DataNotLoadedException
        self.__known_bags_to_contain_gold.clear()
        return self.__get_how_many_bags_can_evetually_contain_shiny_gold()
