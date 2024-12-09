from Solution.solution import *

class SolutionD4(Solution):
    def get_formatted_input(self):
        return list(map(lambda x: list(x), self.input))