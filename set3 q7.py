# guessing game,if intered number is 5 or less than or greater than it.



i=1
num=5
guess=1
while i<=5:
    guess=int(input("guess the number :"))
    if guess!=num:
        print("your guess is incorrect")
    else:
        break
    i=i+1

