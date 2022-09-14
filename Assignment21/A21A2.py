#==Write a recursive python function to print first N natural numbers in reverse order:
def f1(n):
    if n>0:
        print(n)
        f1(n-1)

f1(10)