import random

# Using invent your own computer games with python by  al sweigart

'''
Pseudo Code:
	| Start |
	| secret word |
	| show drawing |
	| ask user for a letter | ->  | player already  guessed this letter|
	| if letter is in word | -> | if letter is not in word| -> | limited guesses|
	| player guessed all letters| -> |player ran out of guesses|
	| ask player to play again | -> | start again |
	|end|




'''



HANGMAN_PICS = [
'''
 +---+
     |
     |    
     |
   ===''',
'''
 +---+
0    |
     |    
     |
   ===''','''
 +---+
0    |
|    |    
     |
   ===''','''
 +---+
 0   |
/|   |   
     |
   ===''','''
 +---+
 0   |
/|\  |    
     |
   ===''','''
 +---+
 0   |
/|\  |    
/    |
   ===''','''
 +---+
 0   |
/|\  |    
/ \  |
   ===''',

]

words = "cat kitty meowmeow kitten tiger lion gato fatty fuzzball".split()


# Functions

def get_random_word(word_list):
	word_index = random.randint(0, len(word_list) - 1) # what does this mean?
	return word_list[word_index]


def display_board():
	pass
def get_guess():
	pass
def play_again():
	pass


