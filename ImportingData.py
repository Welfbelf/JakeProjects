import pandas as pd
import numpy as np

def LoadOriginalCSV():
    df = pd.read_csv('monster_com-job_sample.csv', index_col = 'uniq_id')
    return df

def LoadAdjustedCSV():
    df = pd.read_csv('adjusted_csv.csv', index_col= 0)
    return df


def SaveAdjustedCSV(df):
    pd.DataFrame.to_csv(df, 'adjusted_csv.csv')


def LoadAndSaveOriginalCSV():
    df = LoadOriginalCSV()
    SaveAdjustedCSV(df)

