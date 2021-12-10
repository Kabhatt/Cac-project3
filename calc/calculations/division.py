"""This is the division calculation"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """This is the Division class which gets the result from the parent Calculation class"""
    def get_result(self):
        """Gets Results"""
        division_values= self.values[0]
        try:
            for i, value in (division_values):
                if i==0:
                    return division_values/value
        except ZeroDivisionError:
                    return "ZERO DIVISION ERROR CANNOT DIVIDE!"