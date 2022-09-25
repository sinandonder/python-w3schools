#Access Dictionary Items

#Accessing Items

"""
Koseli parantezler icerisinde key' i referans alarak bir sozlugun ogelerine
erisebilirsiniz.

model key' inin degerini alma:
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = thisdict["model"]
print(x)

"""
'get()' metodu ile de ayni sonuca ulasabilirsiniz.

model key' inin degerini alma:
"""

x = thisdict.get("model")
print(x)


#Get Keys

"""'
'keys()' metodu sozlukdeki butun 'key' lerin bir listesini dondurur.

key' lerin listesini alma:
"""

x = thisdict.keys()
print(x)

"""
Key listesi sozlugun bir gorunumudur, yani sozlukte yapilan herhangi bir 
degisiklik key listesine yansitilacaktir.

Orijinal sozluge yeni bir oge ekleyip key listesinin guncellenmesi:
"""

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x) # degisimden once

car["color"] = "white"

print(x) # degisimden sonra


#Get Values

print("\n#Get Values")
"""
values() metodu sozlukteki butun 'value' larin bir listesini dondurur.

Value' larin listesini alma:
"""

x = thisdict.values()

print(x)

"""
Value listesi sozlugun bir gorunumudur, yani sozlukte yapilacak herhangi bir
degisiklik value listesinede yansitilacaktir.

Orjinal sozlukteki bir ogenin degerini degistirip value listesinin 
guncellenmesi:
"""

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x) # degisimden once

car["year"] = 2020

print(x) # degisimden sonra


"""
Orijinal sozluge yeni bir oge eklenince values listesinin guncellenmesi:
"""

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x) # degisimden once

car["color"] = "red"

print(x) # degisimden sonra


#Get Items
print("\n#Get Items")

"""
'items()' metodu bir sozlukteki butun ogeleri bir liste icerisindeki
tuple' lar halinde dondurur.

key:value ciflerinin alinmasi:
"""

x = thisdict.items()
print(x)

"""
Dondurulen liste sozlugun ogelerinin bir gorunumudur, yani sozlukte yapilacak
herhangi bir degisiklik oge listesine de yansitilacaktir.

Orijinal sozlukte degisiklik yapilip oge listesinin guncellenmesi:
"""

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print(x) #degisimden once

car["year"] = 2020
print(x) #degisimden sonra

"""
Orijinal sozluge yeni bir oge eklenince values listesinin guncellenmesi:
"""

car = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1964
}

x = car.items()
print(x) # degisimden once

car["color"] = "red"
print(x) # degisimden sonra


#Check If Key Exist
print("\n#Check If Key Exits")

"""
Bir sozlukte belirtilen bir key degerinin olup olmadigini belirlemek icin 'in'
anahtar sozcugunu kullanabilirsiniz.

"model" anahtarinin bulunup bulunmadigini kontrol etme:
"""

if "model" in thisdict:
    print("Yes, model is one of the keys in the thisdict dictionary")
