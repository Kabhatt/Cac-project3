import os


class Write:
    @staticmethod
    def DataFrameToCSVFile(filename, df):
        return df.to_csv("tests/tesT_data/input.csv", index=True, header=True)
