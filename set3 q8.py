#guessing game


i=1
num=5
guess=1
while i<=5:
    guess=int(input("enter your guess"))
    if guess<5:
        print("your guess is less than number,try again")
    elif guess>5:
        print("your guess is greater than number,try again")
    else:
        print("wow, you guessed the number")
    i=i+1