#==Create a generator to produce first n odd natural numbers

def odd_generator(n):
    i=1
    while i<=n:
        yield 2*i-1
        i+=1

for e in odd_generator(int(input("enter a number"))):
    print(e)