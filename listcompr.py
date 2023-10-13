'''
List Comprehension
Syntax:
 [expression for item in iterable if conditional]
Example:
Common Way:
'''
l = []
for i in range(10):
 if i%2:
     l.append(i)
print(l)

#Using List Comprehension:
ls = [i for i in range(10) if i%2]
print(ls)

list=[]
for i in range(10):
    if i%2==0:
        list.append(i)
print(list)
