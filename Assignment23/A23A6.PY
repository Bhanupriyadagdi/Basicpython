#==Create a generator to produce first n prime numbers
def isprime(n):
    for e in range(2,n):
        if n%e==0:
            return False
    return True

def prime_gen(k):
    n=2
    while k:
        if isprime(n):
            yield n
            k-=1
        n+=1

for a in prime_gen(5):
    print(a)