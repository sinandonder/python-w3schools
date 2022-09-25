#Python Classes and Objects

#Python Classes/Objects

"""
Python, nesne yonelimli bir programlama dilidir.

Python'daki hemen hemen her sey, ozellikleri ve metodlari ile bir nesnedir.

Bir sinif, bir nesne olusturucu veya nesneler olusturmak icin bir 
"plan(blueprint)" gibidir.
"""

#Create a Class

"""
Bir sinif olusturmak icin 'class' keywordunu kullanin.

x adli bir ozellige sahip MyClass adli bir sinif olusturma:
"""


class MyClass():
    x = 5


#Create Object

"""
Artik nesneler olusturmak icin MyClass adli sinifi kullanabiliriz.

p1 adinda bir nesne olusturup x'in degerini yazdirma:
"""

p1 = MyClass()
print(p1.x)


#The __init__() Function

"""
Yukaridaki ornekler, en basit bicimleriyle siniflar ve nesnelerdir ve gerçek
hayattaki uygulamalarda pek kullanisli degildir.

Siniflarin ne oldugunu anlamak icin build-in __init__() fonksiyonunu anlamamiz
gerekir.

Tum siniflarin, sinif baslatirlirken her zaman yurutulen __init__() adli bir
fonksiyonu vardir.

Nesne ozelliklerine deger atamak veya nesne olusturuldugunda yapilmasi gereken
diger islemler icin __init__() fonksiyonu kullanilir.

Person adinda bir sinif olusturup, name ve age' e degerler atamak icin 
__init__() fonksiyonunu kullanalim:
"""

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


"""
Not: __init__() fonksiyonu, sinif yeni bir nesne olusturmak icin her 
kullanildiginda otomatik olarak cagrilir.
"""


#Object Metods

"""
Nesneler ayrica metodlar icerebilir. Nesneleredeki metodlar, nesneye ait olan 
fonksiyonlardir.

Person sinifinda bir metod olusturalim:
Bir selamlama yazdiran bir fonksiyon ekleyip bunu p1 nesnesinde yurutelim:
"""

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is", self.name)
    
    

p1 = Person("Anna", 36)
p1.myfunc()


#The self Parameter
"""
self parametresi, sinifin mevcut ornegine bir referanstir ve sinifa ait
degiskenlere erismek icin kullanilir.

self olarak adlandirilmasi gerekmez, istediginiz gibi adlandirabilirsiniz, ancak
siniftaki herhangi bir metodun ilk parametresi olmalidir.

self yerine mystillobject ve abc kelimelerini kullanalim:
"""


class Person():
    def __init__(mysillobject, name, age):
        mysillobject.name = name
        mysillobject.age = age
    
    def myfunc(abc):
        print("Hello my name is", abc.name)


p1 = Person("John", 36)
p1.myfunc()


#Modify Object Properties

"""
Asagidaki gibi nesnelerdeki ozellikleri degistirebilirsiniz:

p1 yasini 40 olarak ayarlama:
"""

p1.age = 40


#Delete Object Properties

"""
del keyword' unu kullanarak nesnelerdeki ozellikleri silebilirsiniz.
"""

del p1.age


#Delete Objects

"""
del keyword' unu kullanarak nesneleri silebilirsiniz.

p1 nesnesini silme:
"""

del p1


#The Pass Statement

"""
Sinif tanimlari bos olamaz, ancak herhangi bir nedenle icerigi olmayan bir sinif
taniminiz varsa, hata almamak icin pass ifadesini girin.
"""

class Person():
    pass