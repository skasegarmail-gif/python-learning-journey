import random

secret_number = random.randint(1, 10)
guess = int(input("guess the number from (1,10):"))
attempts = 1

while guess != secret_number and attempts < 5:
    if guess < secret_number:
        print("Too low! try again.")
    elif guess > secret_number:
        print("Too high! try again.")
    attempts += 1
    guess = int(input("guess the number again:"))

if guess == secret_number:
    print("Congrats! you did it.")
    print("You found it in", attempts, "attempts.")
else:
    print("Game Over!")
    print("The secret number was", secret_number)