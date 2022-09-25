#Slicing

"""
Bolumleme syntaxini kullanarak bir dizi karakter dondurebiliriz.
Stringin bir bolumunu dondurmek icin iki nokta(:) ile ayrilmis baslangic dizini
ve bitis dizini belirtin.

2. pozisyondan 5. pozisyona kadar olan karakterleri almak(5 dahil degildir).
"""

b = "Hello, World!"
print(b[2:5])


#Slice From the Start

"""
Baslangic indexini girmedigimizde, donen dizi ilk karakterden baslar.

Ilk karakterden 5. pozisyondaki karaketere kadar almak(5 dahil degildir).
"""

b = "Hello, World!"
print(b[:5])


#Slice To the End

"""
Bitis indexini girmedigimizde, donen dizi sona kadar gider.

2. pozisyondan son pozisyona kadar olan karakterleri almak
"""

b = "Hello, World!"
print(b[2:])


#Negative Indexing

"""
Negatif indexlemeyi kullanarak stringi bolumlemeye sondan baslayabiliriz.
Not: -1 son karaketeri temsil eder.

-5 ten -2 ye kadar olan diziyi almak.
"""

b = "Hello, World!"

print(b[-5:-2])


#Reverse String

"""
Python' da bir string' i tersine cevirmek icin built-in(yerlesik) bir
metot yoktur.

En hızlı ve en kolay yol geriye dogru giden bir slice(dilim) kullanmaktir.
[::-1]
"""

b = "Hello, World!"

print(b[::-1])




































