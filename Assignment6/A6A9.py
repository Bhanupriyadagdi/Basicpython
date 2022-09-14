year=int(input("ennter a year"))
if year%400==0 and year%100==0 or year%4==0 and year%100!=0:
    print("leap year")
else:
    print("not leap year")
