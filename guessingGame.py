chances = 5

import random

number = random.randint(1, 10)


print("Number guessing game")
print("Guess a number (between 1 and 9)")




while chances < 6:
    guess = int(input("Enter your guess:"))
    if guess == number:
        print("Congratulation YOU WON! ! !")
        break
    

    else:
        chances = chances - 1
        print("Your guess was too low: Guess a higher number than",guess)

    if chances < 1:
        print("You lose!!! The number is ",number)
        break
        



