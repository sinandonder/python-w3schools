#Copy Lists

#Copy a List

"""
list2 = list1 yazarak bir listeyi kopyalayamazsiniz cunku: list2 sadece
list1' e referans olacaktir ve list1' de yapilacak degisiklikler list2'de de
otomatik olarak yapilacaktir.

Bir kopya olustrumanin yollari vardir, bir yol built-in(yerlesik) List metodunu
kullanmaktir(copy()).

'copy()' metodunu kullanarak listenin bir kopyasini olusturmak:
"""

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


"""
Bir kopya olusturmanin baska bir yolu da yerlesik metod 'list()'i kullanmaktir.

'list()' metodunu kullanarak listenin bir kopyasini olusturmak:
"""

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


"""
Bir baska yol:
"""

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


"""
Baska bir yol:
"""

thislist = ["apple", "banana", "cherry"]
mylist = [x for x in thislist]
print(mylist)
