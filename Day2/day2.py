import re

from Solution.solution import Solution

class SolutionD2(Solution):
    def get_formatted_input(self):
        formatted_input = []
        for line in self.input:
            formatted_input.append(list(map(lambda x: int(x), re.findall(r'\d+', line))))

        return formatted_input

class SolutionD2C1(SolutionD2):
    @staticmethod
    def is_safe(report):
        ascending = report[1] > report[0]
        for i in range(1, len(report)):
            if ascending:
                if report[i] <= report[i-1]:
                    return False
            else:
                if report[i] >= report[i-1]:
                    return False
            
            diff = abs(report[i] - report[i-1])
            if diff < 1 or diff > 3:
                return False
            
        return True

    def solve(self):
        formatted_input = self.get_formatted_input()

        safe_reports = 0
        for report in formatted_input:
            safe_reports += 1 if self.is_safe(report) else 0
        
        return safe_reports