#Loop Tuples

#Loop Through a Tuple

"""
Bir 'for' dongusu kullanarak tuple ogeleri arasinda dolasabilirsiniz.

Ogeleri yineleyip degerleri yazdirma:
"""

thistuple = ("apple", "banana", "cherry")

for x in thistuple:
    print(x)
    
#Loop Through the Index Number

"""
Ayrica index numaralarina bakarak tuple ogeleri arasinda gecis yapabilirsiniz.

'range()' ve 'len()' metodlarini kullanarak uygun araligi olusturabliliriz.

index numaralari araciligiyla butun ogeleri yazdirma:
"""

thistuple = ("apple", "banana", "cherry")

for i in range(len(thistuple)):
    print(thistuple[i])


#Using a While Loop

"""
Bir 'while' dongusu kullanarak da tuple ogeleri arasinda dolasabilirsiniz.

Tuple'in uzunlugunu belirlemek icin 'len()' fonksiyonunu kullanin, ardindan 
0' dan baslayin ve indexlerine basvurarak tuple ogeleri arasinda dolasin.

Tum index numaralarini kullanarak, while dongusu ile tum ogeleri yazdirma:
"""

thistuple = ("apple", "banana", "cherry")
i = 0

while i < len(thistuple):
    print(thistuple[i])
    i += 1
