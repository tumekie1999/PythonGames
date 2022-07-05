import random

def guess(x):
    c = ''
    low = 1
    high = x
    while guess != c:
        random_number = random.randint(low,x)
        print(f"CPU guess is {random_number}")
        guess = (input("Enter (H) for too high, (L) for too low or (C) for correct:   ")).lower
        if guess == "h":
            high = guess - 1 
        elif guess == "l":
            low = guess + 1
    
    print(f"you won! you guessed {guess} correctly")

guess(100)