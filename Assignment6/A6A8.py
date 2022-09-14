#=== Quadratic equation:
a=int(input("Enter a value of a:"))
b=int(input("Enter a value of b:"))
c=int(input("Enter a value  of c:"))
d=b**2-4*a*b*c
if d==0:
    print("eq has two real and equal roots")
elif d>0:
    print("eq has two real and distinict roots")
else:
    print("eq has imaginary roots")

