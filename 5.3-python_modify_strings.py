#Modify Strings

"""
Python stringlerde kullanilabilecek bir dizi 'built-in' fonksiyona sahiptir.
"""


#Upper Case

"""
upper(): upper metodu stringin buyuk harfli halini dondurur.
"""

a = "Hello, World!"
print(a.upper())


#Lower Case

"""
lower(): lower metodu stringin kucuk harfli halini dondurur.
"""

a = "Hello, World!"
print(a.lower())


a = "banana"
print(a.center(20, '-'))


#Remove Whitespace

"""
Whitespace bir metnin onundeki ve/veya sonundaki bosluktur. Cogu zaman bu
boslugu kaldirmak isteriz.
"""

"""
strip(): strip metodu metnin basinda veya sonunda bulunan herhangi bir boslugu
siler.
"""

a = "   Hello, World!   "
print(a.strip()) # returns "Hello, World!"


#Replace String

"""
replace(): replace metodu bir stringi digeriyle degistirir.
"""

a = "Hello, World!"
print(a.replace('H', 'J'))
print(a.replace("Hello", "Hi"))


#Split String

"""
split(): split metodu, belirtilen ayirici ile, string arasindaki metnin liste
ogeleri haline geldigi bir liste gonderir.
"""

a = "Hello, World!"
print(a.split(','))


#String Count

"""
count('x'): count metodu, belirtilen degerin stringde kac defa goruldugunu
dondurur.
"""

a = "I love apples, apple are my favorite fruit"
print(a.count('a'))
print(a.count("apple"))



#String Methods
"""
String metodlari hakkinda daha fazlasi icin addresse gidebilirsiniz.
"""

address = "https://www.w3schools.com/python/python_ref_string.asp"

import webbrowser
webbrowser.open_new(address)





















