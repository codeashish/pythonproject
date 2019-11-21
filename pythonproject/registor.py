from tkinter import * 
import sys
import os
from sqllite import *
from functools import partial  
from tkinter.messagebox import showinfo


window=Tk()
window.geometry('500x500+100+200')
window.title('Registor Page')  
L1 = Label(window, text="User Name: ")
L1.grid(row=0,column=1)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=2)

L2 = Label(window, text="Reg No:  ")
L2.grid(row=2,column=1)
e2_value=StringVar()

e2=Entry(window,textvariable=e2_value)
e2.grid(row=2,column=2)

L3 = Label(window, text="Hostel/Block : ")
L3.grid(row=3,column=1)
e3_value=StringVar()
e3=Entry(window,textvariable=e3_value)
e3.grid(row=3,column=2)



L4 = Label(window, text="Gender:  ")
L4.grid(row=4,column=1)
radio = IntVar()
c1 = Radiobutton(window, text="Male", variable=radio,value = 0)
c1.grid(row=4,column=2)

c2 = Radiobutton(window, text="female", variable=radio,value = 1)
c2.grid(row=4,column=3)


L5 = Label(window, text="Mobile No : ")
L5.grid(row=5,column=1)
e5_value=StringVar()
e5=Entry(window,textvariable=e5_value)
e5.grid(row=5,column=2)


L6 = Label(window, text="Email Id : ")
L6.grid(row=6,column=1)
e6_value=StringVar()
e6=Entry(window,textvariable=e6_value)
e6.grid(row=6,column=2)

L7 = Label(window, text="Password : ")
L7.grid(row=7,column=1)
e7_value=StringVar()
e7=Entry(window,textvariable=e7_value,show="*")
e7.grid(row=7,column=2)




def submit(n1,n2,n3,n4,n5,n6,n7):
    num1 = (n1.get())
    num2 = int((n2.get()))
    num3 = (n3.get()) 
    num4 = (n4.get())
    num5 = int((n5.get()))
    num6 = (n6.get()) 
    num7 = (n7.get()) 
    create_table()
    insert(num1,num2,num3,num4,num5,num6,num7)
    insertparking(133323,num1,3)
    print(view())
    showinfo("Window", "Sucessfully")
    window.destroy()
    os.system('python3 index.py')
   
    


submit = partial(submit,e1_value,e2_value,e3_value,radio,e5_value,e6_value,e7_value)  


b3=Button(window,text="Submit", bg="blue", fg="white",command=submit)
b3.grid(row=8,column=2)


window.mainloop()