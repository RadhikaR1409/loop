i=1
n=5
k=1
while i<=5:
    b=1
    while b<=5-i:
        print(" ", end="")
        b=b+1
    j=1
    while j<=k:
        print(j,end="")
        j=j+1
    k=k+2
    print()
    i=i+1



for i in range(1,6):
    for j in range(5-i):
        print(" ",end="")
    for k in range(2*i-1):
        print(k,end="")
    print()

