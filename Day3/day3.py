from Solution.solution import *
import re

class SolutionD3(Solution):
    def get_operations(self):
        ops = []
        for line in self.input:
            ops += list(map(lambda x: (int(x[0]), int(x[1])), re.findall(r'mul\((\d+),(\d+)\)', line)))
        return ops
    
    def solve(self):
        operations = self.get_operations()
        total = 0
        for op in operations:
            total += op[0] * op[1]
        return total

class SolutionD3C1(SolutionD3):
    pass

class SolutionD3C2(SolutionD3):
    # Requires newlines stripping from input
    def get_operations(self):
        valid_sections = []
        for line in self.input:
            pline = line
            old_length = -1
            while len(pline) != old_length:
                print(f"step: {pline}")
                old_length = len(pline)
                pline = re.sub(r'don\'t\(\).*?(do\(\)|$)', 'do()', pline)
            valid_sections.append(pline)

        print(f"valid sections: {valid_sections}")
        
        ops = []
        for line in valid_sections:
            ops += list(map(lambda x: (int(x[0]), int(x[1])), re.findall(r'mul\((\d+),(\d+)\)', line)))

        return ops