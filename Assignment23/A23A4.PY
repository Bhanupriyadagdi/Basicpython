#==Create a generator to produce squares of first N natural numbers
def sqr_gen(n):
    i=1
    while n:
        yield i*i
        i+=1
        n-=1


for e in sqr_gen(10):
    print(e)