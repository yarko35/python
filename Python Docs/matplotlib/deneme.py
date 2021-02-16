# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:56:14 2021

@author: yarki
"""
# %%
import pandas as pd
df= pd.read_csv("iris.csv")#eğer aynı yerde değilse dosya yolu kopyala yapıştır
print(df.columns())
print(df.Species.unique())#alt başlıklarını gösterir
print(df.info)
df.describe()#ortalamaları alır
setosa=df[df.Species == "Iris-setosa"]#sadece setosaları ayırır
versiColor=df[df.Species == "Iris-versicolor"]#sadece versicolor ayırır
print(setosa.describe())
print(versiColor.describe())
# %%
import matplotlib.pyplot as plt
df1=df.drop(["Id"],axis=1)#sütundaki tüm değerleri çıkarır ve yeni dataframe oluşturur
df1.plot()#görselleştirme kullanılır
plt.show()#tüm grafiği gösterir (oluşturulan grafiği açar da diyebiliriz)

setosa=df[df.Species == "Iris-setosa"]#sadece setosaları ayırır
versiColor=df[df.Species == "Iris-versicolor"]#sadece versicolor ayırır
virginica=df[df.Species == "Iris-virginica"]#sadece virginicayı ayırır
#----------------------------------------ilk girilen x ekseni ikinci girilen y eksenini ifade eder-----------------
plt.plot(setosa.Id,setosa.PetalLengthCm, color="red",label="setosa - PetalLengthCm")#setosa için özelleştirmeler yapıyoruz
plt.plot(versiColor.Id,versiColor.PetalLengthCm, color="green",label="setosa - PetalLengthCm")#versiColor için özelleştirmeler yapıyoruz
plt.plot(virginica.Id,virginica.PetalLengthCm, color="blue",label="setosa - PetalLengthCm")#virginica için özelleştiremeler yapıyoruz
plt.xlabel("Id")#x ekseni için isim veriyoruz
plt.ylabel("PetalLengthCm")#y ekseni için isim veriyoruz
plt.show()#çizdirdiğimiz grafiği gösterme komutu
# ----------------------------------------------------------grid ve lineStyle gösterme-----------------------------------
df1.plot(grid= True,linestyle = ":")#line : şeklinde çizdirilmiş olur 
plt.show()
#----------------------------------------------------------alpha kullanımı
df1.plot(grid= True,linestyle = ":",alpha=0.5)#saydamlığı ayarlamak için kullanılır 0 yaklaştıkça saydamlık artar
plt.show()