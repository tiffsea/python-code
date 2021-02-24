"""
convert a `.txt` file to csv
- file must be in the format:
some title of file
some column A row 1
some column B row 1
some column N row 1
...
some column A row N
some column B row N
some column N row N
...
"""

# necessary imports
import pandas as pd


# define helper methods
def _add_data(c, dct, data):
    if c not in dct:
        dct[c] = [data.rstrip('\n')]
    else:
        dct[c].append(data.rstrip('\n'))
    return dct


# define class
class ConvertTxtCsv:

    def __init__(self, fp, col_num):
        """
        :param fp: string; file path of txt file
        :param col_num: int; specify how many columns of data is in txt file
        """
        self.csv = {}
        self.read_txt_file(fp, col_num)
        self.title = None

    def read_txt_file(self, fp, col):
        counter = 1  # start counter at 1; will increment until max or col_num
        with open(fp) as f:
            for i, line in enumerate(f):
                if i == 0:  # first line should be proposed title of csv
                    self.title = line.replace(' ',
                                              '_')  # replaces single space with '_'
                elif counter == col:
                    self.csv = _add_data(counter, self.csv, line)
                    counter = 1
                else:
                    self.csv = _add_data(counter, self.csv, line)
                    counter += 1

    def get_csv_as_dct(self):
        return self.csv

    def get_csv_as_df(self):
        return pd.DataFrame(self.csv)

    def set_csv_as_file(self):
        f = pd.DataFrame(self.csv)
        f.to_csv(self.title + '.csv')