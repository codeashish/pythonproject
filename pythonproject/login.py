from tkinter import * 
import sys
import os
from sqllite import *
from functools import partial 
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image

def signup():
    window.destroy()
    os.system('python3 registor.py')

def back():
    window.destroy()
    os.system('python3 index.py')   
    
window=Tk()
window.geometry('300x300+100+200')
window.title('Login Page')  
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



L3 = Label(window, text="Password:  ")
L3.grid(row=3,column=1)
e3_value=StringVar()
e3=Entry(window,textvariable=e3_value,show="*")
e3.grid(row=3,column=2)




def submit(n1,n2,n3):
    num1 = (n1.get())
    num2 = int(n2.get())
    num3=(n3.get())
    print(num1,num2,num3)
    passw=search(num1)
    regno=search_park(num1)
    blockno=str(block(regno))
    print(blockno)

    print(regno,num2)
    print(regno)
    print(type(regno))
    print(type(num2))
    if(passw==num3):
          if(num2==regno):
            showinfo("Window", "You have  take parking option")
            imz = Image.open('download.jpeg')
            im = imz.resize((297, 200), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(im)
            img = Label(window, image=render)
            img.image = render
            img.place(x=0, y=0)
            welcome="Welcome "+ num1 +"\nYou have take block "+ blockno +"\nfor parking" 
            msg = Message(window,width=200 ,text = welcome)  
            msg.place(x=100,y=210)
          else:
            window.destroy()
            os.system("python3 parkingreq.py")
            

        
        
    else:
         showinfo("Window","Wrong credientials")
submit = partial(submit,e1_value,e2_value,e3_value)  

b1=Button(window,text='Login Now',command=submit,bg="blue", fg="white")
b1.grid(row=4,column=2)


b2=Button(window,text='New User',command=signup,bg="blue", fg="white")
b2.grid(row=5,column=2)





window.mainloop()

