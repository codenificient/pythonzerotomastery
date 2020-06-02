#game random automated

from random import randint
print('THIS IS AN AUTOMATED NUMBER GUESSING GAME BY CHRIS TIOYE')
attempt = 0
def guess(*args, **kwargs):
    correct = randint(*args, **kwargs)
    return correct
while True:
    try:
        oneguess = guess(0, 40)
        twoguess = guess(0, 40)
        if oneguess    == twoguess:
            attempt = attempt + 1
            print(f'{attempt} Yay! The guesses {oneguess} and {twoguess} match!')
            print(f'It took  {attempt}  attempts to get it right')
            break
        else:
            attempt = attempt + 1
            print(f'{attempt} the numbers {oneguess} and {twoguess} do not match. Starting over..')

    except ValueError:
        print('please enter a number')