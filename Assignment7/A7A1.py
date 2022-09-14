#====Display the no of days ina given month number:
x=int(input("enter a number"))
match x:
    case x if x in(1,3,5,7,8,10,12):
        print("31 days")
    case x if x in(4,6,9,11):
        print("30 days")
    case 2:
        year=int(input("enter a year"))
        print("29 days") if year%4==0 and year%100!=0 or year%400==0 else print("28 days")
    case _:
     print("exit")
     
     
