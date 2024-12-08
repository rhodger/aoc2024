import re

from Solution.solution import Solution

class SolutionD2(Solution):
    def get_formatted_input(self):
        formatted_input = []
        for line in self.input:
            formatted_input.append(re.findall(r'\d+', line))
        
        print(f"formatted: {formatted_input}")

        return formatted_input

class SolutionD2C1(SolutionD2):
    def solve(self):
        print("unimplemented")