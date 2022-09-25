#Access Tuple Items

"""
Tuple ogelerine, koseli parantez icerisindeki index numarasina basvurarak
ulasabilirsiniz.

Tuple'in ikinci ogesini yazdirma:
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

"""
Not: ILk ogenin index'i 0'dir.
"""


#Negative Indexing

"""
Negatif indexleme, sondan baslama anlamina gelir.

-1 son ogeyi, -2 sondan ikinci ogeyi vb. temsil eder.

Tuple'in son ogesini yazdirma:
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


#Range of Indexes

"""
Araligin nereden baslayacagini ve nerede bitecegini belirterek bir index
araligi belirtebilirsiniz.

Bir aralik belirttiginizde, donus degeri belirtilmis araliklarla yeni bir
tuple olacaktir.

Ucuncu, dorduncu ve besinci ogeleri dondurme:
"""

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

"""
Not: Aralik index 2'de(dahil) baslayacak index 5'te(dahil degil) sona erecektir.

Ilk ogenin indexinin 0 oldugunu unutmayin.
"""

"""
Baslangic degeri belirtilmezse aralik ilk ogeden baslayacaktir.

Asagidaki belirtilen aralik ogeleri bastan kiwi'ye(dahil degil) kadar dondurur:
"""

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


"""
Bitis degeri belirtilmezse aralik listenin sonuna kadar devam eder.

Asagidaki ornek "cherry" den baslayarak tuple' in sonuna kadar devam eder:
"""

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


#Range of Negative Indexes

"""
Aramaya tuple' in sonundan baslamak istiyorsaniz negatif index
belirtebilirsiniz.

Asagidaki ornek index -4(dahil)' den index  -1'e(haric) olan ogeleri dondurur:
"""

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


#Check if Item Exists

"""
Bir tuple'da belirli bir ogenin olup olamadigini kontol etmek icin 'in'
anahtar sozcugunu kullanin.

Tuple' da "apple" olup olmadigini kontrol etme:
"""

thistuple = ("apple", "banana", "cherry")

if "apple" in thistuple:
    print("Yes, apple is in the fruits tuple")
