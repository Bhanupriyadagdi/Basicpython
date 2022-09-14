#===WAPP Write a python program to create a function to check whether a given number is even or odd.

def check_num(a):
    print("{} is even number".format(a)) if a%2==0 else print("{} is odd number".format(a))
        

check_num(2)
check_num(3)
check_num(15)
check_num(24)