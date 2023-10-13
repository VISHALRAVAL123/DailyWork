'''
def reverseList(lst):
 if not lst:
     return []
 return [lst[-1]] + reverseList(lst[:-1])
print(reverseList([1, 2, 3, 4, 5]))


n=5
#Upper part of the pattern
for i in range(1, n + 1):
    print('* ' * i)

# Lower part of the pattern
for i in range(n - 1, 0, -1):
    print('* ' * i)
'''
n = 5  # Number of rows

for i in range(n, 0, -1):
    print('* ' * i)


n = 5  # Number of rows

for i in range(1, n + 1):
    print(' ' * (n - i) + '* ' * i)

    
n = 5  # Number of rows

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=' ')
    print()

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the remaining unsorted portion of the list
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
my_list = [10, 5, 9, 4, 6, 8, 2, 3, 4, 89, 40, 65]
selection_sort(my_list)
print(my_list)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
my_list = [10, 5, 9, 4, 6, 8, 2, 3, 4, 89, 40, 65]
insertion_sort(my_list)
print(my_list)

