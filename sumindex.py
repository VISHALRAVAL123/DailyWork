# Sample list of numbers
numbers = [10, 20, 30, 40, 50, 60, 70]

# List of indices for which you want to find the sum
indices = [1, 3, 5]

# Initialize the sum
sum_of_indices = 0

# Iterate through the indices and add the corresponding numbers to the sum
for index in indices:
    if 0 <= index < len(numbers):
        sum_of_indices += numbers[index]

print("Sum of numbers at specified indices:", sum_of_indices)
