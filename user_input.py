#!/usr/local/bin/python3
# The input function inputs values as strings, so we need to convert it to the type we need
A = float(input("A?: "))
B = float(input("B?: "))


def funckytown(a, b):
    c = a**2 + b**2
    return c

print(funckytown(A,B))
