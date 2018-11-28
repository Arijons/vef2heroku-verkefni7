


import mysql.connector
from mysql.connector import Error

def create_connection():

    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='lykill',
                                       user='root',
                                       password='D1fferential')
        return conn
    except Error as e:
        print(e)
    print ("uuups")
    return None


def er_notandinn_til(u,p):
    notandi_til =False
    conn = create_connection()
    sql="Select * from `user`;"

    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    for r in rows:
        if r[0]==u or r[1]==p:
            print (r[0], r[1])
            notandi_til = True
    return notandi_til

def passa_notendaupplysingar(u,p):
    notendaupplysingar =False
    conn = create_connection()
    sql="Select * from `user`;"
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    for r in rows:
        if r[0]==u and r[1]==p:
            notendaupplysingar = True
    return notendaupplysingar

def nyr_notandi(u,p,n):
    conn = create_connection()
    if er_notandinn_til(u,p):
        print("notandi til")
    else:
        c = conn.cursor()
        c.execute("insert into user (user, pass, name) values(%s,%s,%s)" ,(u,p,n))
        conn.commit()
        conn.close()
        



"""def main():
    database = 'kt_verkqlite.db'
    conn = create_connection()
    
    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    for row in rows:
        print(row)
     #bæta við notanda
    u=str(input("sláðu inn username"))
    p=str(input("sláðu inn password"))
    n=str(input("sláðu inn name"))
    nyr_notandi(u,p,n)
    c = conn.cursor()
    rows = c.fetchall()
    for row in rows:
        print(row)
main()"""
