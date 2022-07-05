import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x}:   "))
        if guess < random_number:
            print(f"you guessed wrong, {guess} is too low!")
        elif guess > random_number:
            print(f"you guessed wrong, {guess} is too high")
    
    print(f"you won! you guessed {guess} correctly")

guess(100)

