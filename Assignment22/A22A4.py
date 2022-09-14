#==Write a recursive python function to calculate sum of squares of first N natural numbers
def sqr_sum(n):
    if n==1:
        return 1
    return n*n+sqr_sum(n-1)



print(sqr_sum(5))