import pandas as pd
import xlrd

excel1 = 'data/MainBook.xlsx'
excel2 = 'data/NewProducts2.xlsx'

df1 = pd.read_excel(excel1)
df2 = pd.read_excel(excel2)
"""wb = xlrd.open_workbook(df1)
wb2 = xlrd.open_workbook(df2)
sheet = wb.sheet_by_index(0)
sheet2 = wb2.sheet_by_index(0)"""


print(df1)

values1 = df1[['Category', 'Product', 'Price', 'Sold_Price']]
values2 = df2[['Category', 'Product', 'Price', 'Sold_Price']]

dataframes = [values1, values2]


join = pd.concat(dataframes)
join.to_excel("output/output1.xlsx")
