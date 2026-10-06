#NS, hangman
import random

# create a list of 10 words on a seperate txt file.
with open ("hangman_word.txt" , "r") as file:
    words = file.read().splitlines()
hangman_word = random.choice(words).lower()
print("Loading word list from words.txt...")

#create another file holds win/loss
#use split(", ") on the contents of word txt document to create your list of words
#pull win and lose totals from the other txt file annd save them as 2 seperate variabales

with open ("hangman_stats.txt" , "r") as file:
    content  = file.read().split(",")

win = int(content[0])
loss = int(content[1])


# built the hangman game



# save the correct word as a variable random.choice(name of the list)
#number of wrong guesses
wrong_guesses = []
#what letters have been guessed
guessed_letter = []

#function to display the hangman (needs the nmber of wrong guesses)
def display_hangman(wrong_guesses):
    stages = [
        """
           ----

          |    |
          |    
          |   
          |   
          |
        ---------""",
        """
           ----

          |    |
          |    O
          |   
          |   
          |
        ---------""",
        """
           ----

          |    |
          |    O

          |    |
          |   
          |
        ---------""",
        """
           ----

          |    |
          |    O

          |   /|
          |   
          |
        ---------""",
        """
           ----

          |    |
          |    O

          |   /|\\
          |   
          |
        ---------""",
        """
           ----

          |    |
          |    O

          |   /|\\
          |   /
          |
        ---------""",
        """
           ----

          |    |
          |    O

          |   /|\\
          |   / \\
          |
        ---------"""
    ]
    print(stages[wrong_guesses])




#function to show the letters and spaces(the correct word, letters that have been guessed)
def abc(hangman_word, guessed_letter):
        #variabel for display word(starts as an empty string)
    display_word = ""
#loop over the correct word
    for letter in hangman_word:
    #variabel for display word(starts as an empty string)
    #check if letter have been guessed
        if letter in guessed_letter:
        #then add the letter to the display word
            display_word += letter
    #if they havent guessed the letter
        else:
        #add an underscore to the display word
            display_word += "_"
#return the finished display word (outside of the loop)
    return display_word

#main gam e loop(while true)
while True:
    #call function to show hangman
    display_hangman(len(wrong_guesses))
    #print function call to show display word
    current_display = abc(hangman_word, guessed_letter)
    print("word: " + current_display)
    print("guessed letter:", " ".join(guessed_letter))
    print("wrong guesses:", " ".join(wrong_guesses))
    # create variable and ask user to guess a letter
    guess = input("guess a letter: ").lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        print("please enter 1 letter!")
        continue
    #add the letter to the list of guessed letters
    if guess in guessed_letter:
        print("you have already guessed that letter!")
    guessed_letter.append(guess)
    #check if not letter in word:
    if guess not in hangman_word:
        #increase incorrect guesses
        wrong_guesses.append(guess)
    #check for win status
    current_word = abc(hangman_word, guessed_letter)
    #chec if display word is same as the word
    if current_word == hangman_word:
        #tell user they won!
        print("you won!")
        # increase win total
        win += 1
        # update 
        with open("hangman_stats.txt", "w") as file:
            file.write(f"{win}, {loss}")
        #asd if they wanna play again
        play_again = input("do you want to play again? (y/n): ").lower()
        if play_again == "y":
            #reset random word, reset wrong count)
            hangman_word = random.choice(words).lower()
            print(hangman_word)
            wrong_guesses = []
            guessed_letter = []
            continue
        else:
            break
    #check to see if they lost (if they have 6 wrong guesses)
    if len(wrong_guesses) >= 6:
        # tell them they lost
        print("you lost!")
        #tell them what the word was
        print(F"The word was: {hangman_word}")
        #increase the lost count
        loss  += 1
        #update
        with open("hangman_stats.txt", "w") as file:
            file.write(f"{win}, {loss}")
        #ask if they want to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == "y":
            hangman_word = random.choice(words).lower()
            wrong_guesses = []
            guessed_letter = []
            continue
        else:
            break
