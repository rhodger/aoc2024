import unittest
from unittest.mock import patch, mock_open
from Day4.day4 import *

TEST_INPUT_1 = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

class TestSolutionD4(unittest.TestCase):
    # Check initialisation works
    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT_1)
    def setUp(self, mock_open):
        self.d = SolutionD4('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], "MMMSXXMASM")

    # Check formatting of input works
    def test_get_formatted_input(self):
        f = self.d.get_formatted_input()
        
        self.assertEqual(f[0], ['M','M','M','S','X','X','M','A','S','M'])
        self.assertEqual(f[-1], ['M','X','M','X','A','X','M','A','S','X'])

class TestSolutionD4C1(TestSolutionD4):
    # Check initialisation works
    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT_1)
    def setUp(self, mock_open):
        self.d = SolutionD4C1('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], "MMMSXXMASM")

    # Test solution works on example
    def test_solve(self):
        solution = self.d.solve()
        self.assertEqual(solution, 18)

class TestSolutionD4C2(TestSolutionD4):
    # Check initialisation works
    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT_1)
    def setUp(self, mock_open):
        self.d = SolutionD4C2('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], "MMMSXXMASM")

    # Test solution works on example
    def test_solve(self):
        solution = self.d.solve()
        self.assertEqual(solution, 9)