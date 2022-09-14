#==Write a recursive python function to print squares of first N natural numbers:
def sqr_N(n):
    if n>0:
        sqr_N(n-1)
        print(n*n)

sqr_N(5)