""" Author : Neha Jalan
    Date : 24 July 2023
WAP to check a number is binary or not"""

n = int(input("enter a binary number"))
def checkBinary(m):
    li = []
    s = {1,0}
    while m > 0:
        li.append(m % 10)
        m = m//10

    temp = set(li)
    if temp == s:
        return "binary number"
    else:
        return "not a binary number"

result = checkBinary(n)
print(result)

