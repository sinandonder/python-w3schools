#Access Set Items

#Access Items

"""
Bir Set' deki ogelere bir index veya key referansiyla erisemezsiniz.

Ancak bir 'for' dongusu kullanarak Set ogeleri arasinda dolasabilir veya in
anahtar sozcugunu kullanarak bir kumede belirli bir degerin olup olmadigini
sorabilirsiniz.

Dongu ile Set' deki degerleri yazdirma:
"""

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


"""
Set' de "banana" olup olmadigini kontrol etme:
"""

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


#Change Items

"""
Bir Set olusturulduktan sonra ogelerini degistiremezsiniz, ancak yeni ogeler
ekleyebilirsiniz.
"""