#Escape Character

"""
* Bir dizeye yazilmayacak karakter eklemek icin kacis karakter(\) kullanilir.

* Kacis karakterini kullanmak icin bir \ ve ardina kullanmak istedigimiz
  karakteri yazariz.

* Ornegin bir dizeye cift tirnak karakterini eklemek istersek backslash ile
  birlikte kullanmamiz gerekir. Aksi halde derleyici hata verebilir.
"""


#Double Quote

txt = "We are the so-called \"Vikings\" from the north"
print(txt)


#Single Quote

txt = 'It\'s alright.'
print(txt)


#Backslash

txt = "This is will insert on \\ (backslash)."
print(txt)


#New Line

txt = "Hello\nWorld"
print(txt)


#Carriage Return

txt = "Hello\rPython!"
print(txt)


#Tab

txt = "Hello\tWorld!"
print(txt)


#Octal Value

"""
Bir backslash(\) karakterinin ardindaki 3 integer bir octal(sekizlik) sayiyi
temsil eder.
"""

txt = "\110\145\154\154\157"
print("Octal Conversion:", txt)


#Hex value

"""
Bir backslash(\) karakterinin ardina 'x' ve bir 'hex' sayi gelmesi bir hex
degeri temsil eder.
"""

txt = "\x48\x65\x6c\x6c\x6f"
print("Hex Conversion:", txt)









































