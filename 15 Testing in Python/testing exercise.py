#interactive guessing game
print('THIS IS AN INTERACTIVE GUESSING GAME BY CHRIS TIOYE')
from random import randint
attempt = 0
try:
    while True:
        try:
            guess = int(input('Please guess a number between 0 and 10 '))
            correct = randint(0, 10)
            attempt = attempt + 1

            if guess != correct:
                print(f'{attempt} Try again. The correct value was {correct}')
            elif guess == correct:
                print(f'{attempt} Wow, you are a genius!, you have guessed {correct} correctly in {attempt} attempts!')
                break
        except ValueError:
          attempt = attempt + 1
          print(f'{attempt} please enter a number')
except:
    pass