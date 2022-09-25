#Dictionaries

#Dictionary

"""
Sozlukler, veri degerlerini key:value ciftlerinde depolamak icin kullanilir.
Sozluk, sirali* degistirilebilir ve yinelenen degerlere izin vermeyen bir 
koleksiyondur.

*Python 3.7 surumunden itibaren sozlukler siralanmistir. Python 3.6 ve onceki
surumlerde sozlukler sirasizdir.

Sozlukler kivircik parantezler arasina yazilir ve key:value degerlerinden 
olusur.

Bir sozluk olusturup yazdirmak:
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict)


#Dictionary Items

"""
Sozluk ogeleri siralidir, degistirilebilir, ve yinelemelere izin vermez.
Sozluk ogeleri key:value ciftlerinden olusur, ve key adi kullanilarak referans
alinabilir.

Sozlugun "brand" degerini yazdirma:
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(thisdict["brand"])


#Ordered or Unordered

"""
Python 3.7 surumunden itibaren sozlukler siralanmistir. Python 3.6 ve onceki
surumlerde sozlukler sirasizdir.

Sozlukler siralidir dedigimizde ogelerin belirli bir sirasi vardir ve bu sira
degismeyecektir.

Sirasiz, ogelerin tanimlanmis bir siraya sahip olmadigi anlamina gelir, bir
ogeye index kullanarak basvuramazsiniz.
"""


#Changeable

"""
Sozlukler degistirilebilir demek sozluk olusturulduktan sonra ogeleri
degistirebilir, ekleyebilir ve kaldirabiliriz.
"""


#Duplicates Not Allowed

"""
Sozlukler ayni iki key' e sahip olamaz.

Yinelenen degerler mevcut degerlerin uzerine yazilir.
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
    
}

print(thisdict)


#Dictionary Length

"""
Bir sozlugun kac ogeden olustugunu belirlemek icin 'len()' fonksiyonu 
kullanilir.

Sozlugun oge sayisini yazdirma:
"""

print(len(thisdict))


#Dictionary Items Data Types

"""
Sozluk ogelerindeki degerler herhangi bir veri turunden olabilir.

String, int, boolean ve list veri tipleri:
"""

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

print(thisdict)


#type()

"""
Python' un bakis acisindan sozlukler 'dict' veri tipine sahip nesneler olarak
tanimlanir.

Bir sozlugun veri tipini yazdirma:
"""

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(type(thisdict))