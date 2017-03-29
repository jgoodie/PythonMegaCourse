#!/usr/local/bin/python3 
# Disctionaries are Key/Value pairs
# You can have lists and Tuples as part of the dictionary
mylist = ["1","g",5,"#"]
mydict = {"FirstName":"John", "LastName":"Goodman", "Age":42, "Gender":"M"}
print(mydict)
print(mydict["FirstName"])
mydict = {"FirstName":"John", "LastName":"Goodman", "Age":42, "Gender":"M", "Cities":["Ruidoso", "Albuquerque", "Santa Clara"]}
print(mydict)
print(mydict["Cities"])
print(mydict["Cities"][0])

money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
print(money["under_bed"][1])


