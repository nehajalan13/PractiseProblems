""" Author : Neha Jalan
    Date : 24 July 2023
WAP to check a given number is even or odd"""

num = int(input("Enter a number"))
def EvenOdd(n):
    if n%2 == 0:
        return ("Even")
    else:
        return ("odd")

result = EvenOdd(num)
print(result)