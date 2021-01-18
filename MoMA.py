# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:35:34 2021

@author: snikkho
"""

import pandas as pd
import numpy as np

csv_path = r'C:\Users\snikkho\Artworks.csv'
df = pd.read_csv(csv_path)
df1 = df.dropna(subset=['Title'])
df1 = df1.dropna(subset=['Artist'])
df1 = df1.dropna(subset=['DateAcquired']) # removed rows that contained blank

count = df1['Department'].value_counts()
Q2_Answer = count['Photography']/count.sum()

df2 = df1.Title.str.lower()
Q3_Answer = df2.str.count("untitled").sum()

df3 = df1.dropna(subset=['Duration (sec.)']) # 2045 count
List = df3['Duration (sec.)'] > 36000
List.value_counts(True)

df4 = df1.Medium.str.lower()
Q4_Answer = df4.str.count("paper").sum()/df4.str.count("canvas").sum()

df5['Ratio'] = np.where(df5['Height (cm)']!= 0, df5['Width (cm)']/df5['Height (cm)'], False)