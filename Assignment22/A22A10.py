#===Write a recursive python function to find the Nth term of the Fibonacci series:
def fibo_series(n):
    if n==1 or n==2:
        return 1
    elif n>2:
        return fibo_series(n-1)+fibo_series(n-2)


print(fibo_series(10))