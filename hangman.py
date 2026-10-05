#NS, hangman
import random

# create a list of 10 words on a seperate txt file.
with open ("hangman_word.txt" , "r") as file:
    words = file.read().splitlines()
hangman_word = random.choice(words).lower()
print(hangman_word)


#create another file holds win/loss
with open ("


#use split(", ") on the contents of word txt document to create your list of words



# pull win and lose totals from the other txt file annd save them as 2 seperate variabales




# built the hangman game



# save the correct word as a variable random.choice(name of the list)
#number of wrong guesses
wrong_guesses = []
#what letters have been guessed
guessed_letter = []

#function to display the hangman (needs the nmber of wrong guesses)
"""
    ----
   |    |
   |    O
   |   /|\\
   |   /\\
   |
   ---------"""



#function to show the letters and spaces(the correct word, letters that have been guessed)
#loop over the correct word
    #variabel for display word(starts as an empty string)
    #check if letter have been guessed
        #then add the letter to the display word
    #if they havent guessed the letter
        #add an underscore to the display word
#return the finished display word (outside of the loop)

#main gam e loop(while true)
    #call function to show hangman
    #print function call to show display word
    # create variable and ask user to guess a letter
    #add the letter to the list of guessed letters
    #check if not letter in word:
        #increase incorrect guesses
    #chec if display word is same as the word
        #tell user they won!
        # increase win total
        #asd if they wanna play again
            #reset random word, reset wrong count)
    #check to see if they lost (if they have 6 wrong guesses)
        # tell them they lost
        #tell them what the word was
        #increase the lost count
        #ask if they want to play again
