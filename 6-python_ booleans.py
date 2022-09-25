"""
Boolean degerleri, iki degerden biri temsil eder: True veya False
"""

#Boolean Values

"""
Programlama da siklikla bir ifadenin 'True' veya 'False' oldugunu bilmek
isteriz.

Python' da herhangi bir ifadeyi degerlendirebilir ve True veya False olmak
uzere iki yanittan birini alabilirsiniz.

Iki degeri karsilastirdiginizda, ifade degerlendirilir ve Python bir Boolean
deger dondurur.
"""

print(10 > 9)
print(10 == 9)
print(10 < 9)


"""
Bir 'if' ifadesinde bir kosul calisrtirildiginda Python 'True' veya 'False'
dondurur.
"""

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


#Evaluate Values and Variables

"""
'bool()' metodu herhangi bir degeri degerlendirmeyi saglar ve True veya False
degerlerinden birini dondurur.

Bir string ve bir sayi degerlendirme
"""

print(bool("Hello"))
print(bool(15))


#Evaluate two variables

x = "Hello"
y = 15

print(bool(x))
print(bool(y))


#Most Values are True

"""
Bir tur icerige sahipse, hemen hemen her deger True olarak degerlendirilir.

Bos String disinda, her String True' dur.

'0' disinda her sayi True' dur.

Bos olmamalari durumunda her list, tuple, set ve dictionary True' dur.

Asagidakiler 'True' dondurecektir.
"""

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


#Some Values are False

"""
Aslinda (), [], {}, "", 0, None degerleri gibi bos degerler disinda 'False'
olarak degerlendirilen cok fazla deger yoktur. Ve Elbette 'False' degeri False
olarak degerlendirilir.

Asagidakiler False Olacaktir.
"""

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


"""
Bu durumda bir deger veya nesne daha 'False' olarak degerlendirilir. Bu da 
0 veya False donduren __len__ metoduna sahip bir nesnedir.
"""

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))


#Functions can Return a Boolean

"""
Boolean degeri donduren fonksiyonlar olusturabilirsiniz.
"""

def my_function():
    return True

print(my_function())


"""
Bir fonksiyonun Boolean yanitina gore kodu calistirabilirsiniz.

Fonksiyon True dondururse "YES!" aksi takdirde "NO!" yazdiran kod:
"""

def my_function2():
    return True

if my_function2():
    print("YES!")
else:
    print("NO!")


"""
Python ayrica, bir nesnenin belirli bir veri turunde olup olmadigini
belirlemek icin kullanilabilen isinstance() fonksiyonu gibi bir Boolean degeri
donduren bircok built-in(yerlesik) fonksiyona sahiptir.

Bir nesnenin 'int' olup olmadigin kontrol etme:
"""

x = 200
print(isinstance(x, int))
print(isinstance(myobj, myclass))
print(isinstance(x, str))
