import pytest
import pandas
import pandas as pd
import os.path
from calc.calculator import Calculator
from calc.utilities.csv_file_reader import reader
from csvmanager.read import Read


@pytest.fixture(name="clear_history")
def fixture_clear_history():
    """clear history function"""
    Calculator.clear_history()


def csv_addition_test(addition_file_fixture):
    """Testing Addition.csv file"""
    file = open("addition.csv")
    reader_csv = reader.read_csv(file)
    for row in reader_csv:
        print(int(row[0]), int(row[1]))
        assert Calculator.add_numbers(int(row[0]), int(row[1])) == int(row[2])


def csv_subtraction_test(addition_file_fixture):
    """Testing Addition.csv file"""
    file = open("subtract.csv")
    reader_csv = reader.read_csv(file)
    for row in reader_csv:
        print(int(row[0]), int(row[1]))
        assert Calculator.subtract_numbers(int(row[0]), int(row[1])) == int(row[2])


def csv_multiplication_test(addition_file_fixture):
    """Testing Addition.csv file"""
    file = open("Multiplication.csv")
    reader_csv = reader.read_csv(file)
    for row in reader_csv:
        print(int(row[0]), int(row[1]))
        assert Calculator.multiply_numbers(int(row[0]), int(row[1])) == int(row[2])


def csv_division_test(addition_file_fixture):
    """Testing Addition.csv file"""
    file = open("Division.csv")
    reader_csv = reader.read_csv(file)
    for row in reader_csv:
        print(int(row[0]), int(row[1]))
        assert Calculator.divide_numbers(int(row[0]), int(row[1])) == int(row[2])


def test_csv_read_file():
    """Testing files"""
    filename = "input.csv"
    path = "tests/test_data"
    full_path = path + "/" + filename
    df = Read.DataFrameFromCSVFile()
    assert type(df) is pandas.DataFrame


def test_csv_write_file():
    """Testing files"""
    filename = "input.csv"
    path = "tests/test_data"
    full_path = path + "/" + filename
    name_dictionary = {
        "value_1": [0.994065876],
        "value_2": [0.477762018],
        "result": [471827894],
        "operation": "addition"
    }
    df = Read.DataFrameFromCSVFile()
    assert type(df) is pandas.DataFrame
