#Python Tuples

"""
Tuple bircok ogeyi tek bir degiskende saklamak icin kullanilir.

Tuple Python'da veri koleksiyonlarini depolamak icin kullanilan 4 built-in
(yerlesik) veri turunden biridir, diger 3'u list, set ve dictionary'dir ve
tumu farkli niteliklere ve kullanima sahiptir.

Tuple sirali ve 'degistirilemez' bir koleksiyondur.

Tuple yuvarlak parantez ile yazilir.

Bir tuple olusturma:
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple)


#Tuple Items

"""
Tuple ogeleri, siralanir, degistirilemez ve yinelenen degerlere izin verir.

Tuple ogeleri indexlidir, ilk ogenin index'i [0], ikinci ogenin index'i [1] vb.
"""

#Ordered

"""
Tuple'lar siralidir dedigimizde, ogelerin belirli bir siraya sahip oldugu ve bu 
siranin degismeyecegi anlamina gelir.
"""

#Unchageable

"""
Tuple'lar degistirilemez, yani tuple olusturulduktan sonra ogeleri degistiremez,
ekleyemez veya cikaramayiz.
"""

#Allow Duplicates

"""
Tuple'lar indexlendiginden, ayni degere sahip ogelere sahip olabilirler.

Ayni degerlere sahip tuple:
"""

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


#Tuple Length

"""
Bir tuple'in kac ogeye sahip oldugunu belirlemek icin 'len()' fonksiyonunu
kullanin.

Tuple ogelerinin sayisini yazdirma:
"""

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#Create Tuple With One Item

"""
Sadece bir oge iceren bir tuple olusturmak icin ogeden sonra bir vigul
eklemeniz gerekir, aksi takdirde Python onu bir tuple olarak tanimaz.

Bir ogeli tuple, virgulu unutmayin:
"""

thistuple = ("apple", )
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#Tuple Items - Data Types

"""
Tuple ogeleri herhangi bir veri tipi olabilir.

String, int ve boolean veri tipleri:
"""

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

"""
Bir tuple farkli veri tipleri icerebilir.

String, int ve boolean degerleri iceren tuple:
"""

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)


#type()

"""
Python'un bakis acisindan tuple'lar 'tuple' sinifina ait nesnelerdir.

Bir tuple' in veri turu nedir?
"""

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


#The Tuple Consructor

"""
Bir tuple olusturmak icin tuple kurucusunu kullanmak da mumkundur.

tuple() metodunu kullanarak tuple olusturma:
"""

thistuple = tuple(("apple", "banana", "cherry")) # iki parantez olmali
print(thistuple)
