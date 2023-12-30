#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import math

from simple_calculator.main import SimpleCalculator

def test_add_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4,5)

    assert result == 9

def test_add_three_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4,5,3)

    assert result == 12

def test_add_many_numbers():
    numbers = range(100)

    calculator = SimpleCalculator()

    result = calculator.add(*numbers)

    assert result == sum(numbers)

def test_subtract_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.sub(5,3)

    assert result == 2

def test_multiply_numbers():
    numbers = list(range(1,10))

    calculator = SimpleCalculator()

    result = calculator.mul(*numbers)

    assert result == math.prod(numbers)

def test_div_two_numbers_float():
    calculator = SimpleCalculator()

    result = calculator.div(13, 2)

    assert result == 6.5

def test_div_by_zero():
    calculator = SimpleCalculator()

    result = calculator.div(13, 0)

    assert result == float('inf')

def test_mul_zero_raises_value_exception():
    calculator = SimpleCalculator()

    with pytest.raises(ValueError):
        calculator.mul(3, 0)

def test_average():
    calculator = SimpleCalculator()

    numbers = [2, 3, 7, 15]
    answer = 6.75

    result = calculator.average(*numbers)

    assert result == answer

def test_average_with_upper_thresh():
    calculator = SimpleCalculator()

    numbers = [2, 3, 7, 15]
    answer = 2.5

    result = calculator.average(*numbers, ut=5)

    assert result == answer


def test_average_with_lower():
    calculator = SimpleCalculator()

    numbers = [2, 3, 7, 15]
    answer = 15

    result = calculator.average(*numbers, lt=7)

    assert result == answer

def test_average_with_and_upper():
    calculator = SimpleCalculator()

    numbers = [2, 3, 7, 15]
    answer = 5

    result = calculator.average(*numbers, lt=2, ut=9)

    assert result == answer

def test_average_with_empty():
    calculator = SimpleCalculator()

    numbers = []
    answer = 0

    result = calculator.average(*numbers)

    assert result == answer

def test_average_with_excluding_lower_thresh():
    calculator = SimpleCalculator()

    numbers = [2,3,7,15]
    answer = 0

    result = calculator.average(*numbers, lt=19)

    assert result == answer

def test_average_with_excluding_upper_thresh():
    calculator = SimpleCalculator()

    numbers = [2,3,7,15]
    answer = 0

    result = calculator.average(*numbers, ut=1)

    assert result == answer

def test_average_with_excluding_lower_thresh_and_upper():
    calculator = SimpleCalculator()

    numbers = [2,3,7,15]
    answer = 0

    result = calculator.average(*numbers, lt = 15, ut=7)

    assert result == answer

def test_average_empty_with_thresh():
    calculator = SimpleCalculator()

    numbers = []
    answer = 0

    result = calculator.average(*numbers, lt = 15, ut=7)

    assert result == answer