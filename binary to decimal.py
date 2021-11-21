i=0
rem=0
deci=0
num=int(input("enter a binary number :- "))
while num>i:
    rem=num%10
    deci=deci+rem
    num=num//10
print(deci)

