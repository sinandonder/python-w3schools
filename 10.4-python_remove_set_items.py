#Remove Set Items

#Remove Item

"""
Set' ten bir ogeyi kaldirmak icin 'remove()' veya 'discard()' metodlarini
kullanabilirsiniz.

'remove()' metodunu kullanarak 'banana' yi kaldirma:
"""

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")

print(thisset)

"""
Not: Kaldirilacak oge yoksa, 'remove()' hataya neden olacaktir.
"""


"""
'discard()' metodunu kullanarak 'banana' yi kaldirma:
"""

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")

print(thisset)

"""'
Not: Kaldirilacak oge yoksa, 'discard()' hataya sebep olmayacaktir.
"""


"""
Ayrica 'pop()' metodunu kullanarak da bir oge kaldirabilirsiniz, ama bu metot
son ogeyi kaldirir. Setlerin sirasiz oldugunu unutmayin, bu nedenle hangi ogenin
kaldirildigini bilemezsiniz.

'pop()' metodunun donus degeri kaldirilan ogedir.

'pop()' metodunu kullanarak son ogeyi kaldirma:
"""

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)
print(thisset)

"""
Not: Set' ler sirasizdir, bu nedenle pop() metodunu kullanirken hangi ogenin
kaldirildigini bilemezsiniz.
"""

#Clear the Set

"""
'clear()' metodu Set' in icini bosaltir:
"""

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


"""
'del' keyword' u Set' i tamamen silecektir.
"""

thisset = {"apple", "banana", "cherry"}

del thisset

#print(thisset) #Set silindigi icin hataya neden olacaktir.
