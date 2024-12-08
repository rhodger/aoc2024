import unittest
from unittest.mock import patch, mock_open
from Day1.day1 import *

TEST_INPUT_1 = """3   4
4   3
2   5
1   3
3   9
3   3"""

TEST_INPUT_2 = TEST_INPUT_1

class TestSolutionD1C1(unittest.TestCase):
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
        self.d = SolutionD1C1('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], ['3', '4'])
    
    def test_SolutionD1C1_get_formatted_input(self):
        """
        Test the get_formatted_input method of SolutionD1C1.
        
        This test checks if the input is correctly formatted and sorted.
        
        Expected result:
            - The first element of both lists should be 1 and 3 respectively
        """
        formatted_input = self.d.get_formatted_input()
        self.assertEqual([formatted_input[0][0], formatted_input[1][0]], [1, 3])

    def test_SolutionD1C1_solve(self):
        """
        Test the solve method of SolutionD1C1.
        
        This test calculates the total distance between two lists of numbers.
        
        Expected result:
            - The solution should return 11
        """
        solution = self.d.solve()
        self.assertEqual(solution, 11)

class TestSolutionD1C2(unittest.TestCase):
    """
    Test cases for SolutionD1C2 (Day 1 Challenge 2).
    
    This class contains test methods for the SolutionD1C2 class,
    including setup and individual test cases.
    """

    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT_2)
    def setUp(self, mock_open):
        """
        Set up the test environment by creating an instance of SolutionD1C2.
        
        Args:
            mock_open: Mock object for the open function
        
        Returns:
            None
        """
        self.d = SolutionD1C2('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], ['3', '4'])
    
    def test_SolutionD1C2_get_formatted_input(self):
        """
        Test the get_formatted_input method of SolutionD1C2.
        
        This test checks if the input is correctly formatted and sorted.
        
        Expected result:
            - The first element of both lists should be 1 and 3 respectively
        """
        formatted_input = self.d.get_formatted_input()
        self.assertEqual([formatted_input[0][0], formatted_input[1][0]], [1, 3])
    
    def test_SolutionD1C2_solve(self):
        """
        Test the solve method of SolutionD1C2.
        
        This test calculates the total similarity between two lists of numbers.
        
        Expected result:
            - The solution should return 31
        """
        solution = self.d.solve()
        self.assertEqual(solution, 31)
