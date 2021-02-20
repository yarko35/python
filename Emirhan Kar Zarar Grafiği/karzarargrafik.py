# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:56:14 2021

@author: yarki
"""
#%%-----------------------Bulut Teknoloji Company--------------------
import pandas as pd 
import matplotlib.pyplot as plt
dataframe=pd.read_csv("karZarar.csv")
hamdataframe=dataframe.rename(columns={'BULUT TEKNOLOJİ':'Ürünler','Unnamed: 10':'Kar','Unnamed: 1': 'Ürün Açıklaması','Unnamed: 2': 'Ürün Adedi',
                                       'Unnamed: 3':'Alış Fiyatı','Unnamed: 5':'Tl Bazında Fiyat','Unnamed: 8':'KDVLİ fiyat','Unnamed: 9':'Satış Fiyatı'})

hamdataframe=hamdataframe.drop(["Unnamed: 11","Unnamed: 7","Unnamed: 6"],axis=1)
hamdataframe=hamdataframe.drop(hamdataframe.index[0])
urunler=hamdataframe["Ürünler"]
urunaciklama=hamdataframe["Ürün Açıklaması"]
kar=hamdataframe["Kar"]
dtframe=pd.concat([urunler,urunaciklama,kar],axis=1)

