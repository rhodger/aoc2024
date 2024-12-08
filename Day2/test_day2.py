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
    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT_1)
    def setUp(self, mock_open):
        self.d = SolutionD2('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], '7 6 4 2 1')
    
    def test_get_formatted_input(self):
        formatted_input = self.d.get_formatted_input()
        self.assertEqual(formatted_input[0], [7, 6, 4, 2, 1])

class TestSolutionD2C1(TestSolutionD2):
    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT_1)
    def setUp(self, mock_open):
        self.d = SolutionD2C1('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], '7 6 4 2 1')

    def test_is_pair_safe(self):
        valid = self.d.is_pair_safe(False, 7, 6)
        invalid_polarity = self.d.is_pair_safe(False, 7, 8)
        invalid_diff = self.d.is_pair_safe(False, 7, 3)

        self.assertTrue(valid)
        self.assertFalse(invalid_polarity)
        self.assertFalse(invalid_diff)

    def test_solve(self):
        solution = self.d.solve()
        self.assertEqual(solution, 2)

class TestSolutionD2C2(TestSolutionD2):
    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT_1)
    def setUp(self, mock_open):
        self.d = SolutionD2C2('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], '7 6 4 2 1')

    def test_is_safe(self):
        valid = self.d.is_safe([7, 6, 4, 2, 1])
        invalid_polarity = self.d.is_safe([7, 6, 4, 2, 3])
        invalid_diff = self.d.is_safe([10, 6, 4, 2, 1])

        self.assertTrue(valid)
        self.assertFalse(invalid_polarity)
        self.assertFalse(invalid_diff)

    def test_solve(self):
        solution = self.d.solve()
        self.assertEqual(solution, 4)