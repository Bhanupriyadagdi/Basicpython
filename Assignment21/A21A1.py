#==Write a recursive python function to print first N natural numbers.
def natural_num(N):
    if N>0:
        natural_num(N-1)
        print(N)
        


natural_num(10)