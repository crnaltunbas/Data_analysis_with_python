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
df.drop(delete_indexes, axis=0).head(10)
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