n=int(input("enter a number: "))
original=n
sum=0
i=1
while i<n:
    if n%i==0:
        #print(i,"is a divisor ")
        sum=sum+i
    # else:
    #     print("not a divisor")
    i=i+1
if sum==original:
    print(n , "is a perfect number ")
else:
    print(n , "is not a perfect number")