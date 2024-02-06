"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:
    def test_addition(self):
        assert 5 == calculator.add(3, 2)

    def test_subtraction(self):
        assert 5 == calculator.subtract(10, 5)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)
    