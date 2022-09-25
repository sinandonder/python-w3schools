#Python Lists

"""
Listeler bircok ogeyi tek bir degiskende saklamak icin kullanilir.

Listeler, Python'da veri koleksiyonlarini saklamak icin kullanilan 4 built-in
(yerlesik) veri turunden biridir. Diger 3' u Tuple, Set ve Dictionary'dir ve 
tumu farkli niteliklere ve kullanima sahiptir.

Listeler koseli parantezler kullanilarak olusturulur.
"""

thislist = ["apple", "banana", "cherry"]
print(thislist)


#List Items

"""
Liste ogeleri sıralanır, degistirilebilir ve yinelenen degerlere izin verir.

Liste ogeleri indexlidir, ilk ogenin indexi [0], ikinci ogenin indexi [1] vb.
"""


#Ordered

"""
Listeler siralanir dedigimizde, ogelerin belirli bir siraya sahip oldugu ve bu
siranin degismeyecegi anlamina gelir.

Bir listeye yeni bir oge eklerseniz, yeni oge listenin sonuna konumlanir.

Not: Siralamayi degistirecek bazi liste metodlari vardir, ancak genel olarak
ogelerin sirasi degismez.
"""


#Changeable

"""
Liste degistirilebilir, yani bir liste olusturulduktan sonra degistirilebilir,
ekleyebilir, ve kaldirabiliriz.
"""


#Allow Duplicate

"""
Listeler indexlendiginden, ayni degerden ogelere sahip olabilir.
"""

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


#List Length

"""
Bir listenin kac ogeye sahip oldugunu belirlemek icin 'len()' fonksiyonu
kullanilir.
"""

thislist = ["apple", "banana", "cherry"]
print(len(thislist))


#List Items - Data Types

"""
Liste ogeleri herhangi bir veri tipi olabilir.
"""

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


"""
Bir liste farkli veri tipleri icerebilir.
"""

list4 = ["abc", 34, True, 40, "male"]


#type()

"""
Python'un bakis acisindan, listeler 'list' veri tipine sahip nesneler olarak
tanimlanir.
"""

mylist = ["apple", "banana", "cherry"]
print(type(mylist))


#The list() Constructor

"""
Ayrica 'list()' kurucusunu kullanarak yeni bir liste olusturulabiliriz.

list() kurucusunu kullanarak liste olusturma:
"""

thislist = list(("apple", "banana", "cherry")) # iki parantezle olusturulur(!)
print(thislist)


#Python Collections (Arrays)

"""
Python programlama dilinde 4 koleksiyon veri tipi vardır:

* list: Liste, sirali ve degistirilebilir bir koleksiyondur. Yinelenen uyelere
  izin verir.
  
* tuple: Tuple, sirali ve degistirilemez bir koleksiyondur. Yinelenen uyelere
  izin verir.
  
* set: Set, sirasiz ve indexlenmemis bir koleksiyondur. Yinelenen uyelere izin
  vermez.
  
* dictionary: Dictionary: sirali* ve degistirilebilir bir koleksiyondur.
  Yinelenen uyelere izin vermez.
  
  *Python 3.7 surumunden itibaren sozlukler siralanmistir. Python 3.6 ve onceki
  surumlerde sozlukler sirasizdir.
"""


"""
Not: Bir koleksiyon turu secerken, o turun ozelliklerini anlamakta fayda var.
Belirli bir veri kumesi icin dogru turun secilmesi, anlamın korunmasi
anlamina gelebilir ve bu, verimlilik veya guvenlikte bir artis anlamina
gelebilir.
"""



































