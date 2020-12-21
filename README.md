# Python Notlarım
## While
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
## Mantıksal Bağlaçlar
- and operatörü:Satır bitene kadar inceler false çıktığı an false yazar false değilse true değer döndürür

- or operatörü: bütün işlemlerin sonucu false ise false döndürür aksi takdirde hep true döndürür.

- not operatörü: bir işlemin sonucunu true ise false, false ise true yapar


## For
- in operatörü: bir değerin başka birdeğer içerisinde var olup olmadığını kontrol etmemize yarar.
	```python
	"a" in "merhaba"
	#true veya false değer döndürür.
	```
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
###Format metoduyla yazım şekli
```python
	toplam=0
	liste=[1,2,3,4,5]
	for eleman in liste:
	    toplam=toplam+eleman
	    print("Toplamları:{} Elemanlar:{}" .format(toplam,eleman))
	    #her döngüde toplamları yazar
```
- kalan bulma operatör=> x%y
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

```python
	 liste=[(1,2),(3,4),(35,20)]
	#iç içe for yaparakta yazılabilir.
	for i,j in liste
	    print("Sayılarınız i:{} j:{}".format(i,j))
```
## Dict
```python
	 #sözlüklerde okuma nasıl yapılır
	#tırnak içindekiler anahtar-keys
	#diğer tarafı values olarak geçer
	sözlük={"oğuz":16,"yarkın":35,"emirhan":10,"sude":10}
```
## İf Elif Else blokları


```python
	a==2
	if(3<a):
		print("sonuc yanlis {}".format(a))
	elif(3>a):
		print("sonucunuz dogru{}".format(a))
	else:
		print("farklı deger veriniz")

```







