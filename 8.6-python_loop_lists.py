#Loop Lists

#Loop Through a List

"""
Bir 'for' dongusu kullanarak liste ogeleri arasinda dolasabilirsiniz.

Listenin butun ogelerini tek tek yazdirma:
"""

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)


#Loop Through the Index Numbers

"""
Ayrica, index numaralariyla liste ogeleri arasinda dolasabilirsiniz.

Uygun bir aralik olusturmak icin 'range()' ve 'len()' fonksiyonlarini kullanin.

Listenin butun ogelerini index numaralariyla yazdirma:
"""

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

"""
Yukaridaki ornekte olusturulan aralik [0, 1, 2] seklindedir.
"""


#Using a While Loop

"""
Bir 'while' dongusu kullanarak liste elemanlari arasinda dolasabilirsiniz.

Listenin uzunlugunu belirlemek icin len() fonksiyonunu kullanin, ardindan
0'dan baslayin ve index numaralariyla liste ogeleri arasinda dolasin.

Her yinelemeden sonra index'i bir artirmayi unutmayin.

Tum indexlerden gecerek bir 'while' dongusuyle ogeleri yazdirma:
"""

thislist = ["apple", "banana", "cherry"]
i = 0

while i < len(thislist):
    print(thislist[i])
    i = i + 1

#Looping Using List Comprehension

"""
List Comprehension, listeler arasinda dolasmak icin en kisa sozdizimini sunar.

Bir listedeki tum elemanlari yazdiracak kisa bir yontem:
"""

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
