# Input from the user
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number.")
elif num <= 3:
    print(f"{num} is a prime number.")
elif num % 2 == 0 or num % 3 == 0:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            is_prime = False
            break
        i += 6
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


#####################################################
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
