#==Write a python program to access a function inside a function.
def start():
    print("WELCOME!")



def check_num():
    a=int(input("enter a even number"))
    start() if a%2==0 else check_num()
        

    
            
check_num()