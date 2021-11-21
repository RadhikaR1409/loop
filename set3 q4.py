# sum of multiples of 8 between 30 to 420


i=30
sum=0
while i<=420:
    if i%8==0:
        sum=sum+i
        print(i,"sum of multiples :", sum)
    #else:
     #   print("end")
    i=i+1
    