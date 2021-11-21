num=int(input("enter the number : "))
copy=num
rem=0
sum=0
while num:
    rem=num%10
    sum=sum+rem
    num=num//10
if copy%sum==0:
    print("this is a harshad number")
else:
    print("this is not a harshad numeber")
