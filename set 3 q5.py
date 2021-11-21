#program to take weight of 11 people and find their average.


i=1
weight=1
sum=0
while i<=11:
    weight=int(input("enter your weight"))
    sum=sum+weight
    i=i+1
print("average weight =" , sum/11)
    
