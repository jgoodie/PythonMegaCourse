#!/usr/local/bin/python3 

### C to F
### F = C * (9/5) + 32
def ctof(c):
    if c < -273.15:
        raise ValueError("That temperature doesn't make sense!")
    else:
        f = c * (9/5) +32
        return f

### F to C
### C = (F - 32) * (5/9)
def ftoc(f):
    c = (f - 32) * (5/9)
    if c < -273.15:
        raise ValueError("That temperature doesn't make sense!")
    else:
        return c

### F to K
### K = (F + 459.67) * (5/9)
def ftok(f):
    k = (f + 459.67) * (5/9)
    if k < 0:
        raise ValueError("That temperature doesn't make sense!")
    else:
        return k

### K to F
### F = K * (9/5) - 459.67
def ktof(k):
    if k < 0:
        raise ValueError("That temperature doesn't make sense!")
    else:
        f = k * (9/5) - 459.67
        return f

### C to K
### K = C + 273.15
def ctok(c):
    if c < -273.15:
        raise ValueError("That temperature doesn't make sense!")
    else:
        k = c + 273.15
        return k

### K to C
### C = K - 273.15
def ktoc(k):
    c = k - 273.15
    if c < -273.15:
        raise ValueError("That temperature doesn't make sense!")
    else:
        return c

temps = [10, -20, -273, 100]
for x in temps:
    print(ctof(x))
    
    



#temp = float(input("Enter a temp in Fahrenheit: "))
# tempC = ftoc(temp)
# tempK = ftok(temp)
# tempF = ctof(tempC)
# tempF2 = ktof(tempK)
# tempCtoK = ctok(tempC)
# tempKtoC = ktoc(tempCtoK)
# 
# print(tempC)
# print(tempK)
# print(tempF)
# print(tempF2)
# print(tempCtoK)
# print(tempKtoC)






