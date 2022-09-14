#==Create an endless iterator using generator method to produce Prime numbers
def prime_check(n):
    for e in range(2,n):
        if n%e==0:
            return False
    return True
def prime_gen():
    n=2
    while True:
        if prime_check(n):
            yield n
        n+=1

list_prime=[]
for e in prime_gen():
    if input("do you want to generate next prime number: [y/n]")=='y':
        list_prime.append(e)
    else:
        break
print(list_prime)