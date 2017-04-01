#!/usr/local/bin/python3

import sqlite3, bookstore_backend
from tkinter import *
# from bookstore_backend import *

def appexit():
    sys.exit()

def view_cmd():
    lbox.delete(0, END)
    for row in bookstore_backend.getall():
        lbox.insert(END, row)
        
def search_cmd():
    lbox.delete(0, END)
    for row in bookstore_backend.search_e(title_text.get(), year_text.get(), author_text.get(), isbn_text.get()):
        lbox.insert(END, row)

def addentry_cmd():
    bookstore_backend.add_e(title_text.get(), year_text.get(), author_text.get(), isbn_text.get())    

# Create the DB table if it doesn't already exist. 
# No need to call this since when bookstore_backend is imported it's automatically called.
# bookstore_backend.create_table()

dbconnection = "book.db"
window=Tk()
window.wm_title("Bookstore")

# Create the labels
Label(window, text="Title").grid(row=0,column=0, sticky=W) 
Label(window, text="Year").grid(row=1,column=0, sticky=W) 
Label(window, text="Author").grid(row=0,column=2, sticky=W) 
Label(window, text="ISBN").grid(row=1,column=2, sticky=W) 

title_text=StringVar()
title_entry=Entry(window, width=15, textvariable=title_text)
title_entry.config(highlightbackground="grey", highlightthickness=1)
title_entry.grid(row=0, column=1, sticky=W)

year_text=StringVar()
year_entry=Entry(window, width=15, textvariable=year_text)
year_entry.config(highlightbackground="grey", highlightthickness=1)
year_entry.grid(row=1, column=1, sticky=W)

author_text=StringVar()
author_entry=Entry(window, width=15, textvariable=author_text)
author_entry.config(highlightbackground="grey", highlightthickness=1)
author_entry.grid(row=0, column=3, sticky=W)

isbn_text=StringVar()
isbn_entry=Entry(window, width=15, textvariable=isbn_text)
isbn_entry.config(highlightbackground="grey", highlightthickness=1)
isbn_entry.grid(row=1, column=3, sticky=W)

# Create the buttons
viewall=Button(window,text="View All", width=12, command=view_cmd)
viewall.grid(row=2, column=3, sticky=W)

searchentry=Button(window,text="Search Entry", width=12, command=search_cmd)
searchentry.grid(row=3, column=3, sticky=W)

addentry=Button(window,text="Add Entry", width=12, command=addentry_cmd)
addentry.grid(row=4, column=3, sticky=W)

updateentry=Button(window,text="Update Entry", width=12, command=view_cmd)
updateentry.grid(row=5, column=3, sticky=W)

deleteentry=Button(window,text="Delete Entry", width=12, command=view_cmd)
deleteentry.grid(row=6, column=3, sticky=W)

closeapp=Button(window,text="Close", width=12, command=appexit)
closeapp.grid(row=7, column=3, sticky=W)

# Create the listbox 
lbox = Listbox(window, height=11, width=35)
lbox.grid(row=2, column=0, rowspan=6, columnspan=2, sticky=W)

# Create scrollbar and attach it to the listbox
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6, sticky=W)

lbox.configure(yscrollcommand=sb1.set)
sb1.configure(command=lbox.yview, highlightbackground="grey", highlightthickness=1)


window.mainloop()

