#Change Item Value

"""
Belirli bir ogenin degerini degistirmek icin, index numarasina bakin.

Ikinci ogeyi degistirme:
"""

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#Change a Range of Item Values

"""
Belirli bir araliktaki ogelerin degerini degistirmek icin, yeni degerlerle bir
liste tanimlayin ve yeni degerleri eklemek icin istediginiz index araligina
bakin.

"banana" ve "cherry" degerlerini "blackcurrant" ve "watermelon" ile degistirme:
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


"""
Degistirdiginizden daha fazla oge eklerseniz, yeni ogeler belirttiginiz yere
eklenir ve kalan ogeler buna gore hareket eder.

Ikinci degeri, iki yeni degerle degistirme:
"""

thislist = ["apple", "banana", "cherry"]
thislist[1:2]  = ["blackcurrent", "watermelon"]
print(thislist)


"""
Not: Eklenen ogelerin sayisi degisen ogelerin sayisiyla eslesmediginde
listenin uzunlugu degisecektir.

Degistirdiginizden daha az oge eklerseniz, yeni ogeler belirttiginiz yere
eklenir kalan ogeler buna gore hareket eder:
"""

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


#Insert Items

"""
Mevcut degerlerden herhangi birini degistirmeden yeni bir liste ogesi
eklemek icin 'insert()' metodunu kullanabilirsiniz.

Ucuncu eleman olarak "watermelon" ekleme:
"""

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

"""
Not: yukaridaki ornekte, liste artık 4 oge icerektir.
"""
