""" Author : Neha Jalan
    Date : 24 July 2023
WAP to print even odd numbers upto 100 with seperate list"""
def EvenOddList():
    Evli = []
    Odli = []
    for i in range(101):
        if i % 2 == 0:
            Evli.append(i)
        else:
            Odli.append(i)
    return (Evli,Odli)

Even_List,Odd_List = EvenOddList()
print("Even numbers upto 100 are ", Even_List)
print("Odd numbers upto 100 are ", Odd_List)