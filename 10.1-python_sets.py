#Python Sets

#Set

"""
Set bircok ogeyi tek bir degiskende saklamak icin kullanilir.

Set, Python' da veri koleksiyonlarini depolamak icin kullanilan 4 build-in
(yerlesik) veri turunden biridir. Diger 3' u list, tuple ve dictionary' dir ve
tumu farkli niteliklere ve kullanima sahiptir.

Set, siralanmamis, degistirilemez*, ve indexlenmemis bir koleksiyondur.

Not*: Set ogeleri degistirilemez ama yeni ogeler eklenip, cikarilabilir.

Set kivircik parantezler({}) arasina yazilir.

Bir Set Olustruma:
"""

thisset = {"apple", "banana", "cherry"}
print(thisset)


"""
Not: Set' ler sirasiz oldugundan ogelerin hangi sirayla goruneceginden emin
olamazsiniz.
"""

#Set Items

"""
Set ogeleri sirasiz, degistirilemez ve yinelenen degerlere izin vermez.
"""


#Unordered

"""
Unordered, bir Set' deki ogelerin tanimlanmis bir siraya sahip olmadigi anlamina
gelir.

Set ogeleri, onlari her kullandiginizda farkli bir sirada gorunebilir ve index
veya key ile referans alinamaz.
"""


#Unchangeable

"""
Set ogeleri degistirilemez yani Set olusturuldukdan sonra ogeleri 
degistiremeyiz.

Bir Set olusturulduktan sonra ogelerini degistiremezsiniz, ancak ogeleri
kaldirabilir ve yeni ogeler ekleyebilirsiniz.
"""


#Duplicates Not Allowed

"""
Set' ler ayni degere sahip iki ogeye sahip olamaz.

Yinelenen degerler yok sayilir:
"""

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


#Get the Length of a Set

"""
Bir Set' in kac ogeye sahip oldugunu belirlemek icin 'len()' fonksiyonunu
kullanabilirsiniz.

Bir Set' deki ogelerin sayisi:
"""

thisset = {"apple", "banana", "cherry"}
print(len(thisset))


#Set Items - Data Types

"""
Set ogeleri herhangi bir veri tipi olabilir.

String, int ve boolean veri tipleri:
"""

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

"""
Bir set farkli veri turleri icerebilir.

Stringler, Integerlar ve boole degerler iceren bir Set:
"""

set1 = {"abc", 34, True, 40, "male"}


#type()

"""
Python' un bakis acisindan Set' ler 'set' veri tipine sahip nesneler olarak
tanimlanir.

Bir Set' in veri tipi nedir?
"""

myset = {"apple", "banana", "cherry"}
print(type(myset))


#The set() Constructor

"""
Bir Set olusturmak icin set() yapicisini kullanmak da mumkundur.

set() kurucusunu kullanarak Set olusturma:
"""

thisset = set(("apple", "banana", "cherry")) # iki parantez icinde olmali
print(thisset)
