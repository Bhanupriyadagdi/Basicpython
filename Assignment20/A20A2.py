#==Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.
def isprime_num():
    n=int(input("Enter a number"))
    for e in range(2,n):
        if n%e==0:
            return "Given number is not prime number"
    return "Given number is prime number"
    
   

print(isprime_num())
            
