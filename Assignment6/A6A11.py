x=int(input("Enter a month value"))
y=[1,3,5,7,8,10,12]
z=[4,6,9,11]
if 1<=x<=12:
    if x in y:
        print("31 Days")
    elif x in z:
        print("30 days")
    elif x==2:
        print("28 days")
