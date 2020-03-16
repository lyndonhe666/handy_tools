# this file contains handy tools in data processing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def report_null(df):
    """
    Use to report detailed null value in a dataframe in pandas style
    """
    res = pd.DataFrame({col:sum(df[col].isnull()) for col in df.columns},index=range(1)).T.reset_index().rename(columns={'index':'column_name',
                                                                                                                        0:'number of null'})
    res['percentage'] = res.apply(lambda x:100*(x['number of null']/len(df[x['column_name']])),axis=1)
    return res