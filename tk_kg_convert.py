#!/usr/local/bin/python3

#import tkinter
from tkinter import *

window=Tk()
window.wm_title("kg converter")
def converter():
    grams = float(kgs.get())*1000
    t1grams.delete(0.0,END)
    t1grams.insert(END, grams)
    lbs = float(kgs.get())*2.20462
    t2lbs.delete(0.0,END)
    t2lbs.insert(END, lbs)
    oz = float(kgs.get())*35.274
    t3oz.delete(0.0,END)
    t3oz.insert(END, oz)

# l1 = Label(window, text="Kilograms")
# l1.grid(row=0,column=0, sticky=W)
Label(window, text="Kilograms").grid(row=0,column=0, sticky=W)   
kgs=StringVar()
kgs.set(1)
kge1=Entry(window, width=15, textvariable=kgs)
kge1.grid(row=0,column=1, sticky=W)

convertb1=Button(window,text="Convert", command=converter)
convertb1.grid(row=0, column=2)

Label(window, text="Grams").grid(row=1,column=0, sticky=W) 
t1grams=Text(window, height=1, width=20)
t1grams.config(highlightbackground="grey", highlightthickness=1)
t1grams.grid(row=1,column=1, sticky=W)

Label(window, text="Pounds").grid(row=2,column=0, sticky=W) 
t2lbs=Text(window, height=1, width=20)
t2lbs.config(highlightbackground="grey", highlightthickness=1)
t2lbs.grid(row=2,column=1, sticky=W)

Label(window, text="Ounces").grid(row=3,column=0, sticky=W)
t3oz=Text(window, height=1, width=20)
t3oz.config(highlightbackground="grey", highlightthickness=1)
t3oz.grid(row=3,column=1, sticky=W)

window.mainloop()