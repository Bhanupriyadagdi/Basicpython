#===Write a recursive python function to calculate sum of cubes of first N natural numbers:
def sum_cubes(n):
    if n==1:
        return 1
    return n*n*n + sum_cubes(n-1)
print(sum_cubes(5))