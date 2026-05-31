import random

secret_number = random.randint(1, 10)
guess = int(input("guess the number from (1,10):"))
attempts = 1
while guess != secret_number:
    if guess < secret_number:
        print("Too low! try again.")
    elif guess > secret_number:
        print("Too high! try again.")
    guess = int(input("guess the number again:"))
    attempts += 1
print("Congrats! you did it.")
print("you found it in", attempts, "attempts.")
print("secret number:", secret_number)