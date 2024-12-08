import unittest
from unittest.mock import patch, mock_open
from Day1.day1 import *

TEST_INPUT = """3   4
4   3
2   5
1   3
3   9
3   3"""

class TestSolution(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT)
    def setUp(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = TEST_INPUT
        self.d = SolutionD1C1('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], ['3', '4'])
    
    def test_SolutionD1C1_get_formatted_input(self):
        formatted_input = self.d.get_formatted_input()
        self.assertEqual([formatted_input[0][0], formatted_input[1][0]], [1, 3])

    def test_SolutionD1C1_solve(self):
        solution = self.d.solve()
        self.assertEqual(solution, 11)