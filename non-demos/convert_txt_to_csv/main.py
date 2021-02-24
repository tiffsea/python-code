# necessary imports
import os
from convert_txt_to_csv import ConvertTxtCsv


# define functions
def get_fp(fn):
    """
    :param fn: string; file name (fn)
    :return: file path (fp) of fn
    """
    print(f'Your current working directory is {os.getcwd()}\n')

    return os.getcwd() + fn


txt_file = '/NAME OF TXT FILE.txt'  # change the name of file
num_data_cols = 3  # change the number of columns
fp = get_fp(txt_file)
ConvertTxtCsv(fp, num_data_cols).set_csv_as_file()
