#!/usr/local/bin/python3

import sqlite3
from tkinter import *
from OOPBackend import Database

class frontend:
    
    def __init__(self):
        self.dbfile="book.db"
        self.db = Database(self.dbfile)
        self.window=Tk()
        self.window.wm_title("Bookstore")
        
        # Create the labels
        Label(self.window, text="Title").grid(row=0,column=0, sticky=W) 
        Label(self.window, text="Year").grid(row=1,column=0, sticky=W) 
        Label(self.window, text="Author").grid(row=0,column=2, sticky=W) 
        Label(self.window, text="ISBN").grid(row=1,column=2, sticky=W) 
        
        self.title_text=StringVar()
        self.title_entry=Entry(self.window, width=15, textvariable=self.title_text)
        self.title_entry.config(highlightbackground="grey", highlightthickness=1)
        self.title_entry.grid(row=0, column=1, sticky=W)
        
        self.year_text=StringVar()
        self.year_entry=Entry(self.window, width=15, textvariable=self.year_text)
        self.year_entry.config(highlightbackground="grey", highlightthickness=1)
        self.year_entry.grid(row=1, column=1, sticky=W)
        
        self.author_text=StringVar()
        self.author_entry=Entry(self.window, width=15, textvariable=self.author_text)
        self.author_entry.config(highlightbackground="grey", highlightthickness=1)
        self.author_entry.grid(row=0, column=3, sticky=W)
        
        self.isbn_text=StringVar()
        self.isbn_entry=Entry(self.window, width=15, textvariable=self.isbn_text)
        self.isbn_entry.config(highlightbackground="grey", highlightthickness=1)
        self.isbn_entry.grid(row=1, column=3, sticky=W)
        
        # Create the buttons
        self.viewall=Button(self.window,text="View All", width=12, command=self.view_cmd)
        self.viewall.grid(row=2, column=3, sticky=W)
        
        self.searchentry=Button(self.window,text="Search Entry", width=12, command=self.search_cmd)
        self.searchentry.grid(row=3, column=3, sticky=W)
        
        self.addentry=Button(self.window,text="Add Entry", width=12, command=self.addentry_cmd)
        self.addentry.grid(row=4, column=3, sticky=W)
        
        self.updateentry=Button(self.window,text="Update Entry", width=12, command=self.update_cmd)
        self.updateentry.grid(row=5, column=3, sticky=W)
        
        self.deleteentry=Button(self.window,text="Delete Entry", width=12, command=self.delete_cmd)
        self.deleteentry.grid(row=6, column=3, sticky=W)
        
        #closeapp=Button(window,text="Close", width=12, command=appexit)
        self.closeapp=Button(self.window,text="Close", width=12, command=self.window.destroy)
        self.closeapp.grid(row=7, column=3, sticky=W)
        
        # Create the listbox 
        self.lbox = Listbox(self.window, height=11, width=35)
        self.lbox.grid(row=2, column=0, rowspan=6, columnspan=2, sticky=W)
        
        # Create scrollbar and attach it to the listbox
        self.sb1 = Scrollbar(self.window)
        self.sb1.grid(row=2, column=2, rowspan=6, sticky=W)
        
        self.lbox.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.lbox.yview, highlightbackground="grey", highlightthickness=1)
        
        self.lbox.bind('<<ListboxSelect>>',self.get_selected_row)
        
        self.window.mainloop()
    
    def appexit(self):
        sys.exit()
    
    def view_cmd(self):
        self.lbox.delete(0, END)
        for row in self.db.getall():
            self.lbox.insert(END, row)
            
    def search_cmd(self):
        self.lbox.delete(0, END)
        for row in self.db.search_e(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.lbox.insert(END, row)
    
    def addentry_cmd(self):
        self.db.add_e(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())    
    
    def get_selected_row(self, event):
        global selected_tuple
        index=self.lbox.curselection()[0]
        self.selected_tuple=self.lbox.get(index)
        self.title_entry.delete(0,END)
        self.title_entry.insert(END,self.selected_tuple[1])
        self.author_entry.delete(0,END)
        self.author_entry.insert(END,self.selected_tuple[2])
        self.year_entry.delete(0,END)
        self.year_entry.insert(END, self.selected_tuple[3])
        self.isbn_entry.delete(0,END)
        self.isbn_entry.insert(END, self.selected_tuple[4])
        # No need to return selected_tuple due to global variable
        #return(selected_tuple)
    
    def delete_cmd(self):
        self.db.delete_e(self.selected_tuple[0])
    
    def update_cmd(self):
        self.db.update_e(self.selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        


bookstore = frontend()




