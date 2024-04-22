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

# Kategorik Değişken Analizi(Analysis of Categorical Variables)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["embarked"].value_counts()
df["sex"].unique()
df["sex"].nunique()
df["survived"].value_counts()

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

cat_cols = cat_cols + num_but_cat
cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols]
df[cat_cols].nunique()
[col for col in df.columns if col not in cat_cols]

df["survived"].value_counts()
100 * df["survived"].value_counts() / len(df)

def cat_summary(dataframe,col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##################################")

cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)

def cat_summary(dataframe,col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

cat_summary(df, "sex", plot=True)

for col in cat_cols:
    if df[col].dtypes == "bool":
       print("sjsjjsjsjsjsjsj")
    else:
       cat_summary(df, col, plot=True)


df["adult_male"].astype(int)

for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)

    else:
       cat_summary(df, col, plot=True)







def cat_summary(dataframe,col_name, plot=False):
    if dataframe[col].dtypes == "bool":
        dataframe[col] = dataframe[col].astype(int)

    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##################################")

    if plot:
     sns.countplot(x=dataframe[col_name], data=dataframe)
     plt.show(block=True)
    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##################################")
    if plt:
       sns.countplot(x=dataframe[col_name], data=dataframe)
    plt.show(block=True)

cat_summary(df, "adult_male", plot=True)


