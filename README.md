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


