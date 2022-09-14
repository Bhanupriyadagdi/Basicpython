#==Write a Python script to calculate the sum of elements in a given list of numbers:
list=[int(e) for e in input("enter a list of numbers").split(' ')]
s=0
for x in list:
    s=s+x
print(s)