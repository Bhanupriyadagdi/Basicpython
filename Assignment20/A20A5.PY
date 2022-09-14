#== Write a python program to create a function to find the Min of three numbers
def min(a,b,c):
    if a<b and a<c or a==b or a==c:
        print("minimum number is {}".format(a))
    elif b<a and b<c or b==c:
        print("minimun number is {}".format(b))
    else:
        print("minimum number is {}".format(c))

min(4,6,2)
min(7,3,9)
min(9,15,19)
min(4,4,9)
min(3,8,3)
min(8,2,2)

