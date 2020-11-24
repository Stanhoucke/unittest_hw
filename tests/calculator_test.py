# Import unittest module
import unittest
# Import functions to test from calculator.py
from src.calculator import add, divide, multiply, subtract

# Define test class
# Convention of "Test" + name of the file being tested
class TestCalculator(unittest.TestCase):

    # Convention of "test_" + name of method being tested
    def test_add(self):
        # assertEqual takes arguments of (expected_result, actual_result)
        self.assertEqual(5, add(2, 3))

    # Code test for subtract
    def test_subtract(self):
        self.assertEqual(3, subtract(10, 7))

    # Code tests for multiply and divide
    def test_multiply(self):
        self.assertEqual(36, multiply(3, 12))

    def test_divide(self):
        self.assertEqual(5, divide(50, 10))

