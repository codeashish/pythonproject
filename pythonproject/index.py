from tkinter import *
import sys
import os
from sqllite import *
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
def login():
    window.destroy()
    os.system('python3 login.py')       
def registor():
    window.destroy()
    os.system("python3 registor.py")
def parkingavail():
    window.destroy()
    os.system("python3 parkingavail.py")
window = Tk()
window.geometry('300x300+100+200')
window.title('Parking  App')

b1 = Button(window, text='Login', bg="blue", fg="white", command=login)
b1.grid(row=20, column=0)

b2 = Button(window, text='New User', bg="blue", fg="white", command=registor)
b2.grid(row=4, column=3)

b3 = Button(window, text="Available parking",
            bg="blue", fg="white", command=parkingavail)
b3.grid(row=20, column=5)
window.mainloop()








