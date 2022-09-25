#Python If ... Else

#Python Conditions and If Statements

"""
Python matematikteki genel mantiksal ifadelerini destekler.

Esit mi: a == b
Esit degil mi: a != b
Kucuktur: a < b
Kucuk veya Esit: a <= b
Buyuktur: a > b
Buyuk veya Esit: a >= b

Bu kosullar, en yaygin olarak 'if ifadeleri' ve dongulerde olmak uzere cesitli
sekillerde kullanilabilir.

'if' anahtar sozcugu kullanilarak bir 'if ifadesi' yazilir.

If ifadesi:
"""

a = 33
b = 200

if b > a:
    print("b is grater than a")


"""
Bu ornekte, b' nin a' dan buyuk olup olmadigini test etmek icin 'if ifadesinin'
bir parcasi olarak kullanilan 'a' ve 'b' degiskenlerini kullaniyoruz.
"""


#Indentation

"""
Python, koddaki kapsami(scope) tanimlamak icin girintiye(satir basindaki bosluk)
bakar. Diger programlama dilleri bu amac icin genellikle kivircik parantezler
kullanir.

Girintisiz if ifadesi(hataya neden olacaktır.):
"""

a = 33
b = 200

"""
if b > a:
print("b is greater than a") # hataya neden olur.
"""


#Elif

"""
'elif' anahtar kelimesi Python' da "onceki kosullar dogru degilse bu kosulu 
dene" demenin yoludur.
"""

a = 33
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")


"""
Bu ornekte a esittir b, yani ilk kosul dogru degil, ancak elif kosulu dogru, bu
yuzden ekrana a ve b esittir yazdiriyoruz.
"""


#Else

"""
'else' keyword' u onceki kosullar tarafindan yakalanmayan her seyi yakalar.
"""


a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")


"""
Bu ornekte a, b' den buyuktur, yani birinci kosul dogru degil, ayrica 'elif'
kosulu da dogru degil, bu yuzden 'else' kosuluna gidip ekrana "a b'den buyuktur"
yazdiriyoruz.

Ayrica 'elif' olmadan da 'else' kullanabilirsiniz:
"""

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")


#Short Hand If

"""
if' den sonra yurutulecek yalnizca bir satir kod varsa, onu if ile ayni satira
yazabilirsiniz.

Tek satir if ifadesi:
"""

if a > b: print("a is greater than b")


#Short Hand If ... Else

"""
if ve else icin, yurutulecek yalnizca bir ifadeniz varsa hepsini ayni satira
yazabilirsiniz.

Tek satir if else ifadesi:
"""

a = 2
b = 330

print('A') if a > b else print('B')

"""
Bu teknik 'Ternary Operators' veya 'Conditional Expressions' olarak bilinir.
"""

"""
Ayni satirda birden fazla else ifadenizde olabilir.

3 kosul ile tek satir if else ifadesi:
"""

a, b = 330, 330

print('A') if a > b else print('=') if a == b else print('B')


#And

"""
'and' keyword' u bir mantiksal operatordur ve kosullu ifadeleri birlestirmek 
icin kullanilir.

a' nin b' den buyuk olup olmadigini VE c' nin a' dan buyuk olup olmadigini test
edin:
"""

a, b, c = 200, 33, 500

if a > b and c > a:
    print("Both conditions are True")


#Or

"""
'or' keyword'u bir mantiksal operatordur ve kosullu ifadeleri birlestirmek icin
kullanilir.

a' nın b' den buyuk olup olmadigini VEYA a' nın c' den buyuk olup olmadigini
test edin:
"""

a, b, c = 200, 33, 500

if a > b or a > c: print("At least one of the conditions the True")


#Nested If

"""
If ifadelerinin icerisinde baska if ifadeleri olabilir, buna ic ice if ifadeleri
denir.
"""

x = 41

if x > 10:
    print("Above ten, ")

    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


#The pass Statement

"""
if ifadeleri bos olamaz, ancak herhangi bir nedenle icerigi olmayan bir if
ifadeniz varsa, hata almamak icin 'pass' ifadesini girin.
"""

a, b = 33, 200

if b > a:
    pass