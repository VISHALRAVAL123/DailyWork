'''
n=int(input("enter number : "))
a,b=0,1
print(a,end="")
print(b,end="")
for _ in range(n-2):
      a,b=b,a+b

      print(b,end=" " )
      
print("="*40)

n=int(input("enter number : "))
fact=1

for i in range(1,n+1):
    fact=fact*i
print(fact)

print("="*40)

a=10
b=20

a,b=b,a
print(a,b)

print("="*40)

n=6
for i in range(5):
    for j in range(i):
        print(i,end=" ")
    print(" ")

n=6
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print("")
print("="*40)
n=6
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==1-n:
            print("*",end="")
        else:
            print(" ",end="")
    print("")


print("="*40)

num=int(input("enter n="))
if num==2:
        print(num,"is number is prime")
elif num <=1 or num %2==0:
              print(num,"is number is not  prime")
else:
      for i in range(3,int(num**0.5)+1,2):
            if num % i==0:
                  print(num,"is number not is prime")
                  break
      else:
            print(num,"num is prime")

print("*"*40)
'''

n=int(input("enter n="))
for i in range(n):
      for j in range(n):
            if i==0 or i==n-1 or j==0 or j==1-n:
                  print("*",end="")
            else:
                  print(" ",end="")
      print("")


n=6
for i in range(1,n):
      for j in range(-1+i,-1,-1):
            print(format(2**j,"3d"),end='')
      print("")
      

      
