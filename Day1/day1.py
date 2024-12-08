import re

from Solution.solution import Solution

class SolutionD1(Solution):
    """
    Solution for Day 1 of Advent of Code.
    
    This class overrides the load_input method to handle the specific input format
    for Day 1 problems.
    """

    @staticmethod
    def load_input(input_file_location):
        """
        Load input from a file at the given location.
        
        Args:
            input_file_location (str): Path to the input file
        
        Returns:
            list: List of pairs of numbers, each pair on a separate line
        
        Raises:
            FileNotFoundError: If the specified file does not exist
        """
        try:
            with open(input_file_location, 'r') as file:
                content = file.readlines()
            formatted_content = []
            for line in content:
                nums = re.findall(r'\d+', line)
                if len(nums) != 2:
                    print(f"Invalid line in input: {line}")
                    return None
                else:
                    formatted_content.append(nums)
            return formatted_content
        except FileNotFoundError:
            print(f"Error: File '{input_file_location}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
    def get_formatted_input(self):
        """
        Format the loaded input by converting strings to integers and sorting.
        
        Returns:
            tuple: Two sorted lists of integers
        """
        sorted_input = [[], []]
        for pair in self.input:
            sorted_input[0].append(int(pair[0]))
            sorted_input[1].append(int(pair[1]))
        sorted_input[0].sort()
        sorted_input[1].sort()
        return sorted_input

class SolutionD1C1(SolutionD1):
    """
    Solution for Day 1 Challenge 1 of Advent of Code.
    
    This class overrides the solve method to calculate the total distance.
    """

    def solve(self):
        """
        Calculate the total distance between the two lists of numbers.
        
        Returns:
            int: Total distance between the two lists
        """
        sorted_input = self.get_formatted_input()

        total_distance = 0
        shortest_list = sorted_input[0] if sorted_input[0] < sorted_input[1] else sorted_input[1]
        for pair_index in range(len(shortest_list)):
            pair = [sorted_input[0][pair_index], sorted_input[1][pair_index]]
            total_distance += abs(pair[0] - pair[1])
        
        return total_distance

class SolutionD1C2(SolutionD1):
    """
    Solution for Day 1 Challenge 2 of Advent of Code.
    
    This class overrides the solve method to calculate the total similarity.
    """

    def solve(self):
        """
        Calculate the total similarity between the two lists of numbers.
        
        Returns:
            int: Total similarity between the two lists
        """
        formatted_input = self.get_formatted_input()

        total_similarity = 0
        for val in formatted_input[0]:
            total_similarity += val * formatted_input[1].count(val)
        
        return total_similarity
