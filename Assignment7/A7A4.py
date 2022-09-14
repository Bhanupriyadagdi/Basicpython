#==Taken user's AGE and display the category of person:
x=int(input("Enter a age:"))
match x:
    case x  if x<10:
        print("kid")
    case x if x<20:
        print("Teen")
    case x if x<40:
        print("Young")
    case x if x<60:
        print("Experienced")
    case x if x>=60:
        print("senior citizen")
    
