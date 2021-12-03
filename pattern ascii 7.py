i=1
k=1
while i<=5:
    b=1
    while b<=5-i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=k:
        print(chr(64+i),end="")
        j=j+1
    print()
    k=k+2
    i=i+1