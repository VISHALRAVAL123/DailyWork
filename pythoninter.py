#Find the Sum of Digits in a Number:
#Write a Python program that calculates the sum of the digits in a given integer.
num = int(input("Enter an integer: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10
print("Sum of digits:", sum_of_digits)


#Factorial of a Number:
#Write a Python program to find the factorial of a non-negative integer.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a non-negative integer: "))
print("Factorial:", factorial(num))


#Fibonacci Sequence:
#Write a Python program to generate the first n terms of the Fibonacci sequence\
n = int(input("Enter the number of terms: "))
a, b = 0, 1
fibonacci_sequence = []
for _ in range(n):
    fibonacci_sequence.append(a)
    a, b = b, a + b
print("Fibonacci sequence:", fibonacci_sequence)


#Palindrome Check:
#Write a Python program to check if a given string is a palindrome (reads the same forwards and backwards).
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")

#Prime Number Check:
#Write a Python program to check if a given integer is a prime number.
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input("Enter an integer: "))
if is_prime(num):
    print("It's a prime number.")
else:
    print("It's not a prime number.")
#####################################
n=int(input("Enter N:"))
if n%2!=0:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print(n," Is Not Prime")
            break
    else:
        print(n," Is Prime")
else:
    print(n," Is Not Prime")

#Reverse a String:
#Write a Python program to reverse a given string.
input_str = input("Enter a string: ")
reversed_str = input_str[::-1]
print("Reversed string:", reversed_str)

#Find the Largest Number in a List:
#Write a Python program to find the largest number in a list of integers.
numbers = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
max_number = max(numbers)
print("Largest number:", max_number)

#Count Vowels in a String:
input_str = input("Enter a string: ")
vowels = "AEIOUaeiou"
vowel_count = sum(1 for char in input_str if char in vowels)

print("Number of vowels:", vowel_count)
