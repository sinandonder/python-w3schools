
"""
Bir degisken uzerinde bir tur belirtmek istedigimiz zamanlar olabilir. Bu 
'casting' (dokum) ile yapilabilir. Python, nesne yonelimli bir programlama
dilidir ve bu nedenle, ilkel turleri dahil olmak uzere veri turlerini 
tanimlamak icin siniflari kullanir.
"""


"""
Python' da casting bu nedenle kurucu metodlari kullanilarak yapilir.

int(): integer kurucu metodu, bir tamsayi degerinden, bir float degerinden 
(tum ondaliklari kaldirarak) veya bir string degerinden(dizenin bir tam 
sayiyi temsil etmesi kosuluyla ex: "203") bir tamsayi olusturur.

float(): float kurucu metodu, bir tamsayi degerinden, bir float degerinden
veya bir string degerinden ondalik sayi olusturur.(string' in bir ondalik veya
tam sayi temsil etmesi kosuluyla.)

str(): string kurucu metodu, metinler, tamsayi degerleri ve float degerleri
dahil olmak uzere cok cesitli veri turlerinden bir string olusturur.
"""


#Integers

x = int(1)   # 1 olacak
y = int(2.8) # 2 olacak
z = int("3") # 3 olacak


#Floats

x = float(1)     # 1.0 olacak
y = float(2.8)   # 2.8 olacak
z = float("3")   # 3.0 olacak
w = float("4.2") # 4.2 olacak


#Strings

x = str("s1") # 's1' olacak
y = str(2)    # '2' olacak
z = str(3.0)  # '3.0' olacak