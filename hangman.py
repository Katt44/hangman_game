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
	print HANGMAN_PICS[len(missed_letters)]
	print 'Missed letters: '
	blanks = '_' * len(secret_word)

	for i in range(len(secret_word)):
		if secret_word[i] in correct_letters
			blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

	for letter in blanks
		print letter + " "


def get_guess():
	pass
def play_again():
	pass

#calls	
print "H A N G M A N"
missed_letters = " "
correct_letters = " "
secret_word = get_random_word(words)
game_is_done = False
