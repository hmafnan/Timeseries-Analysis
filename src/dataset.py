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
        cols = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    df = pd.read_excel(path_, skiprows=skip_rows, usecols=cols)
    headers = df.iloc[0]
    df = df[1:]
    df.columns = headers
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.set_index('Date')
    return df


def load_all_regions(df):
    df_italy = df.iloc[:, 0:1]  # Arrivals to Italy
    df_greek_island = df.iloc[:, 1:2]  # Arrivals to Greek Island
    df_mainland_greece = df.iloc[:, 2:3]  # Arrivals to Mainland greece
    df_fyrom = df.iloc[:, 3:4]  # Arrivals to fYRoM
    df_serbia = df.iloc[:, 4:5]  # Arrivals to Serbia
    df_croatia = df.iloc[:, 5:6]  # Arrivals to Croatia
    df_hungry = df.iloc[:, 6:7]  # Arrivals to Hungry
    df_slovenia = df.iloc[:, 7:8]  # Arrivals to Slovenia
    df_austria = df.iloc[:, 8:9]  # Arrivals to Austria

    return {"italy": df_italy,
            "greek_island": df_greek_island,
            "mainland_greece": df_mainland_greece,
            "fyrom": df_fyrom,
            "serbia": df_serbia,
            "croatia": df_croatia,
            "hungry": df_hungry,
            "slovenia": df_slovenia,
            "austria": df_austria}