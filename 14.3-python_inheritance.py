#Python Inheritance

"""
Kalitim, tum metodlari ve ozellikleri baska bir siniftan miras alan bir sinif
tanimlamamizi saglar.

Parent class(ust sinif), base class olarak da adlandirilan, miras alinan 
siniftir.

Child class(alt sinif), turetilmis sinif olarak da adlandirilan baska bir
siniftan miras alan siniftir.
"""

#Create a Parent Class

"""
Herhangi bir sinif üst sinif olabilir, bu nedenle sozdizimi baska bir sinif
olusturmakla aynidir.

firstname ve lastname ozelliklerine ve bir printname metoduna sahip Person adli
bir sinif olusturma:
"""

class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


#Person class' ini kullanarak nesne olusturup, printname metodunu calistiralim:

x = Person("John", "Doe")
x.printname()


#Create a Child Class

"""
Fonksiyonelligi baska bir siniftan devralan bir sinif olusturmak icin, alt 
sinifi olustururken ust sinifi parametre olarak gonderin.

Person sinifindan ozellikleri ve metodlari devralacak olan Student adli bir
sinif olusturma:
"""

class Student(Person):
    pass

"""
Not: Sinifa baska bir ozellike veya metod eklemek istemiyorsaniz pass 
keyword'unu kullanin.

Artik Student sinifi, Person sinifiyla ayni ozelliklere ve metodlara sahiptir.

Bir nesne olusturmak icin Student sinifini kullanip ve ardindan printname
metodunu calistirma:
"""

s = Student("Mike", "Olsen")
s.printname()


#Add the __init__() Function

"""
Simdiye kadar, ozelliklerini ve metodlarini ebeveyninden miras alan bir alt
sinif olusturduk.

Alt sinifa pass keyword'u yerine __init__() fonksiyonunu eklemek istiyoruz.

Not: __init__() fonksiyonu, sinif bir nesne olusturmak icin her kullanildiginda
otomatik olarak cagrilir.

Student sinifina __init__() fonksiyonunu ekleme:
"""

class Student(Person):
    def __init__(self, fname, lname):
        pass


"""
__init__() fonksiyonunu eklediginizde, cocuk sinif artik ebeveyninin __init__()
fonksiyonunu devralmaz.

Not: Cocuk sinifin __init__() fonksiyonu, ebeveynin __init__() fonksiyonunun
mirasini gecersiz kilar(override).

Ebeveynin __init__() fonksiyonunun mirasini korumak icin, cocuk sinifta 
ebeveynin __init__() fonksiyonunu cagirin.
"""


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)



s = Student("Sinan", "Dönder")
s.printname()


"""
Simdi __init__() fonksiyonunu basariyla ekledik ve ust sinifin mirasini koruduk
ve __init__() fonksiyonuna islevsellik elemeye haziriz.
"""

#Use the super() Function()

"""
Python ayrica, alt sinifin ebeveyninden tum metodlari ve ozellikleri miras
almasini saglayacak bir super metoduna sahiptir.
"""

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


"""
super() fonksiyonunu kullanarak, ust sinifin adini kullanmak gerekmeden, 
metodlari ve ozellikleri ust siniftan otomatik olarak alabilirsiniz.
"""

#Add Properties

"""
Student sinifina graduationyear adli bir ozellik ekleme:
"""

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019


"""
Asagidaki ornekte, 2019 yili bir degisken olmali ve ogrenci nesneleri
olustururken Student sinifina aktarilmalidir. Boyle yapmak icin __init__()
fonksiyonuna baska bir parametre ekleyin.

year parametresi ekleyip nesneleri olusturuken istenen yili iletme:
"""

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

x = Student("Mike", "Olsen", "2022")


#Add Methods

"""
Student sinifina welcome adli bir metod ekleme:
"""

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of",
        self.graduationyear)


s = Student("Mike", "Olsen", "2022")
s.welcome()

"""
Alt sinifa, ust siniftaki bir metodla ayni ada sahip bir metod eklerseniz, ust
metodun mirasi gecersiz kilinir(override).
"""


"""
Not: Alt siniftan olusturulan bir nesne ust sinifin bir ornegidir ancak ust
siniftan olusturulan bir nesne alt sinifin bir ornegi degildir.
"""

class Person():
    pass

class Student(Person):
    pass


p = Person()
s = Student()

print(isinstance(p, Person))
print(isinstance(p, Student))
print(isinstance(s, Person))
