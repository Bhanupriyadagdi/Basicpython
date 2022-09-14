#==Write a python program to append elements from another list to the current list:
FL=["Java","Python","SQL"]
SL=["C","CPP","NOSQL"]
N=len(FL)
i=N-1
while i>=0:
    SL.append(FL[i])
    i-=1
    print(SL)
