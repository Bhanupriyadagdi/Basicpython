#===Write a python script to print first N prime numbers:

n=int(input("enter a number"))
i=1
while i<=n:
    e=2
    for e in range(e,i+1//2,1):
        if i%e==0:
            break
    else:
        print(i)
    i=i+1
