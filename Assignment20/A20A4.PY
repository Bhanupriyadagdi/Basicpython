#===WAPP to create a function that checks whether a passed string is palindrome or not:

def my_fun(s):
    print("{} is palindrome".format(s)) if s==s[::-1] else print("{} is not palindrome".format(s))
       
       
my_fun("radar")
my_fun("level")
my_fun("abcab")