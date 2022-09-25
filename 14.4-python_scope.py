#Python Scope

"""
Bir degisken yalnizca olusturuldugu bolgenin icinde kullanilabilir. Buna kapsam
(scope) denir.
"""


#Local Scope

"""
Bir fonkisyon icinde olusturulan bir degisken, o fonksiyonun yerel scope'una
aittir ve sadece o fonksiyonun icinde kullanilabilir.

Bir fonksiyonun icinde olusturulan bir degisken, o fonksiyonun icerisinde
kullanilabilir:
"""

def myFunc():
    x = 300
    print(x)

myFunc()


#Function Inside Function

"""
Yukaridaki ornekte aciklandigi gibi, x degiskeni fonksiyonun disinda mevcut
degildir, ancak fonksiyonun icindeki herhangi bir fonksiyon icin kullanilabilir.

Local degiskene, fonksiyon icindeki bir fonksiyondan erisilebilir:
"""

def myfunc():
    x = 400

    def myinnerfunc():
        print(x)
        
    myinnerfunc()

myfunc()


#Global Scope

"""
Python kodunun ana(main) govdesinde olusturulan bir degisken global bir
degiskendir ve global kapsama aittir.

Global degiskenler, global ve yerel herhangi bir kapsamda kullanilabilir.

Bir fonksiyonun disinda olusturulan bir degisken globaldir ve herkes tarafindan
kullanilabilir:
"""

x = 300

def myfunc():
    print(x)

myfunc()

print(x)


#Naming Variables

"""
Bir fonksiyonun icinde ve disinda ayni degisken adiyla calisirsaniz, Python
bunlari, biri global kapsamda(fonksiyonun disinda) ve digeri yerel kapsamda
(fonksiyonun icinde) mevcut olan iki ayri degisken olarak degerlendirir.

Fonksiyon local x'i yazdiracak ve ardindan kod genel x' i yazdiracaktir:
"""

x = 500

def myfunc():
    x = 200
    print(x)

myfunc()
print(x)


#Global Keyword

"""
Global bir degisken olusturmaniz gerekiyorsa, ancak local scope'da takilip
kaldiysaniz, global anahtar sozcugunu kullanabilirsiniz.

global keyword'u degiskeni global yapar.

global anahtar sozcugunu kullanirsaniz, degisken global scope'a aittir:
"""

def myfunc():
    global x
    x = 1300

myfunc()

print(x)


"""
Ayrica, bir fonksiyon icinde global bir degiskende degisiklik yapmak 
istiyorsaniz global anahtar sozcugunu kullanin.

Fonksiyon icerisinde bir global degiskenin degerini degistirmek icin, global
keyword'unu kullanarak degiskene basvurun:
"""

x = 300

def myfunc():
    global x
    x = 1200

myfunc()

print(x)
