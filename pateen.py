n=int(input("Enter number :"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")
#
def print_square_pattern(n):
    for i in range(n):
        if i==0 or i==n-1:
            print("* " * n)

# Example: Printing a square pattern of size 5
print_square_pattern(10)
