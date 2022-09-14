#===Disply only middle digit of given three digit number:
x=int(input("Enter a three digit number:"))
x//=10
x%=10
print("Middle digit of given number:",x)
