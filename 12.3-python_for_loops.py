#Python For Loops

"""
for dongusu bir koleksiyon(liste, tuple, set, dict vb.) uzerinde yineleme yapmak
icin kullanilir.

Bu, diger programlama dillerindeki for anahtar sozcugune daha az benzer ve diger
nesne yonelimli programlama dillerinde oldugu gibi daha cok yineleyici bir
yontem gibi calisir.

for dongusuyle, bir liste, tuple, set vb. icindeki her oge icin bir kez olmak
uzere bir dizi ifade calistirabiliriz.

fruit listesindeki her meyveyi yazdirma:
"""


fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)


"""
for dongusu onceden ayarlamak icin bir indeksleme degiskeni gerektirmez.
"""

#Looping Through a String

"""
Stringler bile koleksiyon nesneleridir, bir dizi karakter icerirler.

"banana" kelimesindeki harfler arasinda dolasma:
"""

for x in "banana":
    print(x)


#The break Statement

"""
break ifadesi ile tum ogeler arasinda dolasmadan once donguyu sonlandirabiliriz.

x = "banana" oldugunda donguden cikma:
"""

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
    if x == "banana":
        break


"""
x = "banana" oldugunda donguden cikma ancak bu sefer 'break' yazdirmadan once
gelir:
"""
print("\n")

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    
    if x == "banana":
        break
    
    print(x)


#The continue Statement

"""
continue ifadesi ile dongunun mevcut yinelemesini durdurabilir ve bir sonraki
ile devam edebiliriz.

"banana" yi yazma:
"""
print()


fruits = ["apple", "banana", "cherry"]

for x in fruits:

    if x == "banana":
        continue
    print(x)



#The range() Function

"""
Bir kod dizesini belirli bir sayida yurutmek icin range() islevini 
kullanabiliriz.

range() fonksiyonu, varsayilan olarak 0' dan baslayan ve 1 artan bir sayi dizisi
dondurur ve belirtilen bir sayida biter.

range() fonksiyonunu kullanma:
"""

for x in range(6):
    print(x)


"""
range(6)' nin 0 ila 6 arasindaki degerler degil, 0 ila 5 arasindaki degerler
olduguna dikkat edin.

range() fonksiyonu baslangic degeri varsayilan olarak 0' dir, ancak bir
parametre ekleyerek baslangic degerini belirtmek mumkundur: range(2, 6), bu da
2 ila 6 arasindaki degerler anlamina gelir(ancak 6 dahil degildir.)

Baslangic parametresini kullanma:
"""
print("\n")


for x in range(2, 6):
    print(x)


"""
range() fonksiyonunun varsayilan artis degeri 1' dir, ancak artis degerini
ucuncu bir parametre ekleyerek belirtmek mumkundur: range(2, 30, 3).

Artisi 3 yapma(varsayilan 1' dir):
"""
print("\nIncrement")


for x in range(2, 30, 3):
    print(x)


#Else in For Loop

"""
Bir for dongusundeki else anahtar sozcugu, dongu bittiginde yurutulecek bir kod
blogunu belirtir.

0'dan 5'e kadar olan tum sayilari yazdirin ve dongu sona erdiginde bir mesaj
yazdirin:
"""

for x in range(6):
    print(x)
else:
    print("Finally finished!")

"""
Not: Dongu bir 'break' ifadesi tarafindan durdurulursa, 'else' blogu
UYGULANMAYACAKTIR.

x = 3 oldugunda donguyu kirin ve 'else' bloguna ne oldugunu gorun:
"""
print("\nbreak")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")  


#Nested Loops

"""
Icicie bir dongu, bir dongu icerisindeki bir dongudur.

'ic dongu(inner loop)', 'dis dongunun(outer loop)' her yinelemesi bir kez
yurutulur.

Her bir meyve icin her sifati yazdirma:
"""

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]


for x in adj:
    for y in fruits:
        print(x, y)



#The pass Statement

"""
for donguleri bos olamaz, ancak herhangi bir nedenle icerigi olmayan bir for 
dongusune sahipseniz, hata almamak icin pass ifadesini girin.
"""

for x in [0, 1, 2]:
    pass