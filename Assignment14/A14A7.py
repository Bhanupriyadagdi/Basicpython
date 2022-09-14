#==Write a Python script to remove all non int values from a list:
list=[45,12.3,"hello",453,4.9,5]
list_1=[]
i=0
while i<len(list):
    if type(list[i]) is int:
        list_1.append(list[i])
    i+=1   
list=list_1
print(list)

        
