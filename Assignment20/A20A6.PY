#===WAPP to create a function and print a list where the values are square of numbers between 1 and 30.
def my_fun():
    list_1=[]
    for e in range(1,31):
        list_1.append(e*e)
    print(list_1)

my_fun()