#! use python3
# sort alpha game

import time
import random

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
QUIZ_SIZE = 3
QUIZ_DURATION = 30

def slowprint(text, duration):
    for char in text:
        print(char, flush=True, end='')
        time.sleep(duration)
    print()
        
slowprint(ALPHABET, 0.02)
slowprint('QUIZ'.center(len(ALPHABET)), 0.02)
slowprint(''.join(sorted(ALPHABET, reverse=True)), 0.02)

print('''By myself
Game has only {} seconds!
For example: 
   a e w t --> aetw 
   sort these'''.format(QUIZ_DURATION))

print('press Enter to start:')
input()
startTime = time.time()

while True:
    quiz = random.sample(ALPHABET, QUIZ_SIZE)
    print(' '.join(quiz))
    print()
    response = input('>').upper()
    if time.time() - startTime >= QUIZ_DURATION:
        print('TIME IS UP!')
        break

    quiz.sort()
    if list(response) == quiz:
        print('Correct!')
    else:
        print('Wrong!')
        
    
