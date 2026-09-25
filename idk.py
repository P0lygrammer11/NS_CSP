# NS - Number Guessing Game Assignment

import random

# --- CONFIGURATION & DOCUMENTATION ---
# Secret number range: 1 to 100
LOW_RANGE = 1
HIGH_RANGE = 100

# Limited number of attempts: 6
MAX_ATTEMPTS = 6
# ------------------------------------

# Generate the secret random number
secret_number = random.randint(LOW_RANGE, HIGH_RANGE)

print(f"I'm thinking of a number between {LOW_RANGE} and {HIGH_RANGE}. You have {MAX_ATTEMPTS} tries to guess it!")

# Loop structure to track attempts
for attempt in range(1, MAX_ATTEMPTS + 1):
    # Prompt the player for their guess
    guess = int(input(f"Guess #{attempt}: "))
    
    # Check the guess and provide accurate feedback
    if guess == secret_number:
        print(f"Correct! You guessed it in {attempt} tries!")
        break  # End the game immediately upon correct guess
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
else:
    # This else block runs only if the loop finishes naturally without hitting the 'break'
    print(f"You're out of guesses! The number was {secret_number}.")
