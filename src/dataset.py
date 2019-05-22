import os
import pandas as pd


def load_excel(file_name, skip_rows=14, cols=None):
    """
    Load excel file as data frame.

    :param file_name: name of excel file
    :param skip_rows: Rows to skip in excel file
    :param cols: Column index to be loaded
    :return: Pandas data frame
    """
    dir = "../datasets"
    path_ = os.path.join(dir, file_name)
    if cols is None:
        cols = [0, 1]
    df = pd.read_excel(path_, skiprows=skip_rows, usecols=cols)
    headers = df.iloc[0]
    df = df[1:]
    df.columns = headers
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index('Date')
    return df