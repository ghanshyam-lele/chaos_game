from Tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sin
import random
import threading
import time
WIDTH, HEIGHT = 640, 480

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

a = (120,120)
b = (576,240)
c = (455,444)
array=[a,b,c]
img.put("#ffffff", a)
img.put("#ffffff", b)
img.put("#ffffff", c)

start=(300,300)
img.put("#ffffff",start)


def play():
    global start
    while True:
        ch = random.choice(array)
        point = ((start[0]+ch[0])/2,(start[1]+ch[1])/2)
        img.put("#ffffff", point)
        start=point;
        time.sleep(0.05)
t= threading.Thread(target=play)
t.start()

mainloop()