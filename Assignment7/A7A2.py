#=== Write a menu driven program to perform following operation Addition Subtraction Multiplication division:
print("Enter a choice :")
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.division")
choice=int(input())
x,y=int(input("enter first number")),int(input("enter second number"))
match choice:
    case 1:
        print(x+y)
    case 2:
        print(x-y)
    case 3:
        print(x*y)
    case 4:
        print(x/y)
    case _:
        print("Exit")
