# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:56:14 2021

@author: yarki
"""

import pandas as pd
dataFrame= pd.read_csv("iris.csv")#eğer aynı yerde değilse dosya yolu kopyala yapıştır
print(dataFrame.Columns)
print(dataFrame.Species.unique())#alt başlıklarını gösterir

print(dataFrame.info)
dataFrame.describe()#ortalamaları alır
setosa=dataFrame[dataFrame.Species==["İris-setosa"]]#sadece setosaları ayırır
versiColor=dataFrame[dataFrame.Species==["İris-versicolor"]]#sadece versicolor ayırır
print(setosa.describe())
print(versiColor.describe())