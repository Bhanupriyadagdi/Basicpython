#===given length of triangle
x=int(input("Enter a choice:\n1.Isosceles triangle\n2.Equilateral triangle\n3.Right angled triangle\n4.Exit\n"))
print("entre three sides of triangle:")
a,b,c= int(input("enter one side")),int(input("enter second side")),int(input("enter third side"))
match x:
    case 1:
        print("Isosceles triangle")if a==b or b==c or c==a else print("not")
            
    case 2:
        print("Equilateral triangle")if a==b==c else print("not")
        
    case 3:
        print("Right angled triangle") if a**2+b**2==c**2 else print("not")
            
    case 4:
        exit()
            
