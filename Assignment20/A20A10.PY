#==Write a python program to create a function to check whether a string is an anagram or not:
def anagram(s1,s2):
    if sorted(s1)== sorted(s2):
        print("both string is anagram")
    else:
        print("both string is not anagram")

anagram('listen','silent')

