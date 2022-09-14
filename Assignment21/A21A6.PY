#==Write a recursive python function to print first N even natural numbers in reverse order.
def even_rev(n):
    if n>0:
        print(n*2)
        even_rev(n-1)


even_rev(5)