# VERİ GÖRSELLEŞTİRME: MATPLOTLİB & SEABORN
import numpy as np
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


# Matplotlib'in Özellikleri

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

# plot
# Veriyi görselleştirmek için kullandığımız fonksiyonlardan birisi

x = np.array([1, 8])
y = np.array([0, 150])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()

x = np.array([2, 4, 6, 8, 10])
y = np.array([1, 3, 5, 7, 9])

plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o')
plt.show()

# marker

# işaretleyici özellikleri

y = np.array([13, 28, 11, 100])

plt.plot(y, marker='o')
plt.show()

plt.plot(y, marker='*')

markers = ['o', '*', '.', ',', 'x', 'X', '+', 'P', 's', 'D', 'd', 'p', 'H', 'h']

# line
y = np.array([13, 28, 11, 100])
plt.plot(y)
plt.show()
# düz çizgiyle grafiği çizer.

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashed")
plt.show()
# Kesikli çizgiyle grafiği çizer

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dotted")
plt.show()
# Daha küçük kesikli çizgi(nokta denilebilir) ile grafiği çizer.

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashdot")
plt.show()
# Hem nokta kemde kesikli çizgi ile grafiği çizer.

y = np.array([13, 28, 11, 100])
plt.plot(y, linestyle="dashed", color="r")
plt.show()
# renk eklenmiş oldu

# Multiple Lines

x = np.array([23, 18, 31, 10])
y = np.array([13, 28, 11, 100])
plt.plot(x)
plt.plot(y)
plt.show()

# Labels

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.show()

# Başlık
plt.title("Başlık eklendi")
# Başlık ekler

# X ekseni isimlendirme
plt.xlabel("X ekseni isimlendirmesi")

# Y ekseni isimlendirme
plt.ylabel("Y ekseni isimlendirme")

# Okunabilirliğin artması için birim kare ekleme
plt.grid()
plt.show()

# Subplots

# plot1
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 2, 1)
# 1 satırlık , 2 sütunluk 1. grafiği oluştuluyor.
plt.title("1")
plt.plot(x, y)

#plot2
x = np.array([8, 8, 9, 9, 10, 10, 11, 11, 12, 12])
y = np.array([24, 20, 26, 27, 28, 29, 30, 31, 32, 33])
plt.subplot(1, 2, 2)
# 1 satırlık , 2 sütunluk 2. grafiği oluştuluyor.
plt.title("2")
plt.plot(x, y)

#plot3
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 3, 3)
# 1 satırlık , 2 sütunluk 2. grafiği oluştuluyor.
plt.title("3")
plt.plot(x, y)
plt.show()

# 3 adet plot yapıldı ama 3ünü beraber çalıştırınca hata aldım tekrar bakılıp kontrol edilecek





