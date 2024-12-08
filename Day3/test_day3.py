import unittest
from unittest.mock import patch, mock_open
from Day3.day3 import *

TEST_INPUT_1 = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
TEST_INPUT_2 = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

class TestSolutionD3(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT_1)
    def setUp(self, mock_open):
        self.d = SolutionD3('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], TEST_INPUT_1)

    def test_get_operations(self):
        operations = self.d.get_operations()
        
        self.assertEqual(operations, [(2, 4), (5, 5), (11, 8), (8, 5)])

class TestSolutionD3C1(TestSolutionD3):
    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT_1)
    def setUp(self, mock_open):
        self.d = SolutionD3C1('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], TEST_INPUT_1)

    def test_solve(self):
        solution = self.d.solve()
        self.assertEqual(solution, 161)

class TestSolutionD3C2(TestSolutionD3):
    @patch('builtins.open', new_callable=mock_open, read_data=TEST_INPUT_2)
    def setUp(self, mock_open):
        self.d = SolutionD3C2('')
        mock_open.assert_called_once()
        self.assertEqual(self.d.input[0], TEST_INPUT_2)
    
    def test_get_operations(self):
        operations = self.d.get_operations()
        
        self.assertEqual(operations, [(2, 4), (8, 5)])
    
    def test_solve(self):
        solution = self.d.solve()
        self.assertEqual(solution, 48)