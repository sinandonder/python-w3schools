#Assign Multiple Values

x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)


#One Value to Multiple Variables

x = y = z = "Orange"
print(x, y, z)


#Unpack a Collection

fruits =  ["apple", "banana", "cherry"]

x, y, z = fruits
print(x, y, z)


"""
Python Global Variables
"""

x = "awesome"

def my_func():
    print("Python is " + x)

my_func()

y = "awesome"

def my_func2():
    y = "fantastic"
    print("Python is " + y)

my_func2()
print("Python is " + y)


#The Global Keyword

"""
Normalde bir fonksiyonun icerisinde bir degisken olusturulursa, bu degisken
'local' degiskendir ve yalnizca o fonksiyon icerisinde kullanilabilir.

Bir fonksiyonun icinde bir global degisken olusturmak icin 'global' anahtar
kelimesi kullanilir
"""

def my_func3():
    global a
    a = "fantastic"

my_func3()
print("Python is " + a)

"""
Ayrica, 'global' anahtar kelimesi kullanilarak fonksiyon icerisinde global
degiskenin degeri degistirilebilir.
"""

x = "awesome"

def my_func4():
    global x
    x = "fantastic"
    
my_func4()

print("Python is " + x)










































