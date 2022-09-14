#Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.
def my_fun(list_1):
    n_list=[]                   # create a new list for unique number..
    for e in list_1:
        if list_1.count(e)==1:
            n_list.append(e)
    return n_list


            


list_1=[1,2,3,1,2,4,6,8,1,7,9,4,2]
print(my_fun(list_1))
