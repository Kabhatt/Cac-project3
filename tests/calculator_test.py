"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division

@pytest.fixture
def clear_history():
    Calculator.clear_history()

def add_numbers_test(clear_history):
    """Testing the Add function of the calculator"""
    my_tuple = (2.0,4.0,6.0)
    assert isinstance(Calculator.add_numbers(my_tuple), Addition)
    assert Calculator.get_last_result_value() == 8.0

def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    my_tuple = (2.0, 4.0, 6.0)
    assert isinstance(Calculator.subtract_numbers(my_tuple), Subtraction)
    assert Calculator.get_last_result_value() == -4

def test_calculator_multiply(clear_history):
     my_tuple = (2.0, 4.0, 6.0)
     assert isinstance(Calculator.multiply_numbers(my_tuple), Multiplication)
     assert Calculator.get_last_result_value() == 48

def test_divide_numb(clear_history):
    my_tuple = (4.0, 2.0, 1.0)
    assert isinstance(Calculator.multiply_numbers(my_tuple), Multiplication)
    assert Calculator.get_last_result_value() == 2
    my_tuple = (2.0, 0.0, 0.0)
    assert isinstance(Calculator.multiply_numbers(my_tuple), Multiplication)
    assert Calculator.get_last_result_value() == ZeroDivisionError


