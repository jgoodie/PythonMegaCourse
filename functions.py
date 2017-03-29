#!/usr/local/bin/python3 

def euros2dollars(rate, euros):
    print("hello from myfunc")
    dollars=euros*rate
    return dollars

def dollars2euros(rate, dollars):
    euros=dollars*rate
    return euros

dollars = euros2dollars(0.95,42.00)
print(dollars)

euros = dollars2euros(1.06, 42.00)
print(euros)

