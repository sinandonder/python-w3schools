#Copy a Dictionary

"""
dict2 = dict1 yazarak bir sozlugu kopyalayamazsiniz cunku dict2 sadece dict 1'
in referansi olur, dict1 de yapilan degisiklikler otomatik olarak dict2' de de
meydana gelecektir.

Bir kopya olusturmanin yollari vardir, bir yol built-in metot olan 'copy()'
metodunu kullanmaktir.

'copy()' metodu ile bir sozlugunu kopyasini olusturma:
"""

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = thisdict.copy()
print(mydict)


"""
Bir kopya olusrumanin bir baska yolu ise built-int metot olan 'dict()' i 
kullanmaktir.

'dict()' metodu ile bir sozlugun kopyasini olusturma:
"""

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = dict(thisdict)
print(mydict)