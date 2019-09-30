from django.test import TestCase

from numpy import nan as NaN
import pandas as pd
import numpy as np
# Create your tests here.

# excelFile = open('D:/paper/upload/user/'+ myFile.name, 'wb+')

df=pd.read_excel('D:/paper/upload/title/题目.xlsx')
df=df.fillna('')
row=df.shape[0]
print(df)
# for i in range(row):
#     title=df.iloc[i,0]
#     title_class=str(df.iloc[i,1])
#     A=str(df.iloc[i,3])
#     B=str(df.iloc[i,4])
#     C=str(df.iloc[i,5])
#     D=str(df.iloc[i,6])
#     answer=df.iloc[i,7]
#     score=df.iloc[i,8]
#     print(title,title_class,A,B,C,D,answer,score)
