#===WAPS to create a three dictionaries,then create one  dictionary that will contain the other three dictonries:

d1={101:'Akash',102:'Anil',103:'Bhaskar'}
d2={104:'Bhanupriya',105:'Deeksha'}
d3={106:'Sonia',107:'Pushkar',108:'Yogita'}
dict_1={}
for e in (d1,d2,d3):
    for k,v in e.items():
        dict_1[k]=v
print(dict_1)
