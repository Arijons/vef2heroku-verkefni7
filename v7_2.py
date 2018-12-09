


import pymysql

def create_connection():
#mysql://b6b4e521ba80a5:faae03d5@eu-cdbr-west-02.cleardb.net/heroku_b22cba0b4af10fe?reconnect=true
    try:
        conn = pymysql.connect(host='eu-cdbr-west-02.cleardb.net',
                                       database='heroku_b22cba0b4af10fe',
                                       user='b6b4e521ba80a5',
                                       password='faae03d5')
        return conn
    except Error as e:
        print(e)
    print ("uuups")
    return None


def er_notandinn_til(u,p):
    notandi_til =False
    conn = create_connection()
    sql="Select * from `user_tafla`;"

    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    for r in rows:
        if r[0]==u or r[1]==p:
            print (r[0], r[1])
            notandi_til = True
    return notandi_til

    def nafn(u,p):
    conn = create_connection()
    sql="Select * from `user_tafla`;"

    c = conn.cursor()
    c.execute(sql)
    rows = c.fetchall()
    for r in rows:
        if r[0]==u or r[1]==p:
            print (r[0], r[1])
    return r[2]
        

def passa_notendaupplysingar(u,p):
    notendaupplysingar =False
    conn = create_connection()
    sql="Select * from `user_tafla`;"
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
        c.execute("insert into user_tafla (user, pass, name) values(%s,%s,%s)" ,(u,p,n))
        conn.commit()
        conn.close()
        
#stofna skrána
def stofna_grunn():
    conn = create_connection()
    c = conn.cursor()

    sql="""CREATE TABLE IF NOT EXISTS `user_tafla` (
      `user` varchar(32) NOT NULL,
      `pass` varchar(32) NOT NULL,
      `name` varchar(32) NOT NULL,
      PRIMARY KEY (`user`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

    c.execute(sql)
    conn.commit()


    sql="""INSERT INTO `user_tafla` (`user`, `pass`,`name`) VALUES
    ('admin', '1234', 'Adel Minsson'),
    ('daniel', '4321', 'Daniel Brodirson');"""

    c.execute(sql)
    conn.commit()

#stofna_grunn()


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

