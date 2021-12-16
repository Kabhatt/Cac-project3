"""Calculation history Class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
import pandas as pd
from csvmanager.write import Write


class Calculations:
    """Calculations class manages the history of calculations"""
    history = []

    @staticmethod
    def readHistoryFromCSV():
        """Read the history from csv and put it into the history """

    @staticmethod
    def writeHistoryToCSV():
        """Write the history to csv file"""

    # # pylint: disable=too-few-public-methods
    @staticmethod
    def create_dataframe_write(value1, value2, result, operation):
        """Puts values to history"""
        df_write = pd.DataFrame(columns=['value_1', 'value_2', 'result', 'operation performed'])
        df_write = df_write.append({'value_1': value1,
                                    'value_2': value2,
                                    'result': result,
                                    'operation': operation},
                                   ignore_index=True)
        return Write.DataFrameToCSVFile(df_write)

    @staticmethod
    def clear_history():
        """clear the history of calculations"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """get number of items in history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        """get last calculation"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation"""
        calculation = Calculations.get_last_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_first_calculation():
        """get first calculation"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a generic calculation from history"""
        return Calculations.history.append(calculation)

    @staticmethod
    def add_addition_calculation_to_history(values):
        """create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Addition.create(values))
        # Get the result of the calculation
        return True

    @staticmethod
    def add_subtraction_calculation_to_history(values):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True

    @staticmethod
    def add_multiplication_calculation_to_history(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True

    @staticmethod
    def add_division_calculation_to_history(values):
        """Add a division object to history using factory method create"""
        Calculations.add_calculation(Division.create(values))
