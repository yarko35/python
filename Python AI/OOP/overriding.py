#Geçersiz kılma olarak adlandırılır

class animal:
    def toString(self):
        print("animal")
    
class monkey(animal):
    def toString(self):
        print("monkey classes")

#iki sınıfta da aynı isimle fonksiyon var şayet biz monkey deki toStringi çağırırsak bize çıktı olarak monkey nin toStringini verir animaldaki toStringi geçersiz kılar
#monkey nin toString methodu animalın toString methodunu override etti diyebiliriz.
