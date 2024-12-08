import unittest
from unittest.mock import patch, mock_open
from Day2.day2 import *

TEST_INPUT_1 = """3   4
4   3
2   5
1   3
3   9
3   3"""

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
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], ['3', '4'])
    
    def test_format_input(self):
        formatted_input = self.d.get_formatted_input()
        self.assert_equal(formatted_input[0], [7, 6, 4, 2, 1])
    
    def test_solve(self):
        solution = self.d.solve()
        self.assert_equal(solution, 2)