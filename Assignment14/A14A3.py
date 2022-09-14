#===Write a Python script to create a list of first N even natural numbers:
n=int(input("enter a number"))
print([int(e)for e in range(2,n*2+1,2)])