#!/usr/local/bin/python3

import sqlite3

# 5 STEPS to ACCESS a db
# 1) Connect to a DB 
# 2) Create a cursor object
# 3) Write an SQL query
# 4) Commit to the DB
# 5) close the connection
def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert_data(item, quantity, price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item, quantity, price))
    conn.commit()
    conn.close()

def view_data():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    # conn.commit() # No need for commit on read operations
    conn.close()
    return(rows)

def rmitem(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update_row(quantity, price, item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?,price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()


#insert_data("Wine Glass", 10, 5)
#insert_data("Coffe Cup", 40, 3.75)

print(view_data())
update_row(30, 4.50, "Wine Glass")
print(view_data())


