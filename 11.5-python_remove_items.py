#Remove Dictionary Items

#Remove Items

"""
Bir sozlukten ogeleri kaldirmanin birkac yontemi vardir.

'pop(x)' x: keyname, metodu belirtilen key ismindeki ogeyi kaldirir:
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.pop("model")

print(thisdict)


"""
'popitem()' metodu son eklenen ogeyi kaldirir(3.7 versiyonundan once bunun
yerine rastgele bir oge kaldirilabilirdi):
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.popitem()
print(thisdict)


"""
'del' anahtar kelimesi belirtilen key ismindeki ogeyi kaldirir:
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

del thisdict["model"]
print(thisdict)


"""
'del' anahtar kelimesi ayrica sozlugu tamamen silebilir:
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

del thisdict
#print(thisdict) # 'thisdict' artik olmadigindan hataya sebep olacaktir.


"""
'clear()' metodu sozlugunu icini bosaltir:
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict.clear()
print(thisdict)