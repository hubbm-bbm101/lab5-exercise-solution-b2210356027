import random
number=random.randint(0,100)
while True:
    guess = int(input("Enter your guess: "))
    if guess<number:
        print ("increase your number")
    elif guess>number:
        print ("decrease your number")
    else:
        print("you guessed right")
        break