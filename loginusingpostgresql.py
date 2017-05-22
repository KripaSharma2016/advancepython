'''
Created on 22-May-2017

@author: ks016399
'''
import psycopg2
"""try:
    cur.execute('''CREATE TABLE MYTABLE
      (USERNAME TEXT    NOT NULL,
      PASSWORD TEXT     NOT NULL);''')
except Exception as ex :
    print("error in creatting db"+str(ex))
else:
    con.commit()
    print("Table created.......")
finally:
    con.close()"""

"""username = "rohan"
password = "12345"

try:
    cur.execute('''INSERT INTO MYTABLE (USERNAME,PASSWORD) VALUES (%s,%s)''',(username,password))
except Exception as ex:
    print("not able to insert !"+str(ex))
else:
    con.commit()
    print("got inserted .......")
finally:
    con.close()"""

try:
    con = psycopg2.connect(database='suppliers',  user = "postgres", password = "python123", host = "127.0.0.1", port = "5433")
except Exception as ex:
    print("error in coonecting database!"+str(ex))
else:
    print("connected.............")
cur  = con.cursor()

uname = raw_input("enter your username:")
pwd = raw_input("enter passwaord:")

# get data from db
try:
    cur.execute('''SELECT USERNAME,PASSWORD FROM MYTABLE WHERE USERNAME=%s and PASSWORD=%s''',(uname,pwd))
except Exception as ex:
    print("Error in query"+str(ex))
else:
    rows = cur.fetchall()
    if rows:
        print("Login .......")
    else:
        print("incorrect...")
finally:
    con.close()