import re

from Solution.solution import Solution

class SolutionD2(Solution):
    def get_formatted_input(self):
        formatted_input = []
        for line in self.input:
            formatted_input.append(list(map(lambda x: int(x), re.findall(r'\d+', line))))

        return formatted_input
    
    @staticmethod
    def is_pair_safe(ascending, x, y):
        if ascending:
            if y <= x:
                return False
        else:
            if y >= x:
                return False
        
        diff = abs(y - x)
        if diff < 1 or diff > 3:
            return False
        
        return True

class SolutionD2C1(SolutionD2):
    @staticmethod
    def is_safe(report):
        ascending = report[1] > report[0]
        failures = 0
        for i in range(1, len(report)):
            if not SolutionD2.is_pair_safe(ascending, report[i-1], report[i]):
                failures += 1
        
        print(f"failures: {failures}")
        return failures < 1
    
    def solve(self):
        formatted_input = self.get_formatted_input()

        safe_reports = 0
        for report in formatted_input:
            safe_reports += 1 if self.is_safe(report) else 0
        
        return safe_reports