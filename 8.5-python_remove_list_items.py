#Remove List Items

#Remove Specified Item

"""
'remove()' metodu belirtilen ogeyi kaldirir.

Remove "banana":
"""

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


#Remove Specified Index

"""
'pop()' metodu belirtilen index'i kaldirir.

Ikinci ogeyi kaldirma:
"""

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


"""
Eger index belirtmezseniz, 'pop()' metodu son ogeyi kaldirir.

Son ogeyi kaldirma
"""

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


"""
Ayrica 'del' anahtar kelimesi belirtilen indexi kaldirir.

Ilk elemani kaldirma:
"""

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


"""
Ayrica 'del' anahtar kelimesi listeyi tamamen silebilir.

Tum listeyi silme:
"""

thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) # Liste silindigi icin 'not defined' hatasi verecektir.


#Clear the List

"""
'clear()' metodu listeyi bosaltir.

Liste kalmaya devam eder, ancak icerigi olmaz.

Liste icerigini temizleme:
"""

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
