'''
Map() Function:The map() function iterates through all items in the given iterable and
executes the function we passed as an argument on each of them.
The syntax is:
    '''
map(function, iterable(s))
fruit = ["Apple", "Banana", "Pear"]
map_object = map(lambda s: s[0]
== "A", fruit)
print(list(map_object))

'''Filter() Function:The filter() function takes a function object and an iterable and creates a new ist.
As the name suggests, filter() forms a new list that contains only elements
that satisfy a certain condition, i.e. the function we passed returns True.'''

#The syntax is:
filter(function, iterable(s))
fruit = ["Apple", "Banana", "Pear"]
filter_object = filter(lambda s: s[0] ==
"A", fruit)
print(list(filter_object))

'''
Reduce() Function:The reduce() Function works differently than map() and filter(). It does not return a new
list based on the function and iterable we've passed. Instead, it returns a single value.
Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in thefunctools module.'''
#The syntax is:
reduce(function, sequence[initial])
from functools import reduce
list = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, list))
print("With an initial value: " + str(reduce(lambda x, y: x + y, list, 10)))
