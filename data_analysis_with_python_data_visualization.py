# VERİ GÖRSELLEŞTİRME: MATPLOTLİB & SEABORN

# MATPLOTLIB
# Düşük seviye bir veri görselleştirme aracıdır.
# Kategorik bir değişken varsa sütun grafiği ile görselleştiriyoruz. countplot ya da bar ile gerçekleştirilebilir.
# Sayısal değişken varsa histogram(hist), boxplot ile veri görselleştirilir.

# Veri görselleştirmesi için BI(Business Intelligence) araçları daha çok kullanılmaktadır. Power BI gibi.

# Kategorik Veri Görselleştirme

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind='bar')
plt.show()


# Sayısal Veri Görselleştirme

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

plt.hist(df["age"])
plt.show()

plt.boxplot(df["fare"])
plt.show()




