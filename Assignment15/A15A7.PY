#====WAPS to determine whether a string contains a specific substring:
str_1="I like Python Language"
str_2="Python"
s=str_1.split()
if str_2 in s:
    print("yes-str_2 is substring of str_1:-")
else:
    print("no")
print()