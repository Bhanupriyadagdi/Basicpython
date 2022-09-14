#==Create a generator to produce first n even natural numbers
def even_gen(n):
    i=1
    while i<=n:
        yield 2*i
        i+=1

for e in even_gen(10):
    print(e)
