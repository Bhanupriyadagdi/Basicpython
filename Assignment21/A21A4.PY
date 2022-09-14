#==Write a recursive python function to print first N odd natural numbers in reverse order:
def odd_rev(n):
    if n>0:
        print(2*n-1)
        odd_rev(n-1)

odd_rev(10)