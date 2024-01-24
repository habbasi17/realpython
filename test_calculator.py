"""
Unit tests for the calculatro librarary
"""

import calculator


class TestCalculator:
    def test_addition(self):
        assert 5 == calculator.add(3, 2)

    def test_subtraction(self):
        assert 5 == calculator.subtract(10, 5)
