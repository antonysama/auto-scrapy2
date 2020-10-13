import pandas as pd
from datetime import date

df1=pd.read_csv('f1.csv',parse_dates=True, dtype='unicode')
df1=df1[~df1['date'].str.contains('date')]

unwanted = df1.columns[df1.columns.str.startswith('Unnamed')] # column cleaning
df1.drop(unwanted, axis=1, inplace=True)

df1.to_csv('f1.csv')
