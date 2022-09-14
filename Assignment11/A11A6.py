#===calculate factorial of a given number :
n=int(input("enter a number"))
i=1
fctn=1
while i<=n:
    fctn=fctn*(n+1-i)
    i+=1
print(fctn)