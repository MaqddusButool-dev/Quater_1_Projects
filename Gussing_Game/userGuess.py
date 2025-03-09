from random import randint


def guess_number (x):

  print("=====================================Let's Play Guess the Number!=================================================")
  print(f"=============================I'm thinking of a number between 1 and {x}.==================================================")
  guess = 0
  attempts = 0

  random_number = randint(1,x)

  while(guess != random_number):
    guess = int(input(f"your Guess : "))
    attempts += 1
    if(guess < random_number):
      print("Sorry, guess again, too low")
    elif(guess > random_number):
      print("Sorry, guess again, too high")
    else:
      print(f"conguratulations, You got number in {attempts} attempts")
      print(f"the number was {random_number}")
guess_number(10)