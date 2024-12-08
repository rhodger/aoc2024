import unittest
from unittest.mock import patch, mock_open
from Solution.solution import *

class TestSolution(unittest.TestCase):
    """
    Test cases for the base Solution class.
    
    This class contains test methods for the Solution class,
    including setup and individual test cases.
    """

    @patch('builtins.open', new_callable=mock_open, read_data='Test content')
    def setUp(self, _):
        """
        Set up the test environment by creating an instance of Solution.
        
        Args:
            _: Unused parameter from unittest.mock.patch
        
        Returns:
            None
        """
        self.solution = Solution('')

    @patch('builtins.open', new_callable=mock_open, read_data='Test content')
    def test_load_input_success(self, mock_open):
        """
        Test successful loading of input file.
        
        This test checks if the load_input method correctly reads
        content from a file when provided with a valid path.
        
        Expected result:
            - The method should return the expected content
            - The open function should be called once with the correct arguments
        """
        # Set up the mock to return 'Test content' when called with 'test.txt'
        mock_open.return_value.__enter__.return_value.read.return_value = "Test content"
        
        result = self.solution.load_input("test.txt")
        
        # Verify that the correct method was called
        mock_open.assert_called_once_with("test.txt", 'r')
        
        # Check if the returned value matches what we expected
        self.assertEqual(result, ["Test content"])

    @patch('builtins.open')
    def test_load_input_failure(self, mock_open):
        """
        Test handling of file not found error.
        
        This test checks if the load_input method correctly handles
        a FileNotFoundError when trying to open a non-existent file.
        
        Expected result:
            - The method should return None
            - The open function should be called once with the correct arguments
        """
        mock_open.side_effect = FileNotFoundError
        
        result = self.solution.load_input("non_existent_file.txt")
        
        self.assertIsNone(result)
        mock_open.assert_called_once_with("non_existent_file.txt", 'r')

    @patch('builtins.open')
    def test_load_input_exception(self, mock_open):
        """
        Test handling of other exceptions during file loading.
        
        This test checks if the load_input method correctly handles
        any other type of exception that might occur during file reading.
        
        Expected result:
            - The method should return None
            - The open function should be called once with the correct arguments
        """
        mock_open.side_effect = Exception("An error occurred")
        
        result = self.solution.load_input("error_file.txt")
        
        self.assertIsNone(result)
        mock_open.assert_called_once_with("error_file.txt", 'r')

if __name__ == '__main__':
    unittest.main()
