dict={'a':1,'b':2,'c':3,'d':4}
key=list(dict)
print(key)

d2={'a':1,'b':2,'c':3,'d':4}
key=list(d2.keys())
print(key)

d3={'a':1,'b':2,'c':3,'d':4}
x=d3.keys()
print(x)

###############################

#Delete By Using clear():
d1 = {'A':1,'B':2,'C':3}
d1.clear()
print(d1) #{}

#Delete By Using pop():
d1 = {'A':1,'B':2,'C':3}
print(d1) #{'A': 1, 'B': 2, 'C': 3}
d1.pop('A')
print(d1)# {'B': 2, 'C': 3}

#Delete By Using del():
del d1['B']
print(d1) # {'C': 3}

#Copy A Dictionary Using copy():
d2 = {'A':1,'B':2,'C':3}
print(d2) # {'A': 1, 'B': 2, 'C': 3}
d3 = d2.copy()
print(d3) # {'A': 1, 'B': 2, 'C': 3}

#Copy A Dictionary Using ‘=’:
d2 = {'A':1,'B':2,'C':3}
print(d2) # {'A': 1, 'B': 2, 'C': 3}
d3 = d2
print(d3) # {'A': 1, 'B': 2, 'C': 3}


#Benefit Of Using Copy():
d2 = {'A':1,'B':2,'C':3}
print(d2) # {'A': 1, 'B': 2, 'C': 3}
d3 = d2.copy()
print(d3) # {'A': 1, 'B': 2, 'C': 3}
del d2['B']
print(d2) # {'A': 1, 'C': 3}
print(d3) # {'A': 1, 'B':2, 'C': 3}

#DrawBack Of Using ‘=’
d2 = {'A':1,'B':2,'C':3}
print(d2) # {'A': 1, 'B': 2, 'C': 3}
d3 = d2
print(d3) # {'A': 1, 'B': 2, 'C': 3}
del d2['B']
print(d2) # {'A': 1, 'C': 3}
print(d3) # {'A': 1, 'C': 3}
