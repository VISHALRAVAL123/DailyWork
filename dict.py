dict={1:"vishal",2:"manav",3:"kishan"}
print(dict)
for x in dict.keys():
    print(x)

dict[4]="karan"
print(dict)
dict.pop(4)
print(dict)
dict.update({5:"dharti"})
print(dict)
for x,y in dict.items():
    print(x,y)
