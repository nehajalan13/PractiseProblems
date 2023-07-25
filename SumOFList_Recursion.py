""" Author : Neha Jalan
    Date : 24 July 2023
WAP find the sum of given list using recursion"""

lst = [1,2,3,4,5,6,7,8]
def SumOfList(li):
    if len(li) == 0:
        return 0
    else:
        return (li[0] + SumOfList(li[1:]))

result = SumOfList(lst)
print(result)