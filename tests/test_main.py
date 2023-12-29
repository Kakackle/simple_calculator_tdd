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
