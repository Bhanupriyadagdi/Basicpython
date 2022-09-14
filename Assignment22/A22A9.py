#==Write a recursive python function to print octal of a given decimal number:
def octal(n):
    if n>1:
        octal(n//8)
    print(n%8,end='')

octal(20)