""" Author : Neha Jalan
    Date : 24 July 2023
WAP to find the greatest among 3 numbers """

a = 3
b = 5
c = 9

def greatestNum(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

result = greatestNum(a,b,c)
print("greatest among these numbers is", a, b, c, "is", result)
