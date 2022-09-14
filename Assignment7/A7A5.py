#=== Takes a number from user:
x=int(input("enter a  number"))
match x:
    case x if x%2==0:
        print("Saurabh Shukla")
    case  x if x<0 and x%2!=0:
        print("Prateek Jain")
    case x if x>0 and x%2!=0:
        print("Aditya Choudhary")
    


        
    
