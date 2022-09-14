#===Write a python script to find next prime number of a given number

n=int(input("enter a numbetr"))
a=n+1
for x in range(2,n//2,1):
    if a%x==0:
        a=a+1
else:
    print(a)


   

