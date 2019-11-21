from tkinter import * 
import sys
import os
from sqllite import *
from functools import partial 
from tkinter.messagebox import showinfo


window=Tk()
window.geometry('400x400+100+200')
window.title('Parking Request') 

L1 = Label(window, text="Reg No: ")
L1.grid(row=0,column=1)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=2)


L2 = Label(window, text="Username:")
L2.grid(row=2,column=1)
e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=2,column=2)

variable = StringVar(window)
variable.set(1) 

L3 = Label(window, text="Block: ")
L3.grid(row=3,column=1)

w = OptionMenu(window, variable, 1, 49, 34, 55)
w.grid(row=3,column=2)

L4 = Label(window, text="Price: ")
L4.grid(row=4,column=1)

variable1 = StringVar(window)
variable1.set(3000)
w1 = OptionMenu(window, variable1,3000)
w1.grid(row=4,column=2)



def submit(n1,n2,n3):
    num1 = (n1.get())
    num2 = (n2.get())
    num3 = (n3.get())
    print(num1,num2,num3)
    insertparking(num1,num2,num3)
    showinfo("Window","You have sucessfuly registered")
    window.destroy()
    os.system('python3 index.py') 
    
   
    


submit = partial(submit,e1_value,e2_value,variable)  



b1=Button(window,text='order',command=submit,bg="blue", fg="white")
b1.grid(row=5,column=2)




























window.mainloop()