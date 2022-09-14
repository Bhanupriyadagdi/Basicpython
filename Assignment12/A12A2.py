#===WAPS to check whether a given number is prime or not:
n=int(input("Enter a number"))
i=2
while i<n-1:
    if n%i==0:
        print("not prime")
        break
    i+=1
else:
    print("prime num")


    