#!/usr/local/bin/python3

import sqlite3
from tkinter import *
from OOPBackend import Database

dbfile="book.db"
db = Database(dbfile)

def appexit():
    sys.exit()

def view_cmd():
    lbox.delete(0, END)
    for row in db.getall():
        lbox.insert(END, row)
        
def search_cmd():
    lbox.delete(0, END)
    for row in db.search_e(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        lbox.insert(END, row)

def addentry_cmd():
    db.add_e(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())    

def get_selected_row(event):
    global selected_tuple
    index=lbox.curselection()[0]
    selected_tuple=lbox.get(index)
    title_entry.delete(0,END)
    title_entry.insert(END,selected_tuple[1])
    author_entry.delete(0,END)
    author_entry.insert(END, selected_tuple[2])
    year_entry.delete(0,END)
    year_entry.insert(END, selected_tuple[3])
    isbn_entry.delete(0,END)
    isbn_entry.insert(END, selected_tuple[4])
    # No need to return selected_tuple due to global variable
    #return(selected_tuple)

def delete_cmd():
    db.delete_e(selected_tuple[0])

def update_cmd():
    db.update_e(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    
    
# Create the DB table if it doesn't already exist. 
# No need to call this since when db is imported it's automatically called.
# db.create_table()

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

updateentry=Button(window,text="Update Entry", width=12, command=update_cmd)
updateentry.grid(row=5, column=3, sticky=W)

deleteentry=Button(window,text="Delete Entry", width=12, command=delete_cmd)
deleteentry.grid(row=6, column=3, sticky=W)

#closeapp=Button(window,text="Close", width=12, command=appexit)
closeapp=Button(window,text="Close", width=12, command=window.destroy)
closeapp.grid(row=7, column=3, sticky=W)

# Create the listbox 
lbox = Listbox(window, height=11, width=35)
lbox.grid(row=2, column=0, rowspan=6, columnspan=2, sticky=W)

# Create scrollbar and attach it to the listbox
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6, sticky=W)

lbox.configure(yscrollcommand=sb1.set)
sb1.configure(command=lbox.yview, highlightbackground="grey", highlightthickness=1)

lbox.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()

