# hangman game - we are given six lives and we have to guess the word before all our lives are lost


import random
import string
from words import words
# print(words)


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses a word from the list
    # keeps iterating till we get a valid word (which doesn't contain '-' or ' ') :
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    
    word = get_valid_word(words)
    print(word)
    word_letters = set(word)   # set of all letters in the word
    # set of all the upper case english letters
    alphabet = set(string.ascii_uppercase)  # from string module
    used_letters = set()  # what the user has guessed

    lives = 6

    # getting user input :
    while len(word_letters) !=  0 and lives >0:
        # letters already used :
        print("\nYou have",lives, "lives left and you have used the letters : ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word] # words that aren't guessed are dashes
        print("Current word  : ", ' '.join(word_list))

        user_letter = input("Guess a letter : ").upper()
        if user_letter in alphabet - used_letters:  # if this is a valid character that user haven't used yet
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else :
                lives = lives -1  # takes away a life  if wrong
                print(f"{user_letter} is not in word\n")
                
        elif user_letter in used_letters:
            print("You have already used that character,Please try again \n")
        else:
            print("Invalid character,Please try again \n")

    #  We are decrementing the letter in word by 1 each time so , this loop will iterate till the length of word_letter == 0
    # or all their lives are consumed
    if lives == 0 :
        return True


if hangman() :
    print("Sorry, You died !")
else : 
     print("Yay! you win")

