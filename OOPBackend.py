#!/usr/local/bin/python3

import sqlite3, sys

class Database:
    
    def __init__(self, dbconnection):
        self.conn = sqlite3.connect(dbconnection)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bookstore (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()
        #conn.close()
        # print("hello from table create")
  
    def __del__(self):
        self.conn.close()
        #print("bye")
      
    def getall(self):
        self.cur.execute("SELECT * FROM bookstore")
        rows = self.cur.fetchall()
        return(rows)
        
    def search_e(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM bookstore WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return(rows)
        
    def add_e(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO bookstore VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()
        
    def update_e(self, id, title, author, year, isbn):
        # print(id, title, author, year, isbn)
        self.cur.execute("UPDATE bookstore SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit()
        
    def delete_e(self, id):
        self.cur.execute("DELETE FROM bookstore WHERE id=?", (id,))
        self.conn.commit()

# Create the DB table if it doesn't already exist
# Get's called when imported
# OOP: don't need this because of __init__
# create_table()

#### TESTING ######
# add_e("Fartacular", "Wiener Butt", 2018, 945623456)
# print(getall())
# delete_e(5)
# print(getall())
# update_e(4, "Gas Man", "Captain Butts", 2016, 123456789 )
# print(getall())
# print(search_e(title="", author="John Smith", year="", isbn=""))
# print(search_e(title="", author="", year="2016", isbn=""))

