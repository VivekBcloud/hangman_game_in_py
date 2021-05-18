import string
from words import choose_word
from images import IMAGES

'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    for l in secret_word:
        if l not in letters_guessed:
            return False
    return True
# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    letters_left = string.ascii_lowercase
    available_letters = ""
    for l in letters_left:
        if l not in letters_guessed:
            available_letters += l
    return available_letters
def show_image(remaining_lives):
    print(IMAGES[8-remaining_lives])
    show_remaining_lives(remaining_lives -1 )

def show_remaining_lives(remaining_lives):
    print("")
    print("Remaining Lives:",remaining_lives)
    
def show_hint(letters_guessed,secret_word):
    for letter in secret_word:
        if letter not in letters_guessed:
            return letter

def is_Valid_input(input_character, letters_guessed):
    if len(input_character) == 1 and ord('a') <= ord(input_character) <= ord('z') and (input_character not in letters_guessed): 
        return True
    else:
        return False

# print(get_available_letters(['c','h','w','z']))
def hangman(secret_word,remaining_lives,letters_guessed,start,hint_used):

    if start:
        print("Welcome to the game, Hangman!")
        print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    

    available_letters = get_available_letters(letters_guessed)
    print("Available letters: {} ".format(available_letters))

    guess = input("Please guess a letter: ")
    letter = guess.lower()
    if letter == 'hint' and not hint_used:
        # hint_used = True
        hint_letter = show_hint(letters_guessed,secret_word)
        letters_guessed.append(hint_letter)
        print("Hint used: {}".format(get_guessed_word(secret_word, letters_guessed)))
        if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                return

    if is_Valid_input(letter, letters_guessed):
        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                return
            show_remaining_lives(remaining_lives)
        else:
            print("Oops! That letter is not in my word: {} ".format(get_guessed_word(secret_word, letters_guessed)))
            letters_guessed.append(letter)
            print("")
            show_image(remaining_lives)
            remaining_lives -= 1
            if remaining_lives == 0:
                print("\n *--GAME OVER--*")

        if remaining_lives:
            hangman(secret_word,remaining_lives,letters_guessed,False,hint_used)
    else:
        if letter == 'hint' and not hint_used:
            hint_used = True
            hangman(secret_word,remaining_lives,letters_guessed,False, hint_used)
        else:
            print("Invalid input",letter)
            hangman(secret_word,remaining_lives,letters_guessed,False, hint_used)

secret_word = choose_word()
hangman(secret_word,8,[],True, False)
