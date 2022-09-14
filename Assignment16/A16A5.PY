#===Write a python program to check if all items in the tuple are the same.
T1=(10,15,14,16,20)
for e in T1:
    if type(T1[0])!=type(e):
        print("not same")
        break
else:
    print("ALL item are same")