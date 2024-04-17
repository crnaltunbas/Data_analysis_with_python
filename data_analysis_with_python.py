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
