import unittest
from unittest.mock import patch, mock_open
from Day2.day2 import *

TEST_INPUT_1 = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

TEST_INPUT_2 = TEST_INPUT_1

class TestSolutionD2(unittest.TestCase):
    """
    Test cases for SolutionD1C1 (Day 1 Challenge 1).
    
    This class contains test methods for the SolutionD1C1 class,
    including setup and individual test cases.
    """

    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT_1)
    def setUp(self, mock_open):
        """
        Set up the test environment by creating an instance of SolutionD1C1.
        
        Args:
            mock_open: Mock object for the open function
        
        Returns:
            None
        """
        self.d = SolutionD2C1('')
        print(f"pre-format: {self.d.input}")
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], '7 6 4 2 1')
    
    def test_get_formatted_input(self):
        formatted_input = self.d.get_formatted_input()
        self.assertEqual(formatted_input[0], ['7', '6', '4', '2', '1'])