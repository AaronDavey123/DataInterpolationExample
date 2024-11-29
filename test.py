from fill_data import calcMissing

import unittest
from unittest.mock import patch
from io import StringIO

class TestCalcMissing(unittest.TestCase):
    
    def test_single_missing_value(self):
        test_case_1 = [
            "2023-01-01 12:00\t25.5",
            "2023-01-02 12:00\tMissing_1",
            "2023-01-03 12:00\t26.0",
            "2023-01-04 12:00\t27.5"
        ]
        
        expected_output = "Missing_1: 25.750000\n"  # Expected output for the missing value
        
        # Capture the printed output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calcMissing(test_case_1)
        
        # Get the actual output
        actual_output = mock_stdout.getvalue()
        
        # Print both expected and actual output with test case label
        print("Test Case 1 - Single Missing Value:")
        print("Expected Output:\n", expected_output)
        print("Actual Output:\n", actual_output)
        
        # Check if the output contains the expected value
        self.assertIn(expected_output.strip(), actual_output.strip())
    
    def test_multiple_missing_values(self):
        test_case_2 = [
            "2023-01-01 12:00\t25.0",
            "2023-01-02 12:00\tMissing_1",
            "2023-01-03 12:00\t26.0",
            "2023-01-04 12:00\tMissing_2",
            "2023-01-05 12:00\t28.0"
        ]
        
        expected_output = "Missing_1: 25.500000\nMissing_2: 27.000000\n"  # Expected output for multiple missing values
        
        # Capture the printed output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calcMissing(test_case_2)
        
        # Get the actual output
        actual_output = mock_stdout.getvalue()
        
        # Print both expected and actual output with test case label
        print("Test Case 2 - Multiple Missing Values:")
        print("Expected Output:\n", expected_output)
        print("Actual Output:\n", actual_output)
        
        # Check if the output contains the expected values
        self.assertIn(expected_output.strip(), actual_output.strip())
    
    def test_all_values_missing(self):
        test_case_3 = [
            "2023-01-01 12:00\tMissing_1",
            "2023-01-02 12:00\tMissing_2",
            "2023-01-03 12:00\tMissing_3",
            "2023-01-04 12:00\t26.5"
        ]
        
        expected_output = "Missing_1: 26.500000\nMissing_2: 26.500000\nMissing_3: 26.500000\n"  # Expected output when all values are missing
        
        # Capture the printed output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calcMissing(test_case_3)
        
        # Get the actual output
        actual_output = mock_stdout.getvalue()
        
        # Print both expected and actual output with test case label
        print("Test Case 3 - All Values Missing:")
        print("Expected Output:\n", expected_output)
        print("Actual Output:\n", actual_output)
        
        # Check if the output contains the expected values
        self.assertIn(expected_output.strip(), actual_output.strip())

if __name__ == "__main__":
    unittest.main()
