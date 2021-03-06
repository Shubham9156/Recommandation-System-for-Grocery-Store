# -*- coding: utf-8 -*-
"""ReacommendationSystemForGroceryStore.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TOX-azvFCqTnlZGY4vy2OFWQ2CY6ljOc
"""

import numpy as np
import pandas as pd

df = pd.read_csv('GroceryStoreDataSet.csv',header=None)
df

df.isnull().sum()

df.values.tolist()

T = []
for i in range(len(df)):
  T.append([str(df.values[i,j]) for j in range(0,4) if str(df.values[i,j]) !='nan'])

T

pip install apyori

from apyori import apriori
rules = apriori(T,min_support=0.03,min_cinfidence=0.35,min_lift=3,min_length=2)

list(rules)

