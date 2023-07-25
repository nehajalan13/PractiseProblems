""" Author : Neha Jalan
    Date : 24 July 2023
WAP to find the sum of digits of a no using recursion """

num = int(input("Enter a number"))

def SumOfDigits(n):
    if n == 0 :
        return 0
    else:
        return ((n % 10) + SumOfDigits(n//10))

result = SumOfDigits(num)
print(result)