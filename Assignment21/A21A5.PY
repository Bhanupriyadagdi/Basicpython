#==Write a recursive python function to print first N even natural numbers:
def even_n(n):
    if n>0:
        even_n(n-1)
        print(2*n)

even_n(10)