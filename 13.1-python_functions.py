#Python Functions

"""
Fonksiyon, yalnizca cagrildiginda calisan bir kod blogudur.
Pametre olarak bilinen verileri bir fonksiyona gecirebilirsiniz.
Bir fonksiyon, sonuc olarak bir veri dondurebilir.
"""


#Creating a Function

"""
Python' da 'def' keyword'u kullanilarak bir fonksiyon tanimlanir.
"""


def my_function():
    print("Hello from a function")


#Calling a Function

"""
Bir fonksiyonu cagirmak icin, fonksiyon adini ve ardindan parantez kullanin.
"""

def my_function():
    print("Hello from a function 2")

my_function()

"""
Not: Ayni fonksiyon isminden birden fazla var ise son fonksiyonu esas alir.
"""


#Arguments

"""
Bilgiler, arguman olarak fonksiyona aktarilabilir.

Argumanlar, fonksiyon adindan sonra parantez icinde belirtilir. Virgul ile
ayirarak, istediginiz kadar arguman ekleyebilirsiniz.

Asagidaki ornekte tek argumana sahip bir fonksiyon vardir. Fonksiyon 
cagrildiginda, fonksiyonun icerisine tam adi yazdirmak icin bir ad iletiyoruz.
"""

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

"""
Python dokumantasyonunda argumanlar genellikle 'args' olarak kisaltilir.
"""


#Parameters or Arguments?

"""
Parametre ve arguman terimleri ayni sey icin kullanilabilir: bir fonksiyona
aktarilan bilgiler.

Bir fonksiyonun bakis acisindan:
Parametre, fonksiyon taniminda parantez icinde listelenen degiskendir.
Arguman, fonksiyon cagrildiginda fonksiyona gonderilen degerdir.
"""


#Number of Arguments

"""
Varsayilan olarak, dogru sayida arguman ile bir fonksiyon cagrilmalidir. Yani,
fonksiyonunuz 2 arguman bekliyorsa, fonksiyonu 2 argumanla cagirmalisiniz, ne 
daha fazlasi ne de daha azi.

Bu fonksiyon 2 arguman bekler ve 2 arguman alir:
"""

def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")

"""
Fonksiyonu 1 veya 3 argumanla cagirmaya calisirsaniz bir hata alirsiniz.
"""


def my_function(fname, lname):
    print(fname + " " + lname)


#my_function("Emil") #Hataya neden olacaktir.


#Arbitrary Arguments, *args

"""
Fonksiyonunuza kac tane arguman iletilecegini bilmiyorsaniz, fonksiyon taniminda
parametre adindan once bir * ekleyin.

Bu sekilde fonksiyon bir tuple olarak argumanlar alacak ve buna gore ogelere
erisebilecek.

Arguman sayisi bilinmiyorsa parametre adindan once bir * ekleyin:
"""

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

"""
Arbitrary argumanlar Python dokumantasyonunda genellikle *args olarak 
kisaltilir.
"""


#Keyword Arguments

"""
Ayrica key = value sozdizimini ile bagimsiz degiskenler gonderebilirsiniz.
Bu sekilde argumanlarin sirasi onemli degildir.
"""

def my_function(child1, child2, child3):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")

"""
Keyword Arguments ifadesi Python dokumantasyonunda genellikle kwarg olarak
kisaltilir.
"""


#Arbitrary Keyword Arguments, **kwargs

"""
Fonksiyonunuza kac tane keyword argumaninin iletilecegini bilmiyorsaniz,
fonksiyon taniminda parametre adindan once ** isareti ekleyin.

Bu sekilde fonksiyon, bir arguman sozlugu alacak ve buna gore ogelere
erisebilecektir.

Keyword argumanlarinin sayisi bilinmiyorsa, parametre adindan once bir cift **
ekleyin:
"""

def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


"""
Arbitrary Kword Argumanlari Python dokumantasyonunda genellikle **kwargs olarak
kisaltilir.
"""


#Default Parameter Value

"""
Asagidaki ornek, varsayilan bir parametre degerinin nasil kullanilacagini
gosterir.
Fonksiyonu argumansiz cagirirsak varsayilan degerini kullanir:
"""

def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


#Passing a List as an Argument

"""
Bir fonksiyona herhangi bir veri tipi arguman gonderebilirsiniz(string, number,
list, dictionary vb.) ve fonksiyon icinde ayni veri tipi olarak ele alinacaktir.

Ornegin arguman olarak bir liste gonderirseniz, fonksiyona ulastiginda hala bir
liste olacaktir.
"""

def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


#Return Values

"""
Bir fonksiyonun bir deger gondermesine izin vermek icin 'return' ifadesini
kullanin.
"""


def my_function(x):
    return x * 5


print(my_function(3))
print(my_function(5))
print(my_function(9))


#The pass Statement

"""
Fonksiyon tanimlari bos olamaz, ancak herhangi bir nedenle icerigi olmayan bir
fonksiyon taniminiz varsa, hata almamak icin pass ifadesini girin.
"""

def my_function():
    pass


#Recursion

"""
Python ayrica fonksiyon ozyinelemesini de kabul eder, bu tanimlanmis bir
fonksiyonun kendisini cagirabilecegi anlamina gelir.

Ozyineleme, ortak bir matematik ve programlama kavramidir. Bu bir fonksiyonun
kendisini cagirdigi anlamina gelir. Bu bir sonuca ulasmak icin veriler arasinda
dolacabileceginiz anlamina gelir.

Gelistirici ozyineleme konusunda cok dikkatli olmalidir, cunku hicbir zaman sona
ermeyen veya asiri miktarda bellek ya da islemci gucu kullanan bir fonksiyon
yazmak oldukca kolay olabilir. Bununla birlikte, dogru yazildiginda ozyineleme,
programlama icin cok verimli ve matematiksel olarak zarif bir yaklasim olabilir.

Bu ornekte, tri_recursion(), kendisini cagirmak("recurse") icin tanimladigimiz
bir fonksiyondur. Veri olarak 'k' degiskenini kullaniriz ve bu, her 
tekrarladigimizda -1 azalir. Ozyineleme, kosul 0'dan buyuk olmadiginda yani 0
oldugunda sona erer.
"""


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0

    return result


print("\n\nRecursion Example Results")
tri_recursion(5)



def factorial(n):
    if n > 1:
        result = n * factorial(n - 1)
        print(result)
    else:
        result = 1

    return result


print("\n\nRecursion Factorial Example")
factorial(6)