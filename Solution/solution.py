class Solution:
    """
    A generic base class for Advent of Code solutions.
    
    This class provides a load_input method to read input files
    and an abstract solve method that subclasses should implement.
    """

    @staticmethod
    def load_input(input_file_location):
        """
        Load input from a file at the given location.
        
        Args:
            input_file_location (str): Path to the input file
        
        Returns:
            str: Content of the input file as a string
        
        Raises:
            FileNotFoundError: If the specified file does not exist
        """
        try:
            with open(input_file_location, 'r') as file:
                content = list(map(lambda x: x.strip(), file.readlines()))
            return content
        except FileNotFoundError:
            print(f"Error: File '{input_file_location}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
    def solve(self):
        """
        Abstract method to be implemented by subclasses.
        
        This method should contain the logic to solve the Advent of Code problem.
        """
        print("Unimplemented")

    def __init__(self, input_file_location):
        """
        Initialize the Solution with an input file location.
        
        Args:
            input_file_location (str): Path to the input file
        
        Note:
            The input content will be loaded automatically after initialization.
        """
        self.input = self.load_input(input_file_location)