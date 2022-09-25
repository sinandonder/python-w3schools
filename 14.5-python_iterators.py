#Python Iterators

"""
Iterator, sayilabilir sayida deger iceren bir nesnedir.

Iterator, yinelenebilen bir nesnedir, yani tum degerler arasinda gecis 
yapabilirsiniz.

Teknik olarak, Python'da bir iterator __iter__() ve __next__() metodlarindan 
olusan yineleyici protokolunu uygulayan bir nesnedir.
"""


#Iterator vs Itarable

"""
Listeler, tuple'lar, sozlukler ve kumelerin tumu yinelenebilir nesnelerdir. Bir
iterator alabileceginiz yinelenebilir kaplardir.

Tum bu nesnelerin bir iterator elde etmek icin kullanilan bir iter() metodu
vardir.

Tuple'dan bir iterator dondurun ve her degeri yazdirin:
"""

mytuple = ("apple", "banana", "cherry")
myiter = iter(mytuple)

print(next(myiter))
print(next(myiter))
print(next(myiter))

"""
Stringler bile yinelenebilir nesnelerdir ve bir iterator dondurebilir.

Stringler ayrica bir dizi karakter iceren yinelenebilir nesnelerdir:
"""

mystr = "banana"
myiter = iter(mystr)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


#Looping Through an Iterator

"""
Yinelenebilir bir nesneyi yineleme icin bir for dongusude kullanabiliriz.

Bir tuple'in degerlerini yineleme:
"""

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)


"""
Bir stringin karakterlerini yineleme:
"""

mystr = "banana"

for x in mystr:
    print(x)


"""
Aslinda for dongusu bir iterator nesnesi olusturur ve her dongude next() 
metodunu yurutur.
"""


#Create an Iterator

"""
Iterator olarak bir nesne/sinif olusturmak icin nesnenize __iter__() ve
__next__() metodlarini uygulamaniz gerekir.

Python siniflar/nesneler bolumunde ogrendiginiz gibi, tum siniflarin __init__()
adinda bir fonksiyonu vardir ve bu, nesne olusturulurken cagrilir.

__iter__() metodu benzer davranir, islemler yapabilirsiniz(initializing vb.),
ancak her zaman iterator nesnenin kendisini dondurmeniz gerekir.

__next__() metodu ayrica islem yapmanizi saglar ve siradaki bir sonraki ogeyi
dondurmesi gerekir.

1 ile baslayip birer birer artan sayilari donduren bir iterator olusturma:
"""

class Mynumbers:
    
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = Mynumbers()
myiter = iter(myclass)


print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
    

#StopIteration

"""
Yeterli next() ifadeniz varsa veya bir for dongusunde kullanilmissa, yukaridaki
ornek sonsuza kadar devam eder.

Yinelemenin sonsuza kadar devam etmesini onlemek icin StopIteration ifadesini
kullanabiliriz.

__next__() metodunda, yineleme belirli sayida yapilirsa bir hata olusturmak icin
bir sonlandirma kosulu ekleyebiliriz.

20 yinelemeden sonra dur:
"""

class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = Mynumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
