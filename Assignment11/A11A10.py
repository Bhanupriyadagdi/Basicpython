from re import X


n=int(input("enter a decimal number"))
x=''
while n!=0:
    x=x+str(n%8)
    n=n//8
    oct=""
    for i in range(len(x)-1,-1,-1):
        oct=oct+x[i]
print(oct)