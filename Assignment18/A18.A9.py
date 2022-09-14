#===WAPP to merge two python dictionaries into one dictionary:
dict_1={101:"Chetan",102:'manoj'}
dict_2={103:'vishnu'}
for k,v in dict_2.items():
    dict_1[k]=v
print(dict_1)