# -*- coding = utf-8 -*-
# @Time:2022/11/24 18:54
# @Author:宇
# @File:pandas.py
# @Software:PyCharm
import pandas as pd

miss_values = ['n/a','na','--']

df = pd.read_csv('property-data.csv',na_values=miss_values)

print(df['NUM_BEDROOMS'])
# # print(df['NUM_BEDROOMS'].isnull())
# new_df = df.dropna()
# print(new_df.to_string())