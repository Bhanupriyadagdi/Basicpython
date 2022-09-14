#===Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.
def str_c(s):
    uc=0
    lc=0
    if type(s) is str:
        for e in s:
            if e.isupper():
                uc+=1
            elif e.islower():
                lc+=1
        print("upper case letter is {}".format(uc))
        print("lower case letter is {}".format(lc))
        




str_c("My Name is BhanuPriya Dagdi")
