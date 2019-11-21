from tkinter import * 
import sys
import os
from sqllite import *
from functools import partial 

block1=200-count_one()
block34=200-count_34()
block55=200-count_55()
block49=200-count_49()
# print(block1,block34,block49,block55)

def back():
    window.destroy()
    os.system('python3 index.py')     

window=Tk()
window.geometry('400x400+100+200')
window.title('Parking Available') 

L1 = Label(window, text="Block 1:")
L1.grid(row=1,column=1)

L11 = Label(window, text=block1)
L11.grid(row=1,column=2)



L2 = Label(window, text="Block 49: ")
L2.grid(row=2,column=1)

L22 = Label(window, text=block34)
L22.grid(row=2,column=2)

L3 = Label(window, text="Block 34: ")
L3.grid(row=3,column=1)

L33 = Label(window, text=block55)
L33.grid(row=3,column=2)

L4 = Label(window, text="Block 55: ")
L4.grid(row=4,column=1)

L44 = Label(window, text=block55)
L44.grid(row=4,column=2)

b1 = Button(window, text="Back",
            bg="blue", fg="white", command=back)

b1.grid(row=5, column=2)





























window.mainloop()