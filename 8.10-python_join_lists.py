#Join Lists

#Join Two Lists

"""
Python' da iki veya daha fazla listeyi birlestirmenin birkac yolu vardir.

En kolay yollarindan biri '+' operatorunu kullanmaktir.

Iki listeyi birlestirme:
"""

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


"""
Iki listeyi birlestirmenin bir baska yolu da list2'deki tum ogeleri list1' e
tek tek eklemektir.

list2' yi list1' e ekleme:
"""

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)



"""
Veya bir listeden baska bir listeye oge eklemek icin 'extend()' metodunu
kullanabilirsiniz.

'extend()' metodunu kullanarak list2' yi list1' in sonuna ekleme:
"""

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
