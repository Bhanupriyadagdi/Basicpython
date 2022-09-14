#===WAPP  to create a function which expects an unknown number of arguments:
def fun(*t):
    for e in t:
        print(e)

fun(1,5,8,9,7,2,4)