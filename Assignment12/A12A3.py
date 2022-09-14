#==WAPS to print all prime number under100
i=1
while i<100:
    x=2
    while x<=i//2:
        if i%x==0:
            break
        x+=1
    else:
        print(i)
    i+=1

    
            

