#Python While Loops

#Python Loops

"""
Python' un iki ilkel dongu komutu vardır:

* while loops
* for loops
"""

#The while Loop

"""
while dongusu ile bir dizi ifadeyi, while kosulu dogru oldugu surece 
calistirabilirsiniz.

6' dan kucuk oldugu surece i' yi yazdirma:
"""

i = 1

while i < 6:
    print(i)
    i += 1

"""
Not: i' yi artirmayi unutmayin aksi takdirde dongu sonsuza kadar devam eder.
"""

#The break Statement

"""
break ifadesi ile while kosulu dogru olsa bile donguyu durdurabiliriz.

i 3 oldugunda donguden cikma:
"""

print("\n")

i = 1

while i < 6:
    print(i)

    if i == 3:
        break
    i += 1


#The continue Statement

"""
continue ifadesi ile mevcut yinelemeyi durdurabilir ve bir sonraki ile devam
edebiliriz.

i 3 ise bir sonraki yinelemeye devam etme:
"""

print("\n")

i = 0

while i < 6:
    i += 1

    if i == 3:
        continue
    
    print(i)


#The else Statement

"""
else ifadesi ile kosul artik dogru olmadiginda bir kod blogunu bir kez
calistirabiliriz.

Kosul 'False' oldugunda bir mesaj yazdirma:
"""
print("\n")

i = 1

while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer than 6")
