#Create a generator to produce first n terms of Fibonacci series
def fibo_gen(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1

for e in fibo_gen(10):
    print(e)