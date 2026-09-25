#NS, Number guessing game
import random

low = 1
high = 100
attemps = 6

number = random.randint(low,high)
print(f"I am thinking of a number, the highest number is {high} and the lowst number is {low}. you have {attemps} attemps.")

for attempt in range(1, attemps + 1):
    guess = int(input(f"Guess number{attempt}: "))
    if guess == number:
        print(f"Correct! You guessed it in {attempt} tries!")
        break  
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print(f"You're out of guesses! The number was {number}.")


