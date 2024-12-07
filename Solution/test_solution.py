import unittest
from unittest.mock import patch
from solution import *

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @patch('builtins.open')
    def test_load_input_success(self, mock_open):
        # Set up the mock to return 'Test content' when called with 'test.txt'
        mock_open.return_value.__enter__.return_value.read.return_value = "Test content"
        
        result = self.solution.load_input("test.txt")
        
        # Verify that the correct method was called
        mock_open.assert_called_once_with("test.txt", 'r')
        
        # Check if the returned value matches what we expected
        self.assertEqual(result, "Test content")

    @patch('builtins.open')
    def test_load_input_failure(self, mock_open):
        mock_open.side_effect = FileNotFoundError
        
        result = self.solution.load_input("non_existent_file.txt")
        
        self.assertIsNone(result)
        mock_open.assert_called_once_with("non_existent_file.txt", 'r')

    @patch('builtins.open')
    def test_load_input_exception(self, mock_open):
        mock_open.side_effect = Exception("An error occurred")
        
        result = self.solution.load_input("error_file.txt")
        
        self.assertIsNone(result)
        mock_open.assert_called_once_with("error_file.txt", 'r')

if __name__ == '__main__':
    unittest.main()
