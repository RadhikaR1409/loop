# program to print"nav",if num divisible by 3,,,print "gurukul" if divisible by 7 and "navgurukul " , if divisible by both

i=1
while i<=100:
    if i%3==0 and i%7==0:
        print("nav gurukul")
    elif i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul")
    else:
        print(i)
    i=i+1