#===WAPP to create a function that finds a maximum of four numbers:


def max_fun(a,b,c,d):
    if a>b and a>c and a>d:
        print("maximum number is {}".format(a))
    elif b>a and b>c and b>d:
        print("maximum number is {}".format(b))
    elif c>a and c>b and c>d:
        print("maximum number is {}".format(c))
    else:
        print("maximum number is {}".format(d))



max_fun(92,45,65,78)
max_fun(92,405,65,78)
max_fun(92,405,625,78)
max_fun(92,405,65,708)

    
    
    
    