#Sort Lists

#Sort List Alphanumerically

"""
List nesnelerinin, listeyi alfanumerik olarak siralayacak bir 'sort()' metodu
vardir, siralama varsayilan olarak artan cinstendir.

Listeyi alfabetik olarak siralama:
"""

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


"""
Listeyi sayisal olarak siralama:
"""

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


#Sort Descending

"""
Azalan siralama icin 'reverse = True' keyword argumanini kullanin.

Listeyi azalan sekilde siralama:
"""

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


"""
Listeyi sayisal olarak azalan sekilde siralama:
"""

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#Customize Sort Function

"""
Ayrica 'key = function' keywordunu kullanarak kendi fonksiyonunuz ile siralama
yi ozellestirebilirsiniz.

Fonksiyon listeyi siralamak icin bir sayi dondurur.(Once en dusuk sayi).

Sayinin 50' ye ne kadar yakin olduguna gore listeyi siralama:
"""

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


#Case Insensitive Sort

"""
Varsayilan olarak 'sort()' metodu buyuk/kucuk harflere duyarlidir. Bu da tum
buyuk harflerin kucuk harflerden once siralanmasina sebep olur.

Buyuk/kucuk harfe duyarli siralama beklenmedik bir sonuc verebilir:
"""

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


"""
Neyse ki bir listeyi siralarken built-in(yerlesik) fonksiyonlari 'key'
fonksiyonu olarak kullanabiliriz.

Yani, buyuk/kucuk harfe duyarsiz bir siralama istiyorsaniz, 'key' fonksiyonu
olarak 'str.lower' fonksiyonunu kullanabilirsiniz.

Listeyi buyuk/kucuk harfe duyarli olmadan siralama:
"""

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


#Reverse Order

"""
Alfabeden bagimsiz olarak bir listenin sirasini tersine cevirmek isterseniz
ne olur?

'reverse()' metodu, ogelerin gecerli siralamasini tersine cevirir.

Listenin ogelerinin sirasini tersine cevirme:
"""

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
