"""
Python' da stringler tek tirnaklarla veya cift tirnaklarla cevrilidir.

'hello' veya "hello" ayni seyi ifade eder.

"""

a = "Hello"

print(a)


#Multiple Strings

"""
Uc tirnak kullanarak bir degiskene cok satirli stringi esitleyebiliriz.
Not: Satir sonlari koddaki ile ayni konuma eklenir.
"""

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(b)


#Looping Through a String

"""
Stringler diziler gibi oldugundan bir for dongusuyle icerisinde gezinebiliriz.
"""

for x in "banana":
    print(x)


#String Length

"""
Bir stringin uzunlugunu 'len()' fonksiyonu ile getirebiliriz.
"""

a = "Hello, World!"
print(len(a))


#Check String

"""
Bir string de belirli bir kelime obegi veya karakter olup olmadigini kontrol
etmek icin 'in' anahtar kelimesini kullanabiliriz.
"""

txt = "The best things in life are free!"
print("free" in txt)


if "free" in txt:
    print("Yes, 'free' is present.")


#Check if NOT

"""
Bir string de belirli bir kelime obegi veya karakter olup olmadigini kontrol
etmek icin 'not in' anahtar kelimesini kullanabiliriz.
"""

txt = "The best things in life are free!"
print("expensive" not in txt)


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")













































