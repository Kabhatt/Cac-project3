from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash

from calc.history.calculations import Calculations
from csvmanager import read
from csvmanager.read import Read


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            Calculator.get_history_CSV()
            flash('You successfully calculated')
            flash('You are awesome')
            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            data={
                "value1": [value1],
                "value2": [value2],
                "request":[operation]
            }
            Calculations.write_history_csv()
            Calculations.df_dataframe
            df = Read.DataFrameFromCSVFile()
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result,
                                   tables = [df.to_html(classes="data")], tittles = df.columns.volumes, row_data=list(df.values.tolist()), zip=zip)
            return render_template('calculator.html', error=error)

    @staticmethod
    def get():
        return render_template('calculator.html')
