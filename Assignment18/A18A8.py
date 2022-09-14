#====WAPP to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value
l1=[101,102,103,104,105]
l2=['anil','ajay','akash','anuj','aman']
dict_1={l1[e]:l2[e] for e in range(len(l1))}
print(dict_1)