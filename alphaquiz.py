#! use python3
# sort alpha game

import time
import random

# Set up the constants
QUIZ_SIZE = 3
QUIZ_DURATION = 30
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def slowprint(text, duration):
    for char in text:
        # Set flush=True here so the text is immediately printed
        print(char, flush=True, end='') # end='' means no newline
        time.sleep(duration) # Print a newline
    print()

# Fancy animation for the title:
slowprint(ALPHABET, 0.02)
slowprint('QUIZ'.center(len(ALPHABET)), 0.02)
slowprint(''.join(sorted(ALPHABET, reverse=True)), 0.02)

print('''By myself
Game has only {} seconds!
For example: 
   a e w t --> aetw 
   sort these'''.format(QUIZ_DURATION))

print('press Enter to start:')
input() # Let the player press Enter to start the game

startTime = time.time() # Get the current time for the start time
numCorrect = 0 # Number of questions answered correctly
while True: # Main game loop
    # Come up with QUESTION_SIZE letters for the question:
    quiz = random.sample(ALPHABET, QUIZ_SIZE)
    print(' '.join(quiz))
    print()
    response = input('>').upper()

    # Check if the quiz's time is up:
    if time.time() - startTime > QUIZ_DURATION:
        print('TIME IS UP!')
        break

    # Check if the response is correct:
    if list(response) == sorted(quiz):
        print('Correct!')
        numCorrect += 1 # Increase the score by 1
    else:
        print('Wrong!')
    # At this point, go back to the start of the main game loop.

# After the loop exits, the quiz is over, Show the final score:
print('In {} seconds you got {} correct!'.format(QUIZ_DURATION, numCorrect))
print('Thank you playing!')
        
    
