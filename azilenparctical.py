print('Task-1')
input_str ="aaabbaacccaab"
#(1.a) Count letters in whole string,
def count_let(input_str):
    return len(input_str)
# (1.b) Count consecutive letters in the whole string
from itertools import groupby
def count_consecutive(input_str):
    from itertools import groupby

def count_consecutive(input_str):
    consecutive_counts = [sum(1 for _ in group)for _,group in groupby(input_str)]
    return consecutive_counts

letter_count=count_let(input_str)
consecutive_counts=count_consecutive(input_str)
print("Count letters in whole string:",letter_count)
print("Count consecutive letters in the whole string :",consecutive_counts)
print("*"*50)
print('TASK-2')
input_list = [1, 2, 3, 4, 5]
# (2.a) Find the square of each element and create a new list.
squares_list = [x**2 for x in input_list]
print("square of list:",squares_list)
# (2.b) Find the sum of squares for the given input list.
squares_sum= sum(x**2 for x in input_list)
print("sum of squares:",squares_sum)
print("*"*50)
print('TASK-3')
#Write a custom logic to check whether a string is palindrome or not.\n",
#Note: Do not use list comprehension or string reverse logic",
def palindrome(s):
    start, end = 0, len(s) - 1
    while start < end:
        while start < end and not s[start].isalnum():
            start += 1
        while start < end and not s[end].isalnum():
            end -= 1
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True
string1 = "level"
string2="demo"
print(f"Is '{string1}' a palindrome? {palindrome(string1)}")
print(f"Is '{string2}' a palindrome? {palindrome(string2)}")
print("*"*50)
myStr = input("Enter Any String: ")
j = myStr
rev=""
while len (j) > 0:
    if len(j) > 0:
        a = j[-1]
    j = j [:-1]
    rev = rev + a
if rev == myStr:
    print("The given string is Palindrome.")
else:
    print("The given string is not Palindrome.")
print("*"*50)
print('TASK-4')
#Sort the below input list using the last element of each tuple.
input_tuple_list = [(4,2,7),(3,4,8),(1,2,4),(7,6,1),(9,3,1),(2,4,2)]
sorted_list = sorted(input_tuple_list, key=lambda x: x[-1])
print(f"Sorted list based on the last element: {sorted_list}")
print("*"*50)
print('TASK-5 :Find the list of students who have the second highest marks.')
#Use this input dictionary\n",
student_marks = {'Physics': 82,'Math': 65,'history': 75,'Ashok':60,'Reddy': 60,'RRR': 50,'aaa':50}
sorted_students = sorted(student_marks.items(), key=lambda x: x[1], reverse=True)
second_highest = sorted(set(mark for _, mark in sorted_students), reverse=True)[1]
result = [student for student, mark in sorted_students if mark == second_highest]
print(f"Students with the second-highest marks: {result}")
print("*"*50)
print('TASK-6:')
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compare(self, other):
        return self.a == other.a and self.b == other.b
c1 = Vector(10, 20)
c2 = Vector(10, 20)
print(c1.compare(c2))

print("*"*50)
print('TASK-7:')
def numbers(input_list):
    result = {'odd': [], 'even': []}
    for number in input_list:
        if number % 2 == 0 and number not in result['even']:
            result['even'].append(number)
        elif number % 2 != 0 and number not in result['odd']:
            result['odd'].append(number)
    return result
input_list = [5, 8, 10, 13, 100, 104, 107, 13, 1031, 5, 1245, 1111, 10, 1031, 8, 1032]
dict = numbers(input_list)
print(dict)
print("*"*50)
print('TASK-8:')
print('8.1:Write a function to generate a list of square of values from a given dictionary.')
def squares(input_dict):
    squares_dict={key: value**2 for key,value in input_dict.items()}
    return squares_dict
input_dict = {"Total_classes": 2, "Total_students": 10}
squaresdict=squares(input_dict)
print('Squares of values:',squaresdict)
print('8.2:Generate a list of elements that cannot be divided by \"2\" from a given input list.')



















