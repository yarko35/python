# ! türkçesi çok şekillilik demektir. 

class employee:
    
    def zam(self):
        zam_orani= 0.1
        return 100+100*zam_orani

class bilgisayarmüh(employee):
    def zam(self):
        zam_orani=0.2
        return 100+100*zam_orani

class elektrikmuhendis(employee):
    def zam(self):
        zam_orani=0.5
        return 100+100*zam_orani

#hoca aslında daha önceki örnekleri yaparken bunu anlatmış oltu farklı birşey yok 
# biz return kullandığımız için ekranda gözükmeyecektir hesaplandığı şekilde kalacaktır otomatik olarak kullanıcıya göstermek istersek sonuç için bir variable oluşturup onu printleyebiliriz.