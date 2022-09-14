#== calculate sum of first n odd natural numeber:
n= int(input("Enter a number"))
i=1
sum=0
while i<=n:
    sum=sum+2*i-1
    i+=1
print(sum)