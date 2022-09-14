#==Write a recursive python function to print first N multiples of a given number.
def mul_no(i,n):
    if n>0:
        mul_no(i,n-1)
        print(i*n)


mul_no(7,10)



    




    