myList = [1, 5, 5, 5, 5,10]
max = myList[0]
indexOfMax = 0
for i in range(1, len(myList)):
    if myList[i] > max:
        max = myList[i]
        indexOfMax = i
print(indexOfMax)


myList = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    myList[i - 1] = myList[i]
 
for i in range(0, 6): 
    print(myList[i], end = " ")

#List Comprehension are a shorthand for creating new lists.
names1 = ['Amir', 'Bala', 'Charlie']
names2 = [name.lower() for name in names1]
 
print(names2[2][0])

#A list is passed in append so the length is 5.
numbers = [1, 2, 3, 4]
 
numbers.append([5,6,7,8])
 
print(len(numbers))

#+ will append the element to the list.
def addItem(listParam):
    listParam += [1]
##########################
mylist = [1, 2, 3, 4]
addItem(mylist)
print(len(mylist))

def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1
 
values = [1, 2, 3]
print(increment_items(values, 2))
print(values)
#######################
def example(L):
    ''' (list) -> list
    '''
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result
##################
m = [[x, y] for x in range(0, 4) for y in range(0, 4)]
print(m)
###################
values = [[3, 4, 5, 1], [33, 6, 1, 2]]
 
v = values[0][0]
for row in range(0, len(values)):
    for column in range(0, len(values[row])):
        if v < values[row][column]:
            v = values[row][column]
 
print(v)
############short values
values = [[3, 4, 5, 1 ], [33, 6, 1, 2]]
 
for row in values:
    row.sort()
    for element in row:
        print(element, end = " ")
    print()
