# this file contains handy tools in data processing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def report_null(df):
    """
    Use to report detailed null value in a dataframe in pandas style
    """
    return pd.DataFrame({col:sum(df[col].isnull()) for col in df.columns},index=range(1)).T.rename(columns={0:'column_name'})