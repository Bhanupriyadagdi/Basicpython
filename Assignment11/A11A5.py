#=== Calculate sum of first n even natural number using loop:
n=int(input("enter a number"))
i=1
s=0
while i<=n:
    s=s+i*2
    i+=1
print(s)