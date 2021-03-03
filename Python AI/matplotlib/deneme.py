# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:56:14 2021

@author: yarki
"""
# %% Pandas Review
import pandas as pd
#df= pd.read_csv("iris.csv")#eğer aynı yerde değilse dosya yolu kopyala yapıştır
print(df.Species.unique())#alt başlıklarını gösterir
print(df.info)
df.describe()#ortalamaları alır
setosa=df[df.Species == "Iris-setosa"]#sadece setosaları ayırır
versiColor=df[df.Species == "Iris-versicolor"]#sadece versicolor ayırır
print(setosa.describe())
print(versiColor.describe())
# %% Line Plot(Çizgi Grafiği)
import matplotlib.pyplot as plt
df1=df.drop(["Id"],axis=1)#sütundaki tüm değerleri çıkarır ve yeni dataframe oluşturur
df1.plot()#görselleştirme kullanılır.Komut ekranındaki 
#***************************ilk grafik
plt.show()#tüm grafiği gösterir (oluşturulan grafiği açar da diyebiliriz)

setosa=df[df.Species == "Iris-setosa"]#sadece setosaları ayırır
versiColor=df[df.Species == "Iris-versicolor"]#sadece versicolor ayırır
virginica=df[df.Species == "Iris-virginica"]#sadece virginicayı ayırır
#----------------------------------------ilk girilen x ekseni ikinci girilen y eksenini ifade eder-----------------
#**************************ikinci grafik
plt.plot(setosa.Id,setosa.PetalLengthCm, color="red",label="setosa - PetalLengthCm")#setosa için özelleştirmeler yapıyoruz
plt.plot(versiColor.Id,versiColor.PetalLengthCm, color="green",label="setosa - PetalLengthCm")#versiColor için özelleştirmeler yapıyoruz
plt.plot(virginica.Id,virginica.PetalLengthCm, color="blue",label="setosa - PetalLengthCm")#virginica için özelleştiremeler yapıyoruz
plt.xlabel("Id")#x ekseni için isim veriyoruz
plt.ylabel("PetalLengthCm")#y ekseni için isim veriyoruz
plt.show()#çizdirdiğimiz grafiği gösterme komutu
# ----------------------------------------------------------grid ve lineStyle gösterme-----------------------------------
#*************************Üçüncü grafik
df1.plot(grid= True,linestyle = ":")#line : şeklinde çizdirilmiş olur 
plt.show()
#----------------------------------------------------------alpha kullanımı----------------------
#************************Dördüncü grafik 
df1.plot(grid= True,linestyle = ":",alpha=0.5)#saydamlığı ayarlamak için kullanılır 0 yaklaştıkça saydamlık artar
plt.show()
# %% Scatter Plot(Noktasal Grafik)
# 2 tane özelliği karşılaştırma için kullanılır daha çok 
#************************Beşinci Grafik
import matplotlib.pyplot as plt
setosa=df[df.Species == "Iris-setosa"]#sadece setosaları ayırır
versiColor=df[df.Species == "Iris-versicolor"]#sadece versicolor ayırır
virginica=df[df.Species == "Iris-virginica"]#sadece virginicayı ayırır
plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="red",label="setosa")
plt.scatter(versiColor.PetalLengthCm,versiColor.PetalWidthCm,color="blue",label="versiColor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="green",label="virginica")
plt.xlabel("PetalLentghCm")
plt.ylabel("PetalWidthCm")
plt.title("Scatter Plot")
plt.show()
#%% Histogram Grafik
plt.hist(setosa.PetalLengthCm,bins= 50)#bins histogram çubuklarının kalınlığıdır
plt.xlabel("PetalLengthCm values")
plt.ylabel("Frekans")
plt.title("Hist Grafiği")
plt.show()
#%% Bar Plot(bar şeklinde grafik)
#ülkelerin gelir dağılımlarını düşünelim 
import numpy as np 
x=np.array([1,2,3,4,5,6])
y=x*2+5
plt.bar(x,y)
plt.title("Bar Grafiği")
plt.xlabel("Array değerleri")
plt.ylabel("Denklem Değerleri")
plt.show()
#barda hangi sırayla yazdıysam label değerleride ona göre gelir unutma 
#%% Subplots 
#çubuk grafiğin aynısını farklı farklı çizgilerle çizdirmek demek 

df1.plot(grid=True,alpha=0.9,subplots=True)
setosa=df[df.Species == "Iris-setosa"]#sadece setosaları ayırır
versiColor=df[df.Species == "Iris-versicolor"]#sadece versicolor ayırır
virginica=df[df.Species == "Iris-virginica"]#sadece virginicayı ayırır
#----------------------birinci grafik********************************
plt.subplot(2,1,1)#sondaki 1 birinci grafiğim anlamına gelir

plt.plot(setosa.Id,setosa.PetalLengthCm, color="red",label="setosa - PetalLengthCm")#setosa için özelleştirmeler
plt.ylabel("setosa-PetalLengthCm")
#---------------------birinci grafik bitiş***************************
#--------------------------------------------ikinci grafik*****************
plt.subplot(2,1,2)#sondaki 2 ikinci grafiğim anlamına gelir
plt.plot(versiColor.Id,versiColor.PetalLengthCm, color="green",label="setosa - PetalLengthCm")#versiColor için
plt.ylabel("versicolor-PetalLengthCm")
#--------------------------------------------ikinci grafik bitiş **********




































