#Add Dictionary Items

#Adding Items

"""
Sozluge bir oge eklemek, yeni bir key ile referans edip deger esitleyerek olur.
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["color"] = "red"
print(thisdict)


#Update Dictionary

"""
'update()' metodu verilen arguman ile sozlugu gunceller. Eger verilen arguman,
sozlukte yoksa bu arguman sozluge eklenir.

Bu arguman sozluk veya, key:value ciftlerinden olusan bir koleksiyon olmalidir.

'update()' metodunu kullanarak sozluge color ogesini ekleme:
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.update({"color": "blue"})
print(thisdict)