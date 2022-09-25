#Access List Items

#Access Items

"""
Liste ogeleri indexlenir ve bunlara indeks numarasina bakarak erisebilirsiniz.

Not: ilk oge'nin indexi 0' dir.

Listenin ikinci elemanini yazdirma:
"""

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative Indexing

"""
Negatif indexleme sondan baslama anlamina gelir;
-1 son ogeyi, -2 sondan 2. ogeyi vb. ifade eder.
"""

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


#Range of Indexes

"""
Bir aralik(range) belirterek, hangi ogeden baslayip hangi ogeye kadar devam
edecegini belirleyebilirsiniz.

Bir aralik belirtirken, donus degeri, belirtilen ogeleri iceren yeni bir liste
olacaktir.

Ucuncu, dorduncu ve besinci ogeleri dondurme:
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


"""
Not: Arama dizin 2'de(dahil) baslayacak ve dizin 5'te(dahil degil) bitecektir.

Ilk ogenin indexinin 0 oldugunu unutmayin.

Baslangic degeri girilmezse, aralik ilk ogeden baslayacaktir.

Asagidaki ornek ogeleri bastan bitis degerinde kadar dondurur, "kiwi" dahil
degildir:
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


"""
Bitis degeri girilmezse, aralik listenin sonuna kadar gider.

Asagidaki ornek "cherry" den baslayarak son ogeye kadar bir liste dondurur.
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


#Range of Negative Indexes

"""
Aramaya listenin sonundan baslamak istiyorsaniz, negatif index
belirtebilirsiniz.

Asagidaki ornek "orange"(-4) dan "mango"(-1)(dahil degil) ya kadar olan 
ogeleri dondurur:
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


#Check if Item Exists

"""
Listede belirtilen bir ogenin olup olmadigini belirlemek icin 'in' anahtar
sozcugunu kullanin.

Listede "apple" olup olmadigini kontrol etme:
"""

thislist = ["apple", "banana", "cherry"]

if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
