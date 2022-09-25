#String Format

"""
Python Variables bolumunde int ile string bir turun birlestirilemeyecegini
gorduk.

Ama int ve stringi 'format()' metodunu kullanarak birlestirebiliriz.
"""

#format method

"""
format() medotu {} tutucuların icerisindeki bagimsiz degiskenleri alir,
bicimlendirir ve yer tutucuların bulundugu dizeye ekler.
"""

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#format method - unlimeted arguman

"""
format() metodu limitsiz numara argumanı alır ve ilgili yer tutuculara bu
argumanlari yerlestirir.
"""

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#format method - index place

"""
Bagimsiz degiskenlerin dogru yer tutuculara yerlestirildiginden emin olmak
icin {0} index numaralarini kullanabiliriz.
"""

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))
