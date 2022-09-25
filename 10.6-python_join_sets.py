#Join Sets

#Join Two Sets

"""
Python' da iki veya daha fazla kumeyi birlestirmenin birkac yolu vardir.

Her iki Set' teki tum ogeleri iceren yeni bir Set donduren 'union()' metodunu
veya bir Set' teki tum ogeleri digerine ekleyen 'update()' yontemini
kullanabilirsiniz.

'union()' metodu her iki Set' teki tum ogelerle birlikte yeni bir Set dondurur:
"""

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)

print(set3)

"""
Not: Hem 'union()' hem de 'update()' yinelenen ogeleri haric tutacaktir.
"""


#Keep ONLY the Duplicates

#intersection_update()

"""
'intersection_update()' metodu yalnizca her iki kumede de bulunan ogeleri
tutacaktir. Bir baska deyisle kumelerin kesisimini alacaktir.(x n y)

Hem 'x' kumesinde hem de 'y' kumesinde bulunan ogeleri tutma:
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


#intersection()

"""
'intersection()' metodu yalnizca her iki kumede de bulunan ogeleri iceren yeni
bir kume dondurur.(x n y)

Hem 'x' kumesinde hem de 'y' kumesinde bulunan ogeleri dondurme:
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


#Keep All, But NOT the Duplicates

#symmetric_difference_update()

"""
'symmetric_difference_update()' metodu yalnizca her iki kumede de OLMAYAN
ogeleri tutacaktir. (x u y - x n y) 

Her iki Set' tede bulunmayan ogeleri tutma:
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)


#symmetric_difference()

"""
'symmetric_difference()' metodu yalnizca her iki kumede de OLMAYAN ogeleri
iceren yeni bir Set dondurur.

Her ikisinde de bulunan ogeler haric, her iki kumedeki tum ogeleri iceren bir
Set dondurme: 
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
