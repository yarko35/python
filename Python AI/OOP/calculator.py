# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 05:39:33 2021

@author: yarki
"""
class calc(object):
    
    def __init__(self,numberone,numbertwo):
        self.numberone=numberone
        self.numbertwo=numbertwo
    #toplama fonksiyonu
    def add(self):
        return self.numberone + self.numbertwo
    #çıkarma fonksiyonu 
    def minus(self):
        return self.numberone - self.numbertwo
    #çarpma fonksiyonu
    def multiply(self):
        return self.numberone * self.numbertwo
    #bölme fonksiyonu 
    def bolme (self):
        return self.numberone / self.numbertwo
    
#kullanıcıdan değerleri isteme ekranı
numOne=int(input("Büyük sayıyı giriniz:"))
numTwo=int(input("Küçük sayıyı giriniz: "))
#alınan değerleri class içerisindeki fonksiyonlara yollama
getClasss=calc(numOne, numTwo)
#kullanıcıya bilgi verdirme ekranı
print("\nToplama işleminizin sonucu {}".format(getClasss.add()))
print("Çıkarma işleminizin sonucu {}".format(getClasss.minus()))
print("Çarpma işleminizin sonucu {}".format(getClasss.multiply()))
print("Bölme işleminizin sonucu {}".format(getClasss.bolme()))

#type() ile string mi integer mı double mı class mı nedir ne değildir öğrenmek için kullanıyoruz

