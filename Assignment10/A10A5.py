# print first n odd natural num in reverse order:
n=int(input("enter a number"))
r=range(1,n+1,1)
for x in r:
    print(2*n+1-2*x)