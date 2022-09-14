#===WAPS to check whether number is positive or negative or zero:
x=int(input("enter a number"))
match x:
    case x if x>0:
        print("Positive")
    case x if x<0:
        print("Negative")
    case x if x==0:
        print("Zero")


