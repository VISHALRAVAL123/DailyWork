'''
Dict Comprehension
Syntax :
 {key:value for (key,value) in iterable if conditional}
Example:
Common Way:
Output:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

'''
d = {}
for i in range(1,10):
    sqr = i*i
    d[i] = i*i
print(d)

#Using Dict Comprehension:
d1={n:n*n for n in range(1,10)}
print (d1)


d1={}
for i in range(1,20):
    sqr=i*i
    d1[i]=i*i
print(d1)
