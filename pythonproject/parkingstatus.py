from tkinter import * 
import sys
import os
from sqllite import *
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo


window = Tk()
window.geometry('300x300+100+200')
window.title('Parking  App')
imz = Image.open('download.jpeg')
im = imz.resize((297, 200), Image.ANTIALIAS)
render = ImageTk.PhotoImage(im)
img = Label(window, image=render)

img.image = render
img.place(x=0, y=0)
msg = Message( window, text = "Welcome to Javatpoint")  
msg.place(x=100,y=210)

window.mainloop()