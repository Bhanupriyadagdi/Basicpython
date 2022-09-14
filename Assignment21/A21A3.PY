#==Write a recursive python function to print first N odd natural numbers:
def odd_num(n):
    if n>0:
        odd_num(n-1)
        print(n*2-1)
        
        

odd_num(5)

