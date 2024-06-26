#  PYTHON İLE VERİ ANALİZİ (DATA ANALYSIS WİTH PYTHON)
#  NumPy : Matematiksel işlemler iin ortaya çıkmıştır.
#  Pandas: NumPy üzerine kuruludur. Veri analizi , veri manipülasyonu dendiğinde akla ilk gelen kütüphanedir. NumPy bazi
#  fonksiyonlarını veri tutma biçimlerini geliştirmiştir.
#  Veri Görselleştirme :Matpolit & Seaborn: Elimizdeki verileri görselletştirmek için düşük ve  yüksek seviye
#  diyebileceğimiz yaygın iki kütüphanedir.
#  Gelişmiş Fonksiyonel Keşifçi Veri Analizi (Advanced Functional Exploratory Data Analysis): Elimize büyük ölçekli bir
#  problem geldiğinde fonksiyonel bir seviyede nasıl çözebileceğimizi değerlendireceğiz.


#  NUMPY (Numerical Python)
#  Neden NumPy? (Why NumPy?)
#  NumPy Array-i oluşturmak (Creating Numpy Arrays)
#  NumPy Array Özellikleri (Attributes of Numpy Arrays)
#  Yeniden Şekillendirme (Reshaping)
#  İndex Seçimi (Index Selection)
#  Slicing
#  Fancy Index
#  NumPy- da Koşullu İşlemler ( Conditions on Numpy)
#  Matematiksel İşlemler ( Mathematical Operations)


#  Bilimsel hesaplamaları yapmak için kullanılır. Array-ler  çok boyutlu array-ler ve matrisler üzerinde yüksek
#  performanslı çalışma imkanı sunar.
#  Numpy-ı listelerden ayıran özellikleri: Verimli veri saklamamızı sağlar. Yüksek seviyeli (vektörel) işlemlerdir.
#  Sabit tipte (Mesela sadece int gibi ) veri tutmamızı sağlar. Daha az çaba ile daha fazla işlem yapmamızı sağlar.

#  NumPy kütüphanesi aşağıdaki gibi çağırılabilir. Biz np şeklinde kısa bir isimlendirme kullandık.
#  Bunda kendi isimlendirmenizi kullanabilirsiniz.

import numpy as np

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

#  Bütün elemanların biribiri ile  çarpımını istiyoruz. Normalde bunun için aşağıdaki döngüyü kurarız.

ab =[]

for i in range(0, len(a)):
     ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])

a * b

#  NumPy Array-i Oluşturmak (Creating NumPy Arrays)

import numpy as np

#  Sıfırdan array oluşturmak için array fonksiyonu kullanılır.
np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

#  Çeşitli opsiyonlarda array üretmek için zeros fonksiyonu kullanılır. Bu fonksiyonda sıfır elemanlarından istenilen
#  tipte ve istediğimiz sayıda elemanla array oluşturmak için kullanılır
np.zeros(10, dtype=int)

#  Aşağıdaki random.randint fonksiyonunda 0-10 aralığında kaç tane seçim yapmak istediğini yazıp ,biz burda 10 yazdık,
#  fonksiyonu çalıştırdığında sana array oluşturur. Sonuç olarakta 0-10 arasında rastgele 10 tane int seçildi.

np.random.randint(0, 10, size=10)

#  Eğer belirli bir istatiksel dağilıma göre üretmek istersek; sırasıyla ilk olarak ortalaması , standart sapmasını ve
#  kaça kaçlık bir array istiyorsak bunu belirtmeliyiz. Ayrıca burada matris gibi düşünürsek daha kolay anlayabiliriz.
#  (satır,sütun)

np.random.normal(10, 4, (3, 4))

#  NumPy Array Özellikleri (Attributes of NumPy Arrays)

import numpy as np

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)
# burada 0 dan 10 a kadar yazmadım ama fonksiyon otomatik olarak öyle algılayacak.
a.ndim
# tek boyutlu olduğu için 1 geldi.
a.shape
# (5,) çıktısı geldi tek boyutlu ve içerisinde 5 tane eleman var bilgisiniz verdi. Eğer iki boyut olsaydı her boyuttaki
# eleman sayısı gelecekti.
a.size
# toplam eleman sayısını verdi 5 çıktısı geldi
a.dtype
# veri tipini verdi int32 veri tipindeymiş int 64 te olabilirdi.


# Yeniden Şekillendirme (Reshaping)

import numpy as np

np.random.randint(1, 10, size=9)
# bunu bir matrise veya iki boyutlu bir array-e  çevirmek istiyorum. reshape metodunu kullanarak yapabiliriz.
np.random.randint(1, 10, size=9).reshape(3, 3)
# YADA
ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)
# ANCAK BU ÇEVİRMEDE SİZE GÖZÖNÜNE ALINMALIDIR.
ar = np.random.randint(1, 10, size=10)
ar.reshape(3, 3)

#  INDEX SEÇİMİ (INDEX SELECTİON)

import numpy as np
a = np.random.randint(10, size=10)
a
a[0]
a[0:5]
# şurdan şuraya kadar git 0 dahil,5 hariç bunada slicing denir.

a[0] = 100
#  0 indeksindeki elemanı değiştirmemizi sağlar.

m = np.random.randint(10, size=(3, 5))
m[0, 0]
# ilk kısım satırı ikinci kısım sütunu ifade etmektedir. 0. satır0.sütun.

m[2, 3] = 999

m[2, 3] = 2.9
# girdiğimiz veri tipi float olup normalde m int veri sakladığından veriyi integer a çevirip ekleme yapar bu da numpy-ın
# tek veri tipinde saklama yapıp verimli veri sakladığını gösterir.

m[:, 0]
# bütün satırları seçip 0. indeksteki sütunu seçer

m[1, :]
# 1.satırı seçip bütün sütunları seçer.

m[0:2, 0:3]
# 0 dan 2ye kadar git satırlarda ,0 dan 3 e kadar git sütunlarda

# FANCY INDEX

import numpy as np

v = np.arange(0, 30, 3)
v
# 0 dan 30 a kadar 3 er 3er aralıkla array oluşturur. 30 dahil değil.
v[1]
v[4]

catch = [1, 2, 3]
# bu indekslere sahip eleanları getirmek için aşağıdaki komutu kullanıyoruz.
# bunu genellikle birden fazla elemanı değiştirmek istediğimizde indeksi çağırabiliriz.
v[catch]

# NumPy da Koşullu işlemler(Conditions on Numpy)

import numpy as np
v = np.array([1, 2, 3, 4, 5])

# Amaç array içerisinde 3-ten küçük elemanlara erişmek

# Klasik Döngü ile
ab = []
for i in v:
     if i < 3:
          ab.append(i)

# NumPy ile

v[v < 3]
v[v > 3]
v[v != 3]
v[v == 3]
v[v >= 3]

# Matematiksel İşlemler (Mathematical Operations)

import numpy as np
v = np.array([1, 2, 3, 4, 5])
# Operatörler aracılığı ile gerçekleştirelim.
v /5
v * 5 / 10
v ** 2
v - 1

# Metodlar aracılığı ile gerçekleştirirsek.

np.subtract(v, 1)
# çıkarma işlemi için metotdur.
np.add(v, 1)
# toplama işlemi için metotdur.
np.mean(v)
# ortalamasını almak için metotdur.
np.sum(v)
# tüm elemanları toplayan metotdur.
np.min(v)
# min elemanını bulan metotdur.
np.max(v)
# max elemanını bulan metotdur.
np.var(v)
# varyans bulan metotdur.

# NumPy ile İki Bilinmeyenli Denklem Çözümü
# 5*x0 + x1 = 12
# x0 + 3*x1 = 10
# Aşağıdaki metotlar kullanılarak çözüm bulunabilir.

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])
np.linalg.solve(a, b)

#  Neden NumPy?
#  Hızından dolayı yani sabit tipte veri tipi sakladığından dolayı bu hız kazandırır.
#  Fonksiyonel, vektörel, yüksek düzeyde bize kolaylık sağlamasıdır.


# PANDAS
# Veri Manipülasyonu ya da veri analizi dendiğinde akla gelen ilk python kütüphanelerinden biridir. Öncelikle
# ekonometrik ve finansal çalışmalar için doğmuş daha sonra veri analitiği dendiğinde en sık kullanılan kütüphaneler
# haline gelmiştir. Temeli 2008 de atılmıştı. Bir çok veri yapısı ile çalışma imkanı sunmaktadır, bir çok farklı
# kaynaklardan veri okuma imkanına sahiptir.

# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick look at Data)
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri


#  Pandas Series
import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
# Pandas serisinde indeks göstermek bir iç özelliktir. Bu özellik ekonometri ve zaman serisi ihtiyacı için ortaya çıkmış
# Dolayısıyla zamana bağlı seriler diziler oladuğundan dolayı  gelen çıktı gibi bir indeks bilgimiz var.

type(s)
# s değişkeninin ne tipte veri olduğunu söyler.
s.index
# çıktısı  RangeIndex(start=0, stop=5, step=1) olur, bu da 0 dan başlayıp 5-e kadar 1 artarak indekslenir anlamındadır.
# 5 harici
s.dtype
# içerisindeki verinin tip bilgisini verir.
s.size
# içerisindeki eleman sayısı
s.ndim
# boyutunu verir.
s.values
# s-in elemanlarına erişmek için kullanılır. Bu metot yani values eklemesi yapıldıktan sonra indekslerle
# ilgilenmediğimiz için gelen çıktı numpy array tipindedir.
type(s.values)
s.head()
s.head(3)
# Baştan 3 tanesini getirir.
s.tail(3)
# sondan 3 tanesini getirir.


# Veri Okuma (Reading Data)

#  Pandas bir çok farklı tipteki veriyi kolay bir şekilde okuma imkanı sağlar. İçerisinde bulunan metotlar aracılığıyla
#  csv ,txt, excel ya da  diğer bazı özel dosya formatlarını okuyabilir ve üzerinde çalışabilirsiniz.
#  Datasets oluşturulduktan sonra csv dosyası kaydedildi ve  aşağıda da nasıl okunacağını göstereceğiz.

import pandas as pd
df = pd.read_csv("datasets/advertising.csv")
df.head()
# Burada pd.read kısmında pd üzerine gelip ctrl- ye tıklayıp dökümanı açtıktan sonra ctrl+f diyoruz ve csv dosyası
# haricinde read_ dediiğimizde kullanabileceğimiz metotlar gelir.Bu metotlar farklı formatlarda klasörlere uygulanacak
# olanlardır. Eğer burada kullanmak istediğimiz bir metot var ve bunun nasıl kullanabileceğimiz bulmak için istediğimiz
# metodun üstüne gelip tıklıyoruz. docstring kısmında fonksiyonların detaylarını görebiliriz.
# Pandas  cheatsheet araması ile pandas kütüphanesinde kullanılan bütün metotları fonksiyonları derli toplu bir şekilde
# bulabilirsiniz.

#  Veriye Hızlı Bakış (Quck look at Data)

import seaborn as sns
import pandas as pd


# Seaborn kütüphanesinin içerisindeki bu metot ben seabornun içindakı bazı yaygın verileri koydum, siz bunlarla kolayca
# çalışın, anlamına gelmektedir. Biz bu veri setlerine aşağıdaki gibi erişim sağlayabilriz.

df = sns.load_dataset("titanic")
df.head()
# head metoduyla veriye hızlı bir göz attık.
df.tail()
# tail ile sondan değerlere göz attık.
df.shape
# shape ile boyut bilgisini öğrenmiş olduk.
df.info()
# değişkenlerle alakalı bilgileri bize verir, hangi veri tipine sahip olduğunu ne kadarı dolu ,ne kadarı eksik bilgiye
# sahip bunlar hakkında bize bilgi verir. Burada değişken tiplerinde object ve category değişken tipleride bizim için
# kategorik değişkenlerdir. Genel olarak object veri tipleride kategorik değişkenlerdir.
df.columns
#  bir data frame-in direkt değişkenlerine ulaşmak için columns metodunu kullanabiliriz.
df.index
# İndeks bilgilerini verir. nerden başlayıp nereyekadar devam ettiğini ve kaçar kaçar arttığını bize söylemektedir.
df.describe()
# Elimizdeki bir data frame-in hızlı bir şekilde istatistik bilgilerine erişmek istiyorsak describe metodunu kullanırız .
# Ancak daha okunabilir olması açısından aşağıdaki yöntemi uygulayarak daha rahat okunabilir
df.describe().T
# Buradaki T kısmını transpozunu almak gibi düşünebiliriz.
df.isnull().values.any()
# Bu metot aslında değişkenlerin herhangi birisinde boşluk yani eksiklik var mı anlamındadır.Çıktıyı boolean tipinde
# vermektedir. True veya False olarak.
df.isnull().sum()
# Değişkenlerde bir eksiklik durumu var mı bunu öğrenebilmek için yukarıdaki metot kullanılır. Hangi değişkende kaç tane
# var ihtiyacını karşılamaktadır.
df["sex"].value_counts()
#  Bu metot herhangi bir kategorik değişkenin içerisinde kaç tane sınıf var bunlar neler ve bu kategorik sınıflardan
#  hangisine ne kadar sahipiz bunu öğrenmek için kullanırız.Biz örnek olarak cinsiyet için uyguladık ve kadın erkek için
#  kaç veriye sahip bunu gösterdi.

#  Pandas'ta Seçim İşlemleri (Selection in Pandas)
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

df.index
# indeks bbilgilerine ulaştık
df[0:15]
# slicing işlemi yapıldı.
df.drop(0, axis=0).head()
# indekslere bağlı olarak satırlardan mı sütunlardan mı bir şey silmek istediğimizi bildirdik ve gözlemleyebilmek için
# head metodunu kullandık. Biz yukarıda satır sildik. Eğer burada birden fazla indekse göre silme işlemi yaparsak
# aşağıdaki gibi bir yol izlemeliyiz.
df.drop("delete_indexes", axis=0).head(10)
delete_indexes = [1, 3, 5, 7]

# yukarıdaki silme işlemi kalıcı değildir ancak kalıcı hale getirmek için aşağıdaki yöntemleri kulanabiliriz.
# df = df.drop(delete_indexes, axis=0)
# df.drop(delete_indexes, axis=0, inplace=True)

# Değişkeni İndex'e Çevirmek

df["age"].head()
df.age.head()

df.index = df["age"]

# Burada aslında yapılmak istenen bir değişkenin yerine diğer değişkeni taşımak yani indeksi yaşla değiştirmek gibi

df.drop("age", axis=1, inplace=True)
# son yapılan komutlada age kolonu silindi ve indeks kısmındada yaş veileri yer almaktadır.

# İndex' i Değişkene Çevirmek
# 1. YOL
df.index
df["age"] = df.index
df.head()
# yaş verileri öncesinde silindiği için yeni değişken olarak eklendi
# Şimdi yaş değişkenini tekrar silip 2. yolu görelim.
df.drop("age", axis=1, inplace=True)
# 2. YOL
df.reset_index().head()
# indekste yer alan değeri silecektir, sildiği değeri sütun olarak ekleyecektir.
df = df.reset_index()


#  Değişkenler Üzerinde İşlemler

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
# Bu komut değişkenler yani sütunlar arasındaki 3 noktayı kaldırır. Direkt bütün kolonları sıralar.
df = sns.load_dataset("titanic")

# Aşağıdaki komut istediğimiz herhangi bir değişkenin dataframe-in içinde var mı yok mu bunu öğrenmemizi sağlar.
"age" in df
# Eğer bir değişkeni seçmek istersekte aşağıdaki komutlar kullanılır.
df["age"].head()
df.age.head()
type(df["age"].head())
# Bu type komutunun çıktısı pandas Series olacağından dolayı bir değişken seçerken sonucunu seri ya da data frame olması
# için aşağıdaki gibi iki köşeli parantez kullanılırsa data frame değişmez ve veri yapımız bozulmaz eğer iki köşeli
# parantez kullanılmazsa veri yapımız bozulup pandas series olacağından dolayı herhangi bir değişken seçip fonksiyonu
# uyguladığımız zaman hata alırız.
df[["age"]].head()
type(df[["age"]].head())

df[["age", "alive"]]
col_names = ["age", "adult_male", "alive"]
df[col_names]

# Aşağıda yeni değişkenler ekledik.
df["age2"] = df["age"]**2
df["age3"] = df["age"] / df["age2"]

# Aşağıda kalıcı olarak değişken sildik.
df.drop("age3", axis=1, inplace=True)
df.drop(col_names, axis=1).head()

#  mesela yüzlerce belirli bir ifadeyi barındıran değişkenlere nasıl erişicez veya nasıl seçip nasıl silicez diye
#  düşünebiliriz
df.loc[:, df.columns.str.contains("age")].head()
# Yukarıdaki komutta bütün satırları seçip sütunlardada age string ifadesini barındıran değişkenleri seç dedik. Eğer bu
# ifadeyi barındıranların dışındaki sütunlları yani değişkenleri ver deseydik, aşağıdaki gibi ~ eklemesi yapmalıydık
df.loc[:,~df.columns.str.contains("age")].head()
# Buradaki loc data frame lerde seçme işlemimiz  gerçekleştirmek için kullandığımız bir yapıdır.

# iloc & loc

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()
# iloc data frame lerde indeks bilgisi vererek seçim yapma işlemleridir. Açlımıda integer based selection dır.
# loc ise mutlak olarak indekslerdeki label lara göre seçim yapar.açılımı label based selectiondır

# iloc : integer based selection
# 0 dan 3 e kadar olan elemanları seçtik.
df.iloc[0:3]
# 0. satır 0. sütundaki elemanı seç getir
df.iloc[0, 0]

# loc : label based selection
df.loc[0:3]

# loc ve ilocta yazdığımız aynı şeylerin çıktı olarak farklearı loc-ta dediğimiz gibi mutlak olarak 0,1,2,3
# indekslerindeki elemanların hepsini çıktıya verir. iloc- ta ise 0-dan 3-e kadar alıştığımız anlayış vardır.
# Yani loc isimlendirmenin kendisini seçiyor.

df.iloc[0:3, "age"]
# BU KOMUT HATA VERİR ÇÜNKÜ BİZİM ASLINDA PARANTEZ İÇERİSİNDE 0:, 0:3 YAZMAMIZI BEKLİYOR AMA BİZ DEĞİŞKENİN KENDİ ASIL
# İSMİNDE SEÇİM YAPMAK İSTİYORSAK LOC KULLANMALIYIZ
df.loc[0:3, "age"]
col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]

# Koşullu Seçim (Conditonal Selection)
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head(5)
# Yaşı 50 den büyük olanları gösterir.
df[df["age"] > 50].count()
# Yaşı 50 den büyük olanları saydı yani hangisinde kaç tane yaşı 50 den büyük olanlar var diye
df[df["age"] > 50]["age"].count()
# Bu komuttaki gibi değişken seçimi yaparsak sadece onu sayar

df.loc[df["age"] > 50, "class"].head()
# Biz yaşı elliden büyük olanların hangi sınıfta olduklarını öğrenmek istersekbu komutu uygulayabiliriz.
df.loc[df["age"] > 50, ["age","class"]].head()
#  biz yaşı elliden büyük olanların hangi sınıfta olduğunu ayrıca yaşlarının ne olduğunu görmek için bu komutu
#  kullanmamız gerekir
df.loc[(df["age"] > 50 )& (df["sex"] == "male"), ["age", "class"]].head()
# Aynı anda hem elliden büyük hemde erkek olanların hem yaşını hemde sınıfını göster dedik yani iki şart olduğundan
# şartları parantez içerisine aldık.
df.loc[(df["age"] > 50) & (df["sex"] == "male") & (df["embark_town"] == "Cherbourg"), ["age", "class", "embark_town"]].head()
# Bir başka şart daha eklediğimizde & bağlacı ekleyip yeni şartımızı ekledik ve bu şartı sağlayanların yaşını sınıfını
# ve bindikleri yerleri yazdırtmasını istedik. Bu yukarıdaki aynı kodu bir başka düzende yazabiliriz.
# Bunu aşağıdaki gibi yapabiliriz.
df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & (df["embark_town"] == "Cherbourg"),
       ["age", "class", "embark_town"]].head()
# Ya da aşağıdaki gibi embark_town kısmında yeni bir şart ekleyerek yeni bir komut oluşturabiliriz. Ancak önce bir
# embark_town değişkeninde kaç sınıf, tür var bunu öğrenelim
df["embark_town"].value_counts()

df_new = df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()


# Toplulaştırma & Gruplaştırma(Aggretion & Grouping)
# Toplulaştırma bize özet istatistikleri veren fonksiyonlardır.
# count
# first
# last
# mean
# median
# min
# max
# std
# var
# sum
# pivot table

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean()
# Direkt yaş ortalamasını bulduk.

df.groupby("sex")["age"].mean()
#  Buradada cinsiyete göre yaş ortalaması bulundu ve gruplaştırma yapılmış oldu.

df.groupby("sex").agg({"age": "mean"})
df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                       "survived": "mean"})

df.groupby(["sex", "embark_town"]).agg({
     "age": ["mean"],
     "survived": "mean",
     "sex": "count"})


# Pivot Table

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived", "sex", "embarked", aggfunc="std")

df.pivot_table("survived", "sex", ["embarked", "class"])

df.head()

# sayısalbir değişkeni kategorik bir değişkene çevirirken çevirecek olduğumuz sınıfları tanımlayabiliyoruz.
# Burada çevirirken cut fonksiyonu kullanmalıyız. Ancak tanımlayamazsak qcut fonksiyonu tanımlamalıyız. Çünkü değerleri
# küçükten büyüğe sıralar ve yüzdelik çeyrek değerlerine göre bunları  gruplara kategorilere böler. Çok yaygın bir
# şekilde kullanılır.

df["new_age"] = pd.cut(df["age"],[0, 10, 18, 25, 40, 90])

df.pivot_table("survived", "sex", ["new_age", "class"])
# çıktılar bölük bir şekilde konsolda gözükeceğinden aşağıdaki komutu kullanabiliriz.
pd.set_option('display.width', 500)


# Apply ve Lambda
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
pd.set_option('display.width', 500)
df.head()

# Apply ile satır ya da sütunlarda istediğimiz fonksiyonları uygulayabiliriz.
# Lambda kullan at fonksiyondur

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

# Aşağıda biz bütün age ifadesni içeren değişkenleri 10 bölmek istiyoruz. Bunun için yöntemler

# 1. yöntem
(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

# 2. yöntem
for col in df.columns:
     if "age" in col:
          print((df[col]/10).head())

# 3. yöntem
for col in df.columns:
     if "age" in col:
          df[col] = df[col]/10

df.head()

# 4. yöntem apply & lambda uygulayarak

df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

# YA DA

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

# Başka bir fonksiyon
df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

# Yukarıdaki fonksiyonu bir başka bir deyişle

def standart_scaler(col_name):
     return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# Apply fonksiyonu satırlarda veya sütunlarda elimizdeki belirli bir fonksiyonu bu satır ya da sütunlara uygulama imkanı
# sağlar.Aşağıda bu yaptıklarımızı kalıcı hale getirmiş oluruz.

# df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()
# YA DA
# df.loc[:, ["age", "age2", "age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# Birleştirme (Join) İşlemleri

import numpy as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2","var3"])
df2 = df1 + 99

pd.concat([df1, df2])
# concat fonksiyonu alt alta satırları birleştirme işlemi yapar.
pd.concat([df1, df2], ignore_index=True)
# ilk uyguladığımız komut indeksleri olduğu gibi birleştirince iki data frame-in indeksleri tekrar ettiğinden düzgün bir
# indeksleme olmaz. Bunun için ignore_index=True eklemesi yapıldı ve indeksleme düzeltildi.


# Merge ile Birleştirme İşlemleri

df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': [ 'mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
pd.merge(df1, df2, on="employees")
# on ile neye göre birleştirme işlemi yapacağımızı belirtebiliriz. Yukarıdaki iki çıktıda aynı birleştirmeyi yapar.
# Amaç : Her çalışanın müdürünün bilgisine erişmek istyoruz.

df3 = pd.merge(df1, df2)
df4 = pd.DataFrame({'group':['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})
pd.merge(df3, df4)

