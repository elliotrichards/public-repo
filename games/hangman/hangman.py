import random
import csv
import string

# initialise lives
lives = 0

# create a small list of words for easier testing
# words = ['elephant', 'jumper', 'leg']

# pick a random word from words list
# random_word = random.choice(words)

# set the heart symbol emoji to represent 'lives'
heart_symbol = u'\u2764'

# create an empty list to store the guessed letters
guessed_letters = []
guessed_word_correctly = False

# use a function to read in a csv file, in this case a words list of nouns
def read_and_randomize_csv(filepath):
    """
    Reads a CSV file into a list and then randomizes the list.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        list: A new list containing the randomized data from the CSV file.
              Returns an empty list if the file is not found or empty.
    """
    data_list = []
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                # Assuming each row is a single item.
                # If your CSV has multiple columns, you might want to adjust this.
                if row: # Ensure the row is not empty
                    data_list.append(row[0]) # Append the first element of the row
        random.shuffle(data_list)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data_list

# set the filename
file_name = 'english-nouns.txt'
randomized_nouns = read_and_randomize_csv(file_name)
random_word = random.choice(randomized_nouns)
# This makes the clue automatically match the length of any random_word chosen, which is more robust.
clue = ['?'] * len(random_word)



# create a function to update the guessed word
def update_clue(guessed_letter, random_word, clue):
    index = 0
    while index < len(random_word):
        if guessed_letter == random_word[index]:
            clue[index] = guessed_letter
        index += 1
        

# Let's create difficulty levels based on lives
while lives == 0:
    choose_level = input("Choose your difficulty level. \n(e)asy\n(n)ormal\n(h)ard\n\nkey your choice: ")
    if choose_level == "e":
        lives = 15
    elif choose_level == "n":
        lives = 9
    elif choose_level == "h":
        lives = 5
    else:
        print("You need to select a level to continue.")




while lives > 0:
    print(f"\nLives left: {lives} " + heart_symbol * lives)
    print(f"Word: {''.join(clue)}") # join the list to print the word
        
    # Added .lower() to the input() so that the user's guess (whether uppercase or lowercase) is consistently handled, making the game more forgiving.
    guess = input("\nGuess a letter or the whole word: ").lower()
    # append eash guess to the empty list we created
    guessed_letters.append(guess)

    # check if the user guessed the entire word correctly
    if guess == random_word:
        guessed_word_correctly = True
        print(f"\nYou won! The secret word was {random_word}!")
        break
    
    # check if the guessed letter is in the secret word
    # Added a simple check if len(guess) == 1 and guess.isalpha(): to ensure the user is actually entering a single letter if they're not guessing the whole word.
    if len(guess) == 1 and guess.isalpha():
        if guess in random_word:
            print("\nYou guessed a letter correctly!")
            update_clue(guess, random_word, clue)
            # print a list of guessed letters
            print(''.join(guessed_letters))
            if ''.join(clue) == random_word:
                guessed_word_correctly = True
                print(''.join(clue)) # show the completed word
                print(f"\nYou won! The random word was {random_word}!")
                break
        else:
            print("\nIncorrect, you lose a life.")
            # print a list of guessed letters
            print(''.join(guessed_letters))
            lives -= 1
    else:
        print("\nInvalid guess. Please guess a single letter or the whole word.")

    if lives == 0:
        print(f"\nYou lost all your lives! The secret word was {random_word}!")
        break
                    
print("\nThanks for playing!")

