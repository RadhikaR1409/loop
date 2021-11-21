# armstrong number- 1**3+5**3+3**3=153
                #    1+125+27=153


i=1
sum=0
num=int(input("enter a number"))
original=num
while num>0:
    rem=num%10
    sum=sum+rem**3
    num=num//10
print("sum is", sum)
if sum==original:
    print("this is an armstrong number")
else:
    print("this is not an armstrong number")