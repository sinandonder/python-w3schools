#List Comprehension

"""
List Comprehension, mevcut bir listenin degerlerine dayali olarak yeni bir
liste olusturmak istediginizde daha kisa bir sozdizimi sunar.

Ornek:
    
Bir meyve listesine dayanarak, sadece adinda 'a' harfi olan meyveleri iceren
bir liste istediginizi varsayalim.

List Comprehension olmadan, icinde kosullu ifadeler iceren bir for dongusu
yazmaniz gerekecek:
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if 'a' in x:
        newlist.append(x)

print(newlist)


"""
List Comprehension ile bunlarin hepsini tek bir satirda yapabilirsiniz:
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if 'a' in x]

print(newlist)


#The Syntax

"""
newlist = [expression for item in iterable if condition == True]

Donus degeri yeni bir listedir ve eski liste degisime ugramaz.
"""


"""
Condition:
    Condition(Kosul) yalnizca 'True' olarak degerlendirilen ogeleri kabul eden
    bir filtre gibidir.

Sadece 'apple' olmayan ogeleri kabul etme:
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)

"""
if x != "apple" kosulu, "apple" disindaki tum ogeler icin 'True' degerini
dondurecek yeni listenin "apple" disinda tum elemanlari icermesini saglar.

Condition(Kosul) istege baglidir ve atlanabilir.

'if' ifadesi olmadan:
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)


"""
Itarable:
    Itarble(yinelenebilir), list, tuple, set gibi yinelenebilir herhangi bir
    nesne olabilir.
    
'range()' fonksiyonunu kullanarak bir itarable olusturabilirsiniz:
"""

newlist = [x for x in range(10)]

print(newlist)

"""
Ayni ornegin kosullusu:
"""

newlist = [x for x in range(10) if x < 5]
print(newlist)


"""
Expression:
    Expression(ifade), yinelemedeki gecerli bir ogedir, ancak ayni zamanda, 
    yeni listedeki bir liste ogesi gibi sona ermeden once degistirilebilir.

Sonucu istediginiz gibi degistirebilirsiniz.

Yeni listedeki tum degerleri 'hello' olarak ayarlama:
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ["hello" for x in fruits]

print(newlist)

"""
Expression(ifade), bir filtre degil, sonucu degistirmenin bir yolu olarak
kosullar da icerebilir.

"orange" yerine "banana" dondrume:
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

"""
Yukaridaki ornek soyle diyor:
    "Eger oge 'banana' degilse ogeyi dondur, eger oge 'banana' ise 'orange'
    dondur."
"""
