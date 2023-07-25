""" Author : Neha Jalan
    Date : 24 July 2023
WAP to check a number is prime or not"""

n = int(input("enter a number:"))

def PrimeOrNot(n):
    flag = 0
    if n > 1:
        for i in range(2,(n//2)+1):
            if n % i == 0:
                flag = 1
                break
    elif n == 2:
        flag = 0
    else:
        flag = 1

    if flag == 0:
        return "prime number"
    else:
        return "not a prime number"

def PrimeFactors(n):
    li = []
    for i in range(2,(n//2)+1):
        if n % i == 0:
            if PrimeOrNot(i) == "prime number":
                li.append(i)
    return li


result = PrimeFactors(n)
print(result)