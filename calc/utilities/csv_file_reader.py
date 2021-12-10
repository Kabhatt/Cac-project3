import pandas as pd
import os
import glob
import csv

class reader:
    """File reader class"""

    def __init__(self, csv_file):
        self.csv_file = csv_file

    @property
    def file_name(self):
        return self.csv_file

    def read_csv(self):
        path = os.getcwd()
        csv_file = glob.glob(os.path.join (path, "*.csv"))
        for f in csv_file:
             df=pd.read_csv(f)
             print('Location:', f)
             print("File Name:", f.split("\\")[-1])
             print("Content:")
             print()

    def write_csv(self):
       f=open("path/to/csv_file', 'w'")
       writer = csv.writer(f)
       writer.writerow(self)
       f.close

    def converting_df(self):
        path = "/Users/kashishbhatt/PycharmProjects/calc2/tests/test_data"
        filenames = glob.glob(path + "/*.csv")
        for filename in filenames:
            dfs = (pd.read_csv(filename))
            df = dfs.transpose()
            df.to_csv(os.path.join(r'transposed\Tr_', filename))

