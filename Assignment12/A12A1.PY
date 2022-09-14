#===WAPS to reverse a number:
x =input("enter a number")
n=len(x)
rev=""
while n>0:
    rev=rev+x[n-1]
    n-=1
print(rev)