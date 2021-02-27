# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 08:10:14 2021

@author: yarki
"""

#%% Classes


kole="Ege"
koleninYası=22
koleninadresi="Her zaman benim yanım kardeş"

class kole(object):
    #attribute=kolemizin özellikleri,yaş,adres,isim gibi
    #behaviour=davranışları
    pass#ileride kole sınıfımı doldurucam diye programa söylemiş oluyorum 
    
#Class içerisi dışarısı kavramlarını unutma
#aksi takdirde IndentationError hatasını alabilirsin.(fazla boşluk bırakma)
koleyaratma= kole()#kölemizi yaratmış oluyoruz böylelikle
#%% attribute
class footballer(object):
    soccerTeam="Besiktas"
    age=30
playerOne=footballer()
#----------------------------class içerisinden veri çekme------------------
ageofplayer=playerOne.age
print(ageofplayer)
#----------------------------attribute değiştirme------------------
playerOne.soccerTeam="Porto FC"
print(playerOne.soccerTeam)
#%% methods

class square(object):
    edge=5
    def area(self):
        area=self.edge*self.edge
        print("Your square area point is {}.".format(area))
heyhey=square()
print(heyhey.area())