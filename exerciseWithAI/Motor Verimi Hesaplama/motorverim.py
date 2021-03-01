# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 14:12:55 2021

@author: yarki
"""
import matplotlib.pyplot as plt
while True :
    #Æ***************************************fonksiyon********************
    def kenergy(x,y):
        kinetikenergy=0.5*x*(y^2)
        return kinetikenergy
    #--------------------------kullanıcı ekranı ekle--------------
    islem=input("Yapmak istediğiniz işlemi seçiniz: \n 1.Harcanan benzin miktarı nedir? \n 2.Tekerleklere ne kadar güç aktarılıyor ?\n Çıkmak için q 'a basınız. ")
    #-------------------------- sabitler -------------------------
    verimlilik: 0.18
    galonbenzin=1.3*(10^8)
    gücPayda=3.6*(10^3)
    #--------------------if döngüleri-------------
    if islem=="1":
        i=0
        while i<4:
            i +=1
            carWeight=int(input("Arabanızın ağırlığını giriniz(kg):"))
            hız=int(input("Aracın son hızını giriniz(m/s):"))
            galonwithenergy=kenergy(carWeight,hız)
            galonHesabi=galonwithenergy/(2.3*(10^7))
            print("Aracı kullanabilmek için gereken galon miktarı {} dır.".format(galonHesabi))
            plt.bar(hız,galonHesabi)
            plt.xlabel("Taşıtın hızı(m/s)")
            plt.ylabel("Harcanan yakıt(ga)")
            plt.title("Hız/yakıt")
        break
    elif islem=='2':
        i=0
        while i<4:
            i +=1
            carWeight=int(input("Arabanızın ağırlığını giriniz(kg):"))
            hız=int(input("Aracın son hızını giriniz:"))
            galonwithenergy=kenergy(carWeight,hız)
            galonHesabi=galonwithenergy/(2.3*(10^7))
            power=(galonHesabi*galonbenzin)/gücPayda*(0.18)
            print("Tekerleklere aktarilan gücç {} kw dır.".format(power))
            plt.bar(hız,power)
            plt.xlabel("Taşıtın hızı(m/s)")
            plt.ylabel("Güç(kW)")
            plt.title("Hız/yakıt")
        break
    elif islem=='q':
        print("Tekerine taş değmesin")
        break
        
    
