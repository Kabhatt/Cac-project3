import os

class Write:
    @staticmethod
    def DataFrameToCSVFile_Write(filename, df):
            return df.to_csv(os.path.abspath(filename), float_format="%.2f", index=True, header=True)

    @staticmethod
    def dictionary_to_csv_file(filename, dictionary):
        return dictionary.to_csv(os.path.abspath(filename))

    @staticmethod
    def write_csv_to_history(filename, history):
        return history.to_csv(os.path.abspath(filename))