#==Write a python program to create a function that prints the even numbers from a given list.

def even_num(list_1):
    for e in list_1:
        if e%2==0:
            print(e,end=' ')

list_3=[1,2,3,4,5,6,7,8,9]
even_num(list_3)