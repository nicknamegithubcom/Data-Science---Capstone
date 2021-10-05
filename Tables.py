import pandas as pd
import numpy as np
import xlrd as xlrd

df=pd.read_excel(r'C:/Users/ovidi/Desktop/IBM_DataScience/Data_Visualization_With_Python/UN_MigFlow_A_to_E/Canada.xlsx',
                 engine='openpyxl', header=0, skiprows=range(0, 20), sheet_name='Canada by Citizenship')
df.drop(list(df.filter(regex= 'Unnamed')), axis = 1, inplace = True)
#for col in df.columns:
        #print(col)
       # if col
# print(df.info())
# print(df.head())
print(df.iloc[:6,:5])


#pd.read_excel()
