#====to create a function to check whether a number falls in a given range.


def my_range(a):
   print("{} is in the range".format(a)) if a in range(1,10)  else  print("{} is not in the range".format(a))
      
my_range(8)
my_range(15)
my_range(10)