#==Write a recursive python function to print a number in reverse order:
def num(n):
    if n>0:
        print(n%10,end="")
        num(n//10)

num(14522)