import os

class Write:
    @staticmethod
    def DataFrameToCSVFile(df):
        df.to_csv('tests/test_data/input.csv', mode='a', index=False, header=False)