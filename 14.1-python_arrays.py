#Python Arrays

"""
Python' un diziler icin build-in(yerlesik) destegi yoktur, ancak bunun yerine 
Python Listeleri kullanilabilir.
"""


#Arrays

"""
Diziler bircok degeri tek bir degiskende saklamak icin kullanilir.

Araba adlarini iceren bir dizi olusturun:
"""

cars = ["Ford", "Volvo", "BMW"]


#What is an Array?

"""
Dizi, ayni anda birden fazla degeri tutabilen ozel bir degiskendir.

Bir oge listeniz varsa(Ornegin bir araba adlari listesi), arabalari tek
degiskenlerde depolamak soyle gorunebilir:
"""

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

"""
Ancak arabalar arasinda dolasmak ve belirli bir tane bulmak isterseniz ne olur?
Peki ya 3 degilde 300 arabaniz olsaydi?
Cozum bir dizidir.

Bir dizi tek bir ad altinda bircok degeri tutabilir ve bir index numarasina
basvurarak erisebilirsiniz.
"""

#Access the Elements an an Array

"""
Index numarasi ile bir dizi ogesine ulasabilirsiniz.

Ilk dizi ogesinin degerini alma:
"""

cars = ["Ford", "Volvo", "BMW"]

x = cars[0]


"""
Ilk dizi ogesinin degerini degistirme:
"""

cars[0] = "Toyota"


#The Length of an Array

"""
len() metodunu kullanarak dizinin uzunlugunu bulabilirsiniz(dizideki ogelerin 
sayisi).

cars dizisindeki ogelerin sayisini dondurme:
"""

x = len(cars)
print(x)

"""
Bir dizinin uzunlugu her zaman en yuksek dizi index'inden bir fazladir.
"""


#Looping Array Elements

"""
Bir dizinin tum ogeleri arasinda dongu yapmak icin 'for in' dongusunu
kullanabilirsiniz.

cars dizisindeki her bir ogeyi yazdirin:
"""

for x in cars:
    print(x)


#Adding Array Elements

"""
append() metodunu kullanarak bir diziye eleman ekleyebilirsiniz.
cars dizisine bir eleman daha ekleme:
"""

cars.append("Honda")
print(cars)


#Removing Array Elements

"""
Diziden bir ogeyi kaldirmak icin pop() metodunu kullanabilirsiniz.
cars dizisinin ikinci ogesini silme:
"""

cars.pop(1)
print(cars)


"""
Diziden bir ogeyi kaldirmak icin remove() metodunu da kullanabilirsiniz.

'Toyota' degerine sahip ogeyi silme:
"""

cars.remove("Toyota")
print(cars)

"""
Not: remove() metodu yalnizca ilk gordugu degeri siler.
"""