#Update Tuples

"""
Tuple ogeleri degistirilemez, yani tuple olustrulduktan sonra ogeleri
degistiremez, ekleyemez veya kaldiramazsiniz.

Ama bazi gecici cozumler vardir.
"""


#Change Tuple Values

"""
Bir tuple olustrulduktan sonra degerlerini degistiremezsiniz. Tuplelar
'unchangeable' veya 'immutable' olarak da adlandirilir.

Ama bir gecici cozum var. Tuple'i bir listeye donusturebilir, listeyi 
degistirebilir ve listeyi tekrar bir tuple' a donusturebilirsiniz.

Tuple' i degistirebilmek icin listeye donusturme:
"""

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


#Add Items

"""
Tuplelar immutable oldugundan built-in (yerlesik) bir 'append()' metoduna sahip
degildirler, ancak bir tuple' a oge eklemenin baska yollari da vardir.

1-Listeye Donusturme:
    Bir tuple' i degistirmeye yonelik gecici bir cozum gibi, onu bir listeye
donusturebilir, ogelerinizi ekleyebilir ve tekrar bir tuple' a 
donusturebilirsiniz.

Tuple' i bir listeye donusturup, "orange" ekleyip tekrar tuple' a donusturme:
"""

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)


"""
2-Bir tuple' a tuple ekleme:
    Tuplelara tuple ekleyebiliriz, bu nedenle bir oge veya daha fazla eklemek
istiyorsaniz, ogeler ile yeni bir tuple olusturup onu mevcut tuple'a 
ekleyebiliriz.

"orange" degerine sahip yeni bir tuple olusturup bunu mevcut tuple'a ekleme:
"""

thistuple = ("apple", "banana", "cherry")
y = ("orange", )

thistuple += y

print(thistuple)


"""
Not: Yalnizca bir oge iceren bir tuple olustururken, ogeden sonra virgul
ekelemeyi unutmayin, aksi takdirde tuple olarak tanimlanmayacaktir.
"""


#Remove Items

"""
Not: Bir tuple icerisindeki ogeleri kaldiramazsiniz.

Tuplelar degistirilemez, bu nedenle ondan ogeleri kaldiramazsiniz, ancak tuple
ogelerini degistirmek ve eklemek icin kullandigimizla ayni gecici cozumu
kullanabilirsiniz.

Tuple' i bir listeye donusturun, "apple" i kaldirip tekrar listeye donusturme:
"""

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)


"""
Veya tuple' i tamamen silebilirsiniz.

'del' anahtar kelimesi tuple'i tamamen silebilir:
"""

thistuple = ("apple", "banana", "cherry")
del thistuple

#print(thistuple) #tuple artik mevcut olmadigi icin hataya neden olacaktir.
