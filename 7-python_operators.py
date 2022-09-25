#Python Operators

"""
Operatorler degiskenler ve degerler uzerinde islem yapmak icin kullanilir.

Asagidaki ornekte '+' operatorunu iki degeri birbirine eklemek icin kullandik.
"""

print(10 + 5)

#Pyton divides the operators in the following groups

"""
* Arithmetic operators (Aritmetik Operatorler) (+, -, *, /, %, **, //)
* Assignment operators (Atama Operatorleri) (=, +=, -=, *=, /=, %=, //=, **=, 
                                             &=, |=, ^=, >>=, <<=)
* Comparison operators (Karsilastirma Operatorleri) (==, !=, >, <, >=, <=)
* Logical operators (Mantiksal Operatorler) (and, or, not)
* Identity operators (Kimlik Operatorleri) (is, is not)
* Membership operators (in, not in)
* Bitwise operators (Bitsel Operatorler) (&, |, ^, ~, <<, >>)
"""


#Aritmetical Operators

"""
Aritmetik operatorler, yaygın matematiksel islemleri gerceklestirmek icin
sayisal degerlerle birlikte kullanilir.
"""


#Assigment Operators
# (=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=)
"""
Atama operatorleri, degerleri degiskenlere atamak icin kullanilir.
"""


#Comparison Operators (==, !=, >, <, >=, <=)

"""
Karsilastirma operatorleri, iki degeri karsilastirmak icin kullanilir.
"""


#Logical Operators (and, or, not)

"""
Mantiksal Operatorler, kosullu ifadeleri birlestirmek icin kullanilir.
"""


#Identity Operators (is, is not)

"""
Kimlik operatorleri, nesneleri esit olup olmadiklari degil, aslinda ayni
nesneyse ve ayni bellek konumuna sahipse karsilastirmak icin kullanilir.

Identity Operators: is, is not
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

"""
z, x ile ayni nesne oldugundan True dondurur.
"""
print(x is z)


"""
x, y ayni icerige sahip olsalar bile, ayni nesne olmadiklarindan False doner.
"""
print(x is y)


"""
'is' ve '==' arasindaki fark is, nesnelerin bellekteki konumlarinin ayni olup
olmadigina, '==' ise nesnelerin iceriginin ayni olup olmadigina bakar.
"""
print(x == y)


#Membership Operators (in, not in)

"""
Membership Operatorler, bir nesnede bir dizinin bunulup bunulmadigini test 
etmek icin kullanilirlar.

Membership Operators: in, not in
"""


#Bitwise Operators (&, |, ^, ~, <<, >>)

"""
Bitwise Operatorler, binary sayilari karsilastirmak icin kullanilir.

Bitwise Operatorler: &: (AND), |: (OR), ^: (XOR), ~: (NOT)
"""

#Operatorler hakkinda daha fazlasi icin bkz.

import webbrowser
webbrowser.open("https://www.w3schools.com/python/python_operators.asp")
