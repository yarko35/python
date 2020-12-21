# *****************Python Notlarım*****************
## _While_
- for döngülerinde yapcaklarımız while döngüsünde de yapabiliriz.Sadece bazı noktalarda for döngüleri daha avantajlı oluyor
```python
		i=0
		while(i<10)
		    print("i nin degeri: {}".format(i))
		    i +=1
```
- İsmi 3 kere yazdırma
```python
		a=0
		while(a<=3)
			print("yarkoZe35")
			a+=1
```
 
- for da yaptığımız okumaları while ile de yapabiliriz
```python
		liste=[1,2,3,4,5]
		index=0
		while(index<len(liste))
			print("Hangi index:{},Liste:{}".format(index,liste[index]))
			index +=1
```
## _Mantıksal Bağlaçlar_
- _**and operatörü**_:Satır bitene kadar inceler false çıktığı an false yazar false değilse true değer döndürür

- _**or operatörü**_: bütün işlemlerin sonucu false ise false döndürür aksi takdirde hep true döndürür.

- _**not operatörü**_: bir işlemin sonucunu true ise false, false ise true yapar


## _For_

-for elemanlar üzerinde gezinmemize yarar

-for eleman in liste dediğimiz zaman eleman gezineceğimiz değişkendeki her elemena eşit olmuş oluyor
```python
	liste=[1,2,3,4,5]
	for i in liste:
	    print("Eleman",eleman)
	#her elemanı alt alta yazdırmış oluyoruz liste bitene kadar çalışmış oluyor.


```
```python
	toplam=0
	liste=[1,2,3,4,5]
	for eleman in liste:
	    toplam=toplam+eleman
	    print("Toplamları:",toplam)#her döngüde toplamları yazar
	print("Toplamları:",toplam)#döngü bitince toplamlarını yazar

```
```python
	 liste=[(1,2),(3,4),(35,20)]
	#iç içe for yaparakta yazılabilir.
	for i,j in liste
	    print("Sayılarınız i:{} j:{}".format(i,j))
```



## _Dict_
```python
	 #sözlüklerde okuma nasıl yapılır
	#tırnak içindekiler anahtar-keys
	#diğer tarafı values olarak geçer
	sözlük={"oğuz":16,"yarkın":35,"emirhan":10,"sude":10}
```
## _İf Elif Else blokları_


```python
	a==2
	if(3<a):
		print("sonuc yanlis {}".format(a))
	elif(3>a):
		print("sonucunuz dogru{}".format(a))
	else:
		print("farklı deger veriniz")

```
## _Parametre,Metod ve Operatörler_
### range() parametresi
- istediğimiz oranları  belirterek sayı dizisi oluşturu range kelime olarak aralık anlamına gelir.
```python
	    range(0,20)
	    print(*range(0,20))
	#sayılarım 0 dan 20 e 2 atlayarak gitsin demiş oluyorum
	    print(*range(0,20,2))
	#20 den sıfıra kadar 1 atlayarak git demiş oluyorum
	    print(*range(20,0,-1))
	#1den 100 e kadar olan sayıları range ve for kullanarak yazdırma
	    for i in range(1,101):
		print(i)
	#binom mantığıyla yıldız bastırma
	    for i in range(1,10):
		print("*"* i)
```
### .format() parametresi
```python
	toplam=0
	liste=[1,2,3,4,5]
	for eleman in liste:
	    toplam=toplam+eleman
	    print("Toplamları:{} Elemanlar:{}" .format(toplam,eleman))
	    #her döngüde toplamları yazar
```
### Kalan bulma operatörü
- x%y
### in operatörü
- *in operatörü: bir değerin başka birdeğer içerisinde var olup olmadığını kontrol etmemize yarar.
	```python
	"a" in "merhaba"
	#true veya false değer döndürür.
	```
## _Basit Örnekler_
### Bir sayının tek mi çift mi olduğunu bulma
```python
	liste=[34,17,23,68]
	for eleman in liste
	    if(eleman % 2 ==0)
		print("Sayınız({}) çift bir sayıdır.".format(eleman))
	    else:
		print("Sayınız({})çift bir sayı değildir.".format(eleman))
		break
```








