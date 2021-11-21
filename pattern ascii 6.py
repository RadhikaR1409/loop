n=int(input("enter the number of rows"))
i=1
k=1
while i<=n:
    b=1
    while b<=n-i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=k:
        print(chr(64+j),end="")
        j=j+1
    k=k+1
    print()
    i=i+1