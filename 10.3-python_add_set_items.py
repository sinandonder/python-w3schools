#Add Set Items

#Add Items

"""
Bir Set olusturulduktan sonra ogelerini degistiremezsiniz, ancak yeni ogeler
ekleyebilirsiniz.

Bir Set' e bir oge eklemek icin 'add()' metodunu kullanabilirsiniz.

'add()' metodu ile Set' e bir oge ekleme:
"""

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


#Add Sets

"""
Geçerli Set' e başka bir Set' in ogelerini eklemek icin 'update()' metodunu
kullanabilirsiniz.

tropical Set' indeki elemanlari thisset' e ekleme:
"""

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)


#Add Any Iterable

"""
'update()' metodunun parametresinin bir Set olmasi gerekmez, yinelenebilir
herhangibir nesne(tuple, liste, sozluk) olabilir.
"""

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)
