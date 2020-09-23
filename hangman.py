import random

# Grab the list of available words
with open("word_list.txt", "r") as words:
    words = words.readlines()

# denotes our number of guesses
life = 7
# used to keep track of our "correctly gussed" letters
counter = 0
# keep track of attempts
attempts = []

# grab a random word
word = list(random.choice(words).replace("\n", ""))
# record the len to match our counter, saves us some performance
word_len = len(word)
# prints * x the len of word (e.g. 'coal' ****)
word_hidden = ["*" for letter in word]
print(word)
while life:
    # if the user has guessed the word correctly
    if counter == word_len:
        import sys
        sys.exit("Congratulations you win")
        
    # Print word_hidden as a string
    print("".join(word_hidden))
    # Convert to string so we can index
    guess = str(input("Please enter your next guess: "))[0:1]

    # if an attempt has been maded using this letter then skip this iteration and reduce a life
    if guess in attempts: continue
    
    # add guess to our attempts
    attempts.append(guess)

    # Collect all position(s) of guess
    positions = [position for position, char in enumerate(word) if char == guess]
    # if receieved positions, then replace the word_hidden and increase our counter
    if len(positions):
        for position in positions:
            word_hidden[position] = guess
            counter += 1
    else:
        life -= 1
        
print("You lose!")
