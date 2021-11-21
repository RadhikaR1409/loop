num=int(input("enter a number"))
#for i in range(0,num):
 #   for j in range(0,i+1):
  #      print("*", end="")
   # print()




i=1
while i<=num:
    j=1
    while j<=num-i:
        print(" ",end="")
        j=j+1
    k=1
    while k<=i:
        print("*",end="")
        k=k+1
    print()
    i=i+1