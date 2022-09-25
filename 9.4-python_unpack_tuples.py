#Unpack Tuples

#Unpacking a Tuple

"""
Bir tuple olusturdugumuzda, normalde ona degerler atariz. Buna tuple paketleme
denir.

Tuple paketleme:
"""

fruits = ("apple", "banana", "cherry")

"""
Ancak Python' da paketleri geri acmamiza da izin verilir. Buna 'paket acma'
denir.

Bir tuple'i acma:
"""

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


"""
Not degiskenlerin sayisi, tupledaki degerlerin sayisi ile eslesmelidir, degilse
kalan degerleri bir liste olarak toplamak icin bir 'yildiz' isareti 
kullanmalisiniz.
"""


#Using Asterisk *

"""
Degisken sayisi deger sayisindan az ise, degisken adina * ekleyebilirsiniz ve
degerler liste olarak degiskene atanacaktir.

Degerlerin geri kalanini 'red' isimli bir liste olarak atayin:
"""

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


"""
Yildiz isareti sondan baska bir degisken adina eklenirse, Python, kalan
degerlerin sayisi kalan degiskenlerin sayisiyla eslesene kadar degiskene
degerler atar.

'tropic' degiskenine liste atama:
"""

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
