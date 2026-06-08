import random

secret_number = random.randint(1,20)
print("welcome to the number guessing game! I have picked a number between 1 and 20.")

while True:
  guess = int(input("enter your guess: "))

  if guess > secret_number:
     print("too High")
  elif guess < secret_number:
     print("Too low")
  else:
   print("Correct!")

   break





             