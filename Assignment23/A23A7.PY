#===Create an endless iterator using generator method to produce terms of Fibonacci series

def fibo_gen():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

list_fibo=[]
for e in fibo_gen():
    if input("Do you want to generate next element[y/n]")=='y':
        list_fibo.append(e)
    else:
        break
print(list_fibo)
    