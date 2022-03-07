import numpy as np
import pandas as pd
import xlrd

excel1 = 'data/MainBook.xlsx'
excel2 = 'data/NewProducts2.xlsx'

df1 = pd.read_excel(excel1)
df2 = pd.read_excel(excel2)

comparevalues = df1.values == df2.values
print(comparevalues)

rows, cols = np.where(comparevalues == False)
for item in zip(rows, cols):
    df1.iloc[item[0], item[1]] = '{} --> {}'.format(
        df1.iloc[item[0], item[1]], df2.iloc[item[0], item[1]])
df1.to_excel('output/output.xlsx', index=False, header=True)
