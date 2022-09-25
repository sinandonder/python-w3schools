#Loop Dictionaries

#Loop Through a Dictionary

"""
Bir for dongusu kullanarak sozlukte dolasabilirsiniz.

Bir sozlukte dolasirken, donus degerleri sozlugun 'key' leridir, ancak value'
lari dondurmeninde yontemleri vardir.

Sozlukteki butun key' leri birer birer yazdirma:
"""


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in thisdict:
    print(x)



"""
Sozlukteki butun value' lari birer birer yazdirma:
"""

for x in thisdict:
    print(thisdict[x])


"""
Ayrica 'values()' metodunu kullanarak bir sozlugun value' larini 
dondurebilirsiniz:
"""

for x in thisdict.values():
    print(x)



"""
'keys()' metodunu kullanarak bir sozlugun key' lerini dondurebilirsiniz:
"""

for x in thisdict.keys():
    print(x)


"""
items metodunu kullanarak hem key hem de value' lar arasinda dolasabilirsiniz:
"""

for x, y in thisdict.items():
    print(x, y)

