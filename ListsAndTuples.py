#!/usr/local/bin/python3 

mylist = ["1","g",5,"#"]
print(mylist)
print(mylist[3])
# print(type(list))
# print(dir(list))
mylist.append(42)
print(mylist)
mylist.reverse()
print(mylist)

# Tuples are not mutable. You can't change them.
mytup = ("hello", 1, 4.5, "42")
print(mytup)
print(mytup[0])
print(dir(mytup))
print(dir(mylist))





