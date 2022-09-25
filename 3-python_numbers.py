import random

#Power Float

"""
Float tipi 10 uzeri bir sayiyi ifade eden 'e' harfi ile de tanimlanabilir.

ex: float f = 6e2 = 6 * 10 ^ 2 = 600.0
"""

#Type Conversion

i = 1
f = 2.8
c = 1j

#Convert from int to float

a = float(i)
print(a)

#Convert from float to int

b = int(f)
print(b)

#Convert from int to complex

c = complex(i)
print(c)


print(type(a))
print(type(b))
print(type(c))

"""
Karmasik(complex) sayilar baska bir sayi turune donusturulemez.
"""


"""
Random Number

Python' da random() fonksiyonu yoktur fakat Python' da bir built-in modul olan
'random' modulu vardır. Bu modulu kullanarak random sayilar uretebilirsiniz.
"""

#import random

print(random.randrange(1, 10))












































