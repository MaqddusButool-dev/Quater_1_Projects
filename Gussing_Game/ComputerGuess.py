from random import randint

def guess_number( sec_number, x):
   print("=====================================Let's Play Guess the Number!=================================================")
   print(sec_number)
   low = 1
   high = x
   feedback = ''
   attempts = 0
   while(feedback != "c"):
    if(low != high):
      guess = randint(low, high)
    else:
      guess = low
    feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
    if(feedback == "h"):
      high = guess - 1
    elif(feedback == "l"):
      low = guess + 1
    attempts += 1
   print(f"conguratulations, You got number in {attempts} attempts")


guess_number( 5, 10)