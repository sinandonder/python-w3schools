"""print("sinan".count('n'))


a = int()

print(a)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.append(list2)
print(list1)

list1 = [1, 2, 3]
list1.extend(list2)
print(list1)


list2.extend(list1)
print(list2)
list2.sort()
print(list2)



name = "Sinan"
age = 25

combine = f"{name}{age}"
print(combine)
print(name + str(age))


txt = "Hello\rWorld!"
print(txt)

import sys
print(sys.version)


my_tuple = (1, 2)

var1, var2 = my_tuple

print(var1, var2)



a = 10
b = 20

if a < 10 | b > 10:
    print("in the if")


def sqrt(n):
    print(n)
    return n * n

list1 = [sqrt(x) for x in range(10)]
print(list1)


def my_func():
    global y
    y = "awesome"
    print(y)

my_func()
print(y)


a = range(1, 10, 3)

a_l = list(a)
print(a_l)
"""





"""file = open("style.css", "r")
text = file.read()
file.close()

print(text)
print(type(text))
print(len(text))"""














"""from gtts import gTTS


mytext = "against"
language = "en"


obj = gTTS(text=mytext, lang=language, slow=False)

obj.save("test.mp3")"""





"""
def toplam(n):
    return (n * (n + 1)) / 2

print(toplam(n=12))"""


"""def my_function(*args, name, surname):
    print(args[0] + name + surname)



my_function("a", "b", name="hello", surname="dear")"""



"""class Person():
    population = 50



p = Person()

p.population = 30

print(p.population)"""


"""li = [x for x in range(1, 11)]

print(li)
li = [x ** 2 for x in li if x % 2 == 0]


print(li)

import time

start = time.time()

li = [x for x in range(1, 100000001)]

finish = time.time()

print("Geçen Süre", (finish - start))

#li = [x ** 2 if x % 2 == 0 else x for x in li]

#print(li)"""




import numpy as np
import cv2
import time
 
 
"""# creating the videocapture object
# and reading from the input file
# Change it to 0 if reading from webcam
 
cap = cv2.VideoCapture(0)
 
# used to record the time when we processed last frame
prev_frame_time = 0
 
# used to record the time at which we processed current frame
new_frame_time = 0
 
# Reading the video file until finished
while(cap.isOpened()):
 
    # Capture frame-by-frame
 
    ret, frame = cap.read()
 
    # if video finished or no Video Input
    if not ret:
        break
 
    # Our operations on the frame come here
    gray = frame
 
    # resizing the frame size according to our need
    gray = cv2.resize(gray, (500, 300))
 
    # font which we will be using to display FPS
    font = cv2.FONT_HERSHEY_SIMPLEX
    # time when we finish processing for this frame
    new_frame_time = time.time()
 
    # Calculating the fps
 
    # fps will be number of frame processed in given time frame
    # since their will be most of time error of 0.001 second
    # we will be subtracting it to get more accurate result
    fps = 1/(new_frame_time-prev_frame_time)
    prev_frame_time = new_frame_time
 
    # converting the fps into integer
    fps = int(fps)
 
    # converting the fps to string so that we can display it on frame
    # by using putText function
    fps = str(fps)
 
    # putting the FPS count on the frame
    cv2.putText(gray, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)
 
    # displaying the frame with fps
    cv2.imshow('frame', gray)
 
    # press 'Q' if you want to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
# Destroy the all windows now
cv2.destroyAllWindows()"""









from tkinter import *
from tkinter import ttk
import threading

def func1():
    while True:
        print("1")

def func2():
    while True:
        print("2")
        

def func3():
    while True:
        print("3")
        

def func4():
    while True:
        print("4")
        

def func5():
    while True:
        print("5")
        

def func6():
    while True:
        print("6")

def func7():
    while True:
        print("7")
        


def start_func():
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t3 = threading.Thread(target=func3)
    t4 = threading.Thread(target=func4)
    t5 = threading.Thread(target=func5)
    t6 = threading.Thread(target=func6)
    t7 = threading.Thread(target=func7)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()



root = Tk()

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="func", command=start_func).grid(column=1, row=1)
root.mainloop()


