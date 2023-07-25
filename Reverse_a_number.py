""" Author : Neha Jalan
    Date : 24 July 2023
WAP to reverse a given number"""

n = int(input("enter a number to reverse"))

def rev(n):
    temp = 0
    while (n != 0):
        d = n % 10
        temp = (temp * 10) + d
        n = n//10
    return temp

num = rev(n)
print(num)


