import random 
computerNumber = random.randint(0,10)
userGuess = int(input("Guess what number I am thinking of from 0 - 10 "))
if (userGuess == computerNumber):
  print("You guessed it correctly")
else:
  print("Wrong! My number was " + str(computerNumber))
  