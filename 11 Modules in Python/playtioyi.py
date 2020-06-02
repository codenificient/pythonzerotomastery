#random game
from random import randint

attempt = 0
while True:
  try:
  	guess = int(input('Please guess a number between 0 and 10 '))
    correct = randint(0, 10)
    if guess != correct:
      print(f"{attempt} Try again. The correct value was {correct}")
			attempt = attempt + 1
    elif guess == correct:
			attempt = attempt + 1
      print(f"{attempt} Wow, you're a genius!, you have guessed {correct} correctly in {attempt} attempts !")
      break
  except ValueError:
		attempt = attempt + 1
    print("please enter a number")

