# GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ (ADVANCED FUNCTİONAL EDA )
# Genel Resim
# Kategoik Değişken Analizi (Analysis of Categorical Variables)
# Sayısal Değişken Analizi (Analysis of Numerical Variables)
# Hedef Değişken Analizi (Analysis of Target Variables)
# Korelasyon Analizi(Analysis of Correlation)

# Genel resim
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape()
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()

def check_df(dataframe, head=5):
    print('#######SHAPE#####')
    print(dataframe.shape)
    print('#####TYPES####')
    print(dataframe.dtypes)
    print('######HEAD#####')
    print(dataframe.head(head))
    print('######TAİL######')
    print(dataframe.tail(head))
    print('#####NA#####')
    print(dataframe.isnull().sum())
    print('#####QUANTİLES####')
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)
check_df(df)


df = sns.load_dataset("tips")
check_df(df)

df = sns.load_dataset("flights")
check_df(df)





