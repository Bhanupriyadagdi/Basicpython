#===Write a python script to print all Prime numbers between two given numbers:

num_1,num_2=int(input("enter a number")),int(input("enter a number"))
for n in range(num_1,num_2+1,1):
    for e in range(2,n+1//2,1):
        if n%e==0:
            break
    else:
        print(n)