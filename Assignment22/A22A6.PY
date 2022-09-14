#===Write a recursive python function to calculate the factorial of a number:
def factorial_rec(n):
    if n==1:
        return 1
    return n* factorial_rec(n-1)

print(factorial_rec(3))