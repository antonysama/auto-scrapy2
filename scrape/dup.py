import pandas as pd
from datetime import date
import numpy as np
import re

## f is today's f1 is the whole
df=pd.read_csv('f.csv', parse_dates=True, dtype='unicode')
df1=pd.read_csv('f1.csv',parse_dates=True, dtype='unicode')

##clean
unwanted = df1.columns[df1.columns.str.startswith('Unnamed')] # column cleaning
df1.drop(unwanted, axis=1, inplace=True) #column cleaning
df1=df1[~df1['date'].str.contains('date')] #row cleaning
df1=df1[~df1['date'].str.contains('date')]

##concat f w. f1
c=pd.concat([df,df1], sort=True)

##removing duplicates
c = c.sort_values('date', ascending=False)
c = c.drop_duplicates(subset='title', keep='last')

##reorder cols
c=c[['date', 'title','source','link']]
# print(c.head(5))

#save
c.to_csv('f1.csv', index=False)
