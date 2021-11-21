num=int(input("enter a number :"))
i=2
if i==num:
    print(num,"is a prime number")
while i<num:
    if num%i==0:
        print(num,"is not a prime number")
        break
    else:
        print(num,"is a prime number")
        break
    
        i=i+1
    