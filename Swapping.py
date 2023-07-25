""" Author : Neha Jalan
    Date : 24 July 2023
WAP to Swap 2 numbers """
a = 2
b = 3

def Swap(a,b):
    a = a + b
    b = a - b
    a = a - b
    return (a,b)

print("Before Swaping")

print("a =", a)
print("b =", b)

a,b = Swap(a,b)

print("After Swaping")

print("a =", a)
print("b =", b)

