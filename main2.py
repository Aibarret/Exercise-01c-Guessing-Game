#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
import random
number = random.randrange(1,11)
guess = input("Guess a number from 1 to 10:  (EPIC GAMER HINT the number definitly isn't " + str(number) + ") ")
guess = int(guess)
more = 10
less =1
count = 0
score = 0
if count < 1:
    if guess == number:
        print("Great job! You got it!")
        score = score + 1

    if guess > more or guess <= less:
        print("Did you read the rules?")
        count = count + 1

    else:
        print("Sorry, better luck next time.")
        print("The number was " + str(number))
        count = count + 1

if count == 1:
    print("Uh oh you're running out of time!")
    number = random.randrange(1,11)
    guess = input("Guess a number from 1 to 10:  (EPIC GAMER HINT the number definitly isn't " + str(number) + ") ")
    guess = int(guess)

    if guess == number:
        print("Great job! You got it!")
        score = score + 1

    if guess > more or guess <= less:
        print("Did you read the rules?")
        count = count + 1

    else:
        print("Sorry, better luck next time.")
        print("The number was " + str(number))
        count = count + 1

if count > 1:
    print("C'mon! you can do it!")
    number = random.randrange(1,11)
    guess = input("Guess a number from 1 to 10:  (EPIC GAMER HINT the number definitly isn't " + str(number) + ") ")
    guess = int(guess)

    if guess == number:
        print("Great job! You got it!")
        score = score + 1

    if guess > more or guess <= less:
        print("Did you read the rules?")
        count = count + 1

    else:
        print("Sorry, better luck next time.")
        print("The number was " + str(number))
        count = count + 1

if count == 3:
    print("Last chance...")
    number = random.randrange(1,11)
    guess = input("Guess a number from 1 to 10:  (EPIC GAMER HINT the number definitly isn't " + str(number) + ") ")
    guess = int(guess)

    if guess == number:
        print("Great job! You got it!")
        score = score + 1

    if guess > more or guess <= less:
        print("Did you read the rules?")
        count = count + 1

    else:
        print("Sorry, better luck next time.")
        print("The number was " + str(number))
        count = count + 1

if count > 3:
    print("GAME OVER: " + str(score) + " POINTS")