print("enter three numbers:")
x,y,z=int(input("x:")),int(input("y:")),int(input("z:"))
if x>=y and x>=z:
    print("greatest num:",x)
elif y>=x and y>=z:
    print("greatest num:",y)
else:
    print("greatest num:",z)
                                            
