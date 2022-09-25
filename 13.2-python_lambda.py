#Python Lambda

"""
Bir lambda fonksiyonu, kucuk bir anonim fonksiyondur.

Bir lambda fonksiyonu herhangi bir sayida arguman alabilir, ancak yalnizca bir
ifadeye sahip olabilir.
"""


#Syntax

"""
    lambda arguments : expression

    Ifade(expression) yurutulur ve sonuc dondurulur.

Arguman a'ya 10 ekleyin ve sonucu dondurun:
"""

x = lambda a : a + 10

print(x(5))


"""
Lambda fonksiyonlari herhangi bir sayida arguman alabilir.
a argumanini b argumaniyla carpin ve sonucu dondurun:
"""

x = lambda a, b : a * b

print(x(5, 6))


"""
a, b ve c argumanlarini toplayin ve sonucu dondurun:
"""

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



x = lambda n: (n * (n + 1)) / 2

print(x(10000))


#Why Use Lambda Functions?

"""
Lambda' nin gucu, onlari baska bir fonksiyonun icinde anonim bir islev olarak
kullandiginizda daha iyi gosterilir.

Bir arguman alan bir fonksiyon taniminiz oldugunu ve bu argumanin bilinmeyen bir
sayi ile carpilacagini varsayalim.

Gonderdiginiz sayiyi her zaman iki katina cikaran bir fonksiyon yapmak icin bu 
fonksiyon tanimini kullanalim:
"""

def myfunc(n):
    return lambda a : a * n


mydoubler = myfunc(2)
print(mydoubler(11))


"""
Veya, gonderdiginiz sayiyi her zaman 3 katina cikaran bir fonksiyon yapmak icin
ayni fonksiyon tanimini kullanin:
"""

mytripler = myfunc(3)
print(mytripler(11))


"""
Kisa bir sure icin anonim bir islev gerektiginde lamda fonksiyonlarini kullanin.
"""
