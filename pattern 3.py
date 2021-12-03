n=int(input("enter the nuumber of rows: "))
# i=1
# while n>0:
#     b=1
#     while b<i:
#         print(" ",end="")
#         b=b+1
#     j=1
#     while j<=(n*2)-1:
#         print("*",end="")
#         j=j+1
#     print()
#     n=n-1
#     i=i+1


for i in range(n,0,-1):
    for j in range(0,6-i):
        print(" ",end="")
    for k in range(2*i-1,0,-1):
        print("*",end="")
    print()
