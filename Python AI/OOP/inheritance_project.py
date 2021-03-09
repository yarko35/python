# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:56:14 2021

@author: yarki
"""

class webstie:
    #initilaizer atamalarını yaptık
    def __init__(self,name,surname,mail):
        self.name=name
        self.surname=surname
        self.mail=mail
    #kullanıcılara gerekli bilgileri göstermek için 
    def logInfo(self):
        print("Kullanıcının adı ve soyadı {} {}".format(self.name,self.surname))
class websitesiKisisel(webstie):
    #temel oluşturudğumuz website daki name ve surname i çektik sadece
    def __init__(self,name,surname,ids):
        webstie.__init__(self,name,surname)
        self.ids=ids#yeni bir atama yaptık 
    def login(self):
        print(self.name+" "+self.surname+" "+self.ids)
#bu classda da isim ve maili kullandım sadece ek olarak telefon numarası ekledim
class websiteMail(webstie):
    def __init__(self, name,mail,phoneNumber):
        webstie.__init__(self,name,mail)
        self.phoneNumber=phoneNumber
    def info_mail(self):
        print(self.name,self.mail,self.phoneNumber)


