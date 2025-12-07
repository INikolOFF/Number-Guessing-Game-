import random

secret = random.randint(1, 100)
attempts = []

print("🎲 Guess the number between 1 and 100!")

while True:
    guess = int(input("Your guess: "))
    attempts.append(guess)

    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")
    else:
        print(f"Correct! The number was {secret}.")
        print(f"You guessed it in {len(attempts)} attempts.")
        break