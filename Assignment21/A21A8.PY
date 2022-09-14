#==Write a recursive python function to print cubes of first N natural numbers:
def cube_N(n):
    if n>0:
        cube_N(n-1)
        print(n**3)


cube_N(5)