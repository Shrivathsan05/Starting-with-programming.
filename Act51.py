import random
Playing = True
Number = str(random.randint(0,9))
print(" I will genarate a number from 0 to 9, and you have to the number 1 digit at a time! ")
print(" The game ends when you get 1, Hero! ")
while Playing:
    Guess = input(" Give me your best guess!\n ")
    if Number == Guess:
        print(" You win the game! ")
        print(" The number was,", Number)
    else:
        print(" Your guess isn't quite right. Try again!\n ")