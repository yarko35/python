#parent
class animal:

    def __init__(self):
        print("Animal is created.")
    
    def toString(self):
        print("Animal")
    def walk(self):
        print("Hayvanlar yürür")
#Maymun classı
class monkey(animal): #monkey classım animal classımdan türemiştir demiş oluyorum 

    def __init__(self):
        super().__init__() #parent classının init özelliklerini alıyor buraya aktarıyor
        print("monkey is created")
    def toString(self):
        print("monkey")
    def climb(self):
        print("maymunlar tırmanabilir")
#Kuş classsı
class birds(animal):
    def __init__(self):
        super().__init__()
    def ucar(self):
        print("Kuşlar uçabilir")
    def kanat(self):
        print("Kuşların 2 tane kanadı vardır.")
    def gaga(self):
        print("Kuşların gagası vardır")
maymun1=monkey()
maymun1.toString()
maymun1.walk()#normalde monkeyde animal yazmasaydı animal classındaki walk ı kullanamayacaktı 

eagle=birds()
eagle.gaga()