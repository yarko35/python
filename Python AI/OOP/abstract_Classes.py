#soyut klaslar
#super class ve sub class(child)
#super class sub class için gereken sınıfları soyut olarka tutar

#abstract base class demektir
from abc import ABC, abstractmethod

class animal(ABC):#super class
    @abstractmethod
    def walk(self):pass
    @abstractmethod
    def run(self):pass
    #abstract sınıfta kullanılan bir method sub classda kullanılmak ZORUNDAdır.

    #artık animal classı abstract bir sınıf olmuş oluyor
class bird(animal):#sub class
    def __init__(self):
        print("bird")
    def walk(self):
        print("Kuşlar aynı zamanda yürür")
    
    def run(self):
        print("Kuşlar koşamaz.")


#Temel Kurallar
#Eğer bir abstract sınıf oluşturduysak ve bunun bir child ı varsa abstract sınıf içerisinde yer alan methodlar child da da olmak zorundadır
# abc import ettikten sonra object kısmına ABC diye geçilmelidir aksi takdirde hala daha abstract sınıf olduğu anlaşılmaz sistem tarafından.
#sınıf içerisindeki her methodun(fonksiyonun) başına  @abstractmethod diye eklenmelidir.
#Abstract kullanılma sebebi bir şablon yaratmaktır sanki bir yorum satırı açmış gibi içerisine barınmasını istediğimiz methodları gireriz. 
#Abstract bir sınıftaki methodda sadece bir tane  @abstractmethod olması yeterlidir ama hangi methodun başında  @abstractmethod varsa o methodu kullanmayı zorunlu kılar.
#Eğer ki run methodunun başındaki  @abstractmethod ı kaldırırsak run methodunun sub classtaki kullanılma zorunluluğu kalkmış olur
