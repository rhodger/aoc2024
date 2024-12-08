import unittest
from unittest.mock import patch, mock_open
from Day2.day2 import *

TEST_INPUT_1 = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

class TestSolutionD2(unittest.TestCase):
    """
    Test cases for SolutionD2 class.
    """

    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT_1)
    def setUp(self, mock_open):
        """
        Set up the test environment by initializing SolutionD2 instance.
        
        Args:
            mock_open (mock_open): Mocked open function.
        """
        self.d = SolutionD2('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], '7 6 4 2 1')
    
    def test_get_formatted_input(self):
        """
        Test the get_formatted_input method.
        
        Asserts:
            - Correct formatting of the input.
        """
        formatted_input = self.d.get_formatted_input()
        self.assertEqual(formatted_input[0], [7, 6, 4, 2, 1])

class TestSolutionD2C1(TestSolutionD2):
    """
    Test cases for SolutionD2C1 class.
    """

    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT_1)
    def setUp(self, mock_open):
        """
        Set up the test environment by initializing SolutionD2C1 instance.
        
        Args:
            mock_open (mock_open): Mocked open function.
        """
        self.d = SolutionD2C1('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], '7 6 4 2 1')

    def test_is_pair_safe(self):
        """
        Test the is_pair_safe static method.
        
        Asserts:
            - Correct handling of ascending order.
            - Correct handling of invalid polarity.
            - Correct handling of invalid difference.
        """
        valid = self.d.is_pair_safe(False, 7, 6)
        invalid_polarity = self.d.is_pair_safe(False, 7, 8)
        invalid_diff = self.d.is_pair_safe(False, 7, 3)

        self.assertTrue(valid)
        self.assertFalse(invalid_polarity)
        self.assertFalse(invalid_diff)

    def test_solve(self):
        """
        Test the solve method.
        
        Asserts:
            - Correct count of safe reports.
        """
        solution = self.d.solve()
        self.assertEqual(solution, 2)

class TestSolutionD2C2(TestSolutionD2):
    """
    Test cases for SolutionD2C2 class.
    """

    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT_1)
    def setUp(self, mock_open):
        """
        Set up the test environment by initializing SolutionD2C2 instance.
        
        Args:
            mock_open (mock_open): Mocked open function.
        """
        self.d = SolutionD2C2('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], '7 6 4 2 1')

    def test_is_report_safe(self):
        """
        Test the is_report_safe static method.
        
        Asserts:
            - Correct handling of valid reports.
            - Correct handling of invalid polarity.
            - Correct handling of invalid difference.
        """
        valid = self.d.is_report_safe([7, 6, 4, 3, 1])
        invalid_polarity = self.d.is_report_safe([7, 6, 4, 5, 6])
        invalid_diff = self.d.is_report_safe([15, 10, 4, 2, 1])

        self.assertTrue(valid)
        self.assertFalse(invalid_polarity)
        self.assertFalse(invalid_diff)

    def test_is_report_handlable(self):
        """
        Test the is_report_handlable static method.
        
        Asserts:
            - Correct handling of handlable reports.
        """
        handlable_no_removes = [7, 6, 4, 2, 1]
        handlable_one_remove = [1, 3, 2, 4, 5]
        unhandlable = [1, 2, 7, 8, 9]

        self.assertTrue(self.d.is_report_handlable(handlable_no_removes))
        self.assertTrue(self.d.is_report_handlable(handlable_one_remove))
        self.assertFalse(self.d.is_report_handlable(unhandlable))

    def test_solve(self):
        """
        Test the solve method.
        
        Asserts:
            - Correct count of handlable reports.
        """
        solution = self.d.solve()
        self.assertEqual(solution, 4)
