#!/usr/local/bin/python3

import sqlite3, sys

dbconnection = "book.db"

def create_table():
    conn=sqlite3.connect(dbconnection)
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()
    #print("hello from table create")

def getall():
    conn=sqlite3.connect(dbconnection)
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookstore")
    rows=cur.fetchall()
    conn.close()
    return(rows)
    
def search_e(title="", author="", year="", isbn=""):
    conn=sqlite3.connect(dbconnection)
    cur=conn.cursor()
    cur.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows=cur.fetchall()
    conn.close()
    return(rows)
    
def add_e(title, author, year, isbn):
    conn=sqlite3.connect(dbconnection)
    cur=conn.cursor()
    cur.execute("INSERT INTO bookstore VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()
    
def update_e(id, title, author, year, isbn):
    conn=sqlite3.connect(dbconnection)
    cur=conn.cursor()
    cur.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()
    
def delete_e(id):
    conn=sqlite3.connect(dbconnection)
    cur=conn.cursor()
    cur.execute("DELETE FROM bookstore WHERE id=?", (id,))
    conn.commit()
    conn.close()

# Create the DB table if it doesn't already exist
# Get's called when imported
create_table()

#### TESTING ######
# add_e("Fartacular", "Wiener Butt", 2018, 945623456)
# print(getall())
# delete_e(5)
# print(getall())
# update_e(4, "Gas Man", "Captain Butts", 2016, 123456789 )
# print(getall())
# print(search_e(title="", author="John Smith", year="", isbn=""))
# print(search_e(title="", author="", year="2016", isbn=""))

