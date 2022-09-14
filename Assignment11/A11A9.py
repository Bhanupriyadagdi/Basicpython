n=int(input("Enter a decimal number"))
x=""
while n!=0:
  x=x+str(n%2)
  n=n//2
print([int(e)for e in x])

    
  

 
 