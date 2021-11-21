#program to check is given number is prime or not


i=1
n=1
factors=0
n=int(input("enter a number"))
for j in range(1,n+1):
    if n%j==0:
        print(n,"is divisible by :" , j)
        factors=factors+1
    else:
        print(n, "is not divisible by :" , j)
if factors==2:
    print(n,"ek prime num hain")
else:
    print(n,"is not a prime number")