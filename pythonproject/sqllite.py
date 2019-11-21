import sqlite3

def create_table():
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute("create table if not exists register(username TEXT,regno INTEGER,hostel TEXT,gender NUMERIC,mobileno NUMERIC,emailid TEXT,password TEXT)")
    conn.commit()
    conn.close()

def insert(username,regno,hostel,gender,mobileno,emailid,password): 
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute("insert into register values(?,?,?,?,?,?,?)",(username,regno,hostel,gender,mobileno,emailid,password))
    conn.commit()
    conn.close()
        


def view():
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute("select * from  register")
    rows=cur.fetchall()
    return rows
    conn.close()

def delete():
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute("delete from register ")
    conn.commit()
    conn.close()

def search(usr):
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute('select password from register where username=?',(usr,))
    result=cur.fetchall()
    # return result
    x=result[0][0]
    return x

def count():
    conn=sqlite3.connect("project.db")
    cur=conn.cursor()
    cur.execute('select count(regno) from parking')
    count = cur.fetchone()
    number=count[0]
    return number
#parking table starts here

def create_parking():

    conn=sqlite3.connect("parking.db")
    cur=conn.cursor()
    cur.execute("create table if not exists parking(regno INTEGER,username TEXT,block INTEGER)")
    conn.commit()
    conn.close()


def insertparking(regno,username,block): 
    conn=sqlite3.connect("parking.db")
    cur=conn.cursor()
    cur.execute("insert into parking values(?,?,?)",(regno,username,block))
    conn.commit()
    conn.close()
        
def view_park():
    conn=sqlite3.connect("parking.db")
    cur=conn.cursor()
    cur.execute("select * from  parking")
    rows=cur.fetchall()
    return rows
    conn.close()

def delete_park():
    conn=sqlite3.connect("parking.db")
    cur=conn.cursor()
    cur.execute("delete from parking ")
    conn.commit()
    conn.close()


def count_one():
    conn=sqlite3.connect("parking.db")
    cur=conn.cursor()
    cur.execute('select count(regno) from parking where block=1')
    count = cur.fetchone()
    number=count[0]
    return number
def count_49():
    conn=sqlite3.connect("parking.db")
    cur=conn.cursor()
    cur.execute('select count(regno) from parking where block=49')
    count = cur.fetchone()
    number=count[0]
    return number
def count_34():
    conn=sqlite3.connect("parking.db")
    cur=conn.cursor()
    cur.execute('select count(regno) from parking where block=34')
    count = cur.fetchone()
    number=count[0]
    return number
def count_55():
    conn=sqlite3.connect("parking.db")
    cur=conn.cursor()
    cur.execute('select count(regno) from parking where block=55')
    count = cur.fetchone()
    number=count[0]
    return number

def search_park(usr):
    conn=sqlite3.connect("parking.db")
    cur=conn.cursor()
    cur.execute('select regno from parking where username=?',(usr,))
    result=cur.fetchall()
    x=result[0][0]
    return x

def block(regno):
    conn=sqlite3.connect("parking.db")
    cur=conn.cursor()
    cur.execute('select block from parking where regno=?',(regno,))
    result=cur.fetchall()
    x=result[0][0]
    return x    


# print(search('ashish'))
# create_parking()
# insert('ashish',11802002,'BH6',1,88490234230,'ashishboss9977@gmail.com','ashish123')
# insertparking('11802002','Boss','1')
# print(view())
# print(view_park())
# print(count())
# print(search_park('Boss'))
# print(ashish)
# delete()
# delete()
# print(count_one())
# print(count_34())
# print(count_55())
# print(count_49())
# def popup_showinfo():
#     showinfo("Window", "Login Sucessfully")
# img = ImageTk.PhotoImage(Image.open("rose.jpeg"))
# panel = Label(window, image = img)

# panel.grid(row=10,column=6)