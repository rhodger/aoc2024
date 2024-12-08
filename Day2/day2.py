import re

from Solution.solution import Solution

class SolutionD2(Solution):
    """
    A subclass of Solution used for solving Day 2 problems.
    
    Attributes:
        input_file_location (string): The input file path.
    """

    def get_formatted_input(self):
        """
        Formats the input data by converting each line into a list of integers.
        
        Returns:
            list: A list of lists containing formatted integer values.
        """
        formatted_input = []
        for line in self.input:
            formatted_input.append(list(map(lambda x: int(x), re.findall(r'\d+', line))))
        return formatted_input
    
    @staticmethod
    def is_pair_safe(ascending, x, y):
        """
        Checks if a pair of numbers is safe based on ascending order.
        
        Args:
            ascending (bool): Whether the numbers should be in ascending order.
            x (int): The first number.
            y (int): The second number.
        
        Returns:
            bool: True if the pair is safe, False otherwise.
        """
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
    """
    A subclass of Solution used for solving Day 2 Challenge 1 problems.
    
    Attributes:
        input_file_location (string): The input file path.
    """

    @staticmethod
    def is_safe(report):
        """
        Checks if a report is safe based on the is_pair_safe method.
        
        Args:
            report (list): A list of numbers representing the report.
        
        Returns:
            bool: True if the report is safe, False otherwise.
        """
        ascending = report[1] > report[0]
        failures = 0
        for i in range(1, len(report)):
            if not SolutionD2.is_pair_safe(ascending, report[i-1], report[i]):
                failures += 1
        
        print(f"failures: {failures}")
        return failures < 1
    
    def solve(self):
        """
        Solves the problem by counting the number of safe reports.
        
        Returns:
            int: The count of safe reports.
        """
        formatted_input = self.get_formatted_input()

        safe_reports = 0
        for report in formatted_input:
            safe_reports += 1 if self.is_safe(report) else 0
        
        return safe_reports

class SolutionD2C2(SolutionD2):
    """
    A subclass of Solution used for solving Day 2 Challenge 2 problems.
    
    Attributes:
        input_file_location (string): The input file path.
    """

    @staticmethod
    def is_report_safe(report):
        """
        Checks if a report is safe based on the is_pair_safe method.
        
        Args:
            report (list): A list of numbers representing the report.
        
        Returns:
            bool: True if the report is safe, False otherwise.
        """
        ascending = report[1] > report[0]
        failures = 0
        for i in range(1, len(report)):
            if not SolutionD2.is_pair_safe(ascending, report[i-1], report[i]):
                failures += 1
        
        print(f"failures: {failures}")
        return failures < 1
    
    @staticmethod
    def is_report_handlable(report):
        """
        Checks if a report can be handled by removing one element.
        
        Args:
            report (list): A list of numbers representing the report.
        
        Returns:
            bool: True if the report can be handled, False otherwise.
        """
        successes = 0
        successes += 1 if SolutionD2C2.is_report_safe(report) else 0
        for i in range(len(report)):
            trimmed_report = report[:i] + report[i+1:]
            successes += 1 if SolutionD2C2.is_report_safe(trimmed_report) else 0
        
        return successes > 0

    def solve(self):
        """
        Solves the problem by counting the number of handlable reports.
        
        Returns:
            int: The count of handlable reports.
        """
        formatted_input = self.get_formatted_input()
        safe = 0
        for report in formatted_input:
            safe += 1 if self.is_report_handlable(report) else 0
        return safe
