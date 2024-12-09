from Solution.solution import *
import re

class SolutionD3(Solution):
    def get_operations(self):
        ops = []
        for line in self.input:
            ops += list(map(lambda x: (int(x[0]), int(x[1])), re.findall(r'mul\((\d+),(\d+)\)', line)))
        return ops

class SolutionD3C1(SolutionD3):
    def solve(self):
        operations = self.get_operations()
        total = 0
        for op in operations:
            total += op[0] * op[1]
        return total

class SolutionD3C2(SolutionD3):
    def get_operations(self):
        valid_sections = []
        for line in self.input:
            valid_sections.append(re.sub(r'don\'t().*do()', 'do()', line))

        print(f"valid sections: {valid_sections}")
        
        ops = []
        for line in valid_sections:
            ops += list(map(lambda x: (int(x[0]), int(x[1])), re.findall(r'mul\((\d+),(\d+)\)', line)))

        return ops