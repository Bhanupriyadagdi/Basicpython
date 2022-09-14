#===Write a recursive python function to calculate sum of the digits of a given number:
def digit_sum(n):
    if n==0:
        return 0
    return n%10+digit_sum(n//10)
        

print(digit_sum(87956))