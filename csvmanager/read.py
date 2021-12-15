import os

import pandas as pd
filename = "test/test_data/input.csv"

class Read:
    @staticmethod
    def DataFrameFromCSVFile(filename, df):
        return pd.read_csv(os.path.abspath(filename))