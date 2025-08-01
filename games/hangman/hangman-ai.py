import random
import csv
import time

'''
This is the AI version of my game. Using Google Gemini I copied my original code and asked it to improve it, and it fed back the following code, tweaking what I had already written and actually
making the game a little more polished. Nice to see it in action and follow along, but it's not strictly my code! I'm including it here as an example along with my original which I'm still pleased with as a novice Python
learner.
'''

# initialise lives
lives = 0

# set the heart symbol emoji to represent 'lives'
heart_symbol = u'\u2764'

# create a slight pause in the game to make it easier to follow the messages
pause = 0.100

# create an empty list to store the guessed letters
guessed_letters = []

# use a function to read in a csv file, in this case a list of English nouns in the same directory
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
                if row:  # Ensure the row is not empty
                    data_list.append(row[0].lower())  # Append the first element of the row and convert to lowercase
        random.shuffle(data_list)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data_list

# set the filename
file_name = 'english-nouns.txt'
randomized_nouns = read_and_randomize_csv(file_name)

# Make sure there are words to play with.
if not randomized_nouns:
    print("No words found in the file. Exiting game.")
else:
    random_word = random.choice(randomized_nouns)
    # This makes the clue automatically match the length of any random_word chosen, which is more robust.
    clue = ['?'] * len(random_word)

    # create a function to update the guessed word
    def update_clue(guessed_letter, random_word, clue):
        for index, letter in enumerate(random_word):
            if guessed_letter == letter:
                clue[index] = guessed_letter

    # Let's create difficulty levels based on lives
    while lives == 0:
        choose_level = input("Choose your difficulty level. \n(e)asy\n(n)ormal\n(h)ard\n\nkey your choice: ").lower()
        if choose_level == "e":
            lives = 15
        elif choose_level == "n":
            lives = 9
        elif choose_level == "h":
            lives = 5
        else:
            print("You need to select a level to continue.")

    # Main game loop
    while lives > 0:
        time.sleep(pause)
        print("-" * 25)
        print(f"Lives: {lives} " + heart_symbol * lives)
        print(f"Word: {''.join(clue)}")
        print(f"Guessed letters: {', '.join(sorted(list(set(guessed_letters))))}")
        time.sleep(pause)
        
        guess = input("\nGuess a letter or the whole word: ").lower()

        # Check if the guess is a single letter or a full word
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
            else:
                guessed_letters.append(guess)
                if guess in random_word:
                    print(f"\nCorrect! '{guess}' is in the word.")
                    update_clue(guess, random_word, clue)
                    if ''.join(clue) == random_word:
                        print(f"\nYou won! The secret word was '{random_word}'!")
                        break
                else:
                    print(f"\nIncorrect, '{guess}' is not in the word. You lose a life.")
                    lives -= 1
        
        elif len(guess) > 1 and guess.isalpha():
            if guess == random_word:
                print(f"\nYou won! The secret word was '{random_word}'!")
                break
            else:
                print(f"\nIncorrect guess. '{guess}' is not the word. You lose a life.")
                lives -= 1
        else:
            print("\nInvalid guess. Please enter a single letter or the full word.")
        
        if lives == 0:
            print(f"\nGame over! You lost all your lives. The secret word was '{random_word}'!")

    print("\nThanks for playing!")
