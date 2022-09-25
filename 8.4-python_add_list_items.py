#Add List Items

#Append Items

"""
Listenin sonuna bir oge eklemek icin 'append()' metodu kullanilir.

'append()' metodunu kullanarak oge ekleme:
"""

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#Insert Items

"""
Bir listenin belirli bir index'ine eleman eklemek icin 'insert()' metodu
kullanilir.

'insert()' metodu belirlenen indexe elemani ekler.

Ikinci konuma bir oge ekleme:
"""

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

"""
Yukaridaki ornekte liste artik 4 elemanli olacaktir.
"""


#Extend List

"""
Gecerli listeye baska bir liste eklemek icin 'extend()' metodu kullanilir.

'tropical' listesinin ogelerini 'thislist' e ekleme:
"""

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

"""
Ogeler listenin sonuna eklenecektir.
"""


#Add Any Iterable

"""
extend() metodu sadece listeler icin gecerli degildir, yinelenebilir herhangi
bir nesne(tuple, set, dictionary) ekleyebilirsiniz.

Bir listeye bir tuple' in ogelerini ekleme:
"""

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
