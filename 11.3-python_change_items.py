#Change Dictionary Items

#Change Values

"""
Key' i referans alarak belirli bir ögenin degerini degistirebilirsiniz.

'year' i 2018 olarak degistirme:
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict["year"] = 2018

print(thisdict)


#Update Dictionary

"""
'update()' metodu sozlugu verilen argumanlarla guncelleyecektir.

Bu arguman dictionary veya key:value ciftinden olusan bir koleksiyon olmalidir.

'car' in yilini 'update()' metodu kullanarak guncelleme:
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.update({"year": 2020})

print(thisdict)
