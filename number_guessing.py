import random

# Ask the player to choose difficulty
print("Choose difficulty level:")
print("1 = Easy (1–50)")
print("2 = Medium (1–100)")
print("3 = Hard (1–200)")

choice = input("Your choice: ")

if choice == "1":
    max_range = 50
    base_score = 120
    print("🔵 Difficulty: EASY")
elif choice == "2":
    max_range = 100
    base_score = 100
    print("🟡 Difficulty: MEDIUM")
else:
    max_range = 200
    base_score = 80
    print("🔴 Difficulty: HARD")

def give_hint(secret):
    if secret % 2 == 0:
        print("ℹ️ Hint: The secret number is EVEN.")
    else:
        print("ℹ️ Hint: The secret number is ODD.")

def show_attempts(attempts):
    print("Your attempts so far:", attempts)

def show_difference(secret, last_guess):
    diff = abs(secret - last_guess)
    print(f"🔍 You're {diff} away from the secret number.")

def show_trend(secret, attempts):
    if len(attempts) < 2:
        return
    prev_diff = abs(secret - attempts[-2])
    curr_diff = abs(secret - attempts[-1])
    if curr_diff < prev_diff:
        print("🔥 You're getting closer!")
    elif curr_diff > prev_diff:
        print("❄️ You're moving away!")

# Updated scoring depending on difficulty
def calculate_score(attempts, base_score):
    score = max(0, base_score - (len(attempts) - 1) * 10)
    return score

secret = random.randint(1, max_range)
attempts = []

print(f"🎲 Guess the number between 1 and {max_range}!")
print("Type 0 if you want a hint!")

while True:
    guess = int(input("Your guess: "))
    attempts.append(guess)

    if guess == 0:
        give_hint(secret)
        continue

    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")
    else:
        print(f"Correct! The number was {secret}.")
        print(f"You guessed it in {len(attempts)} attempts.")
        score = calculate_score(attempts, base_score)
        print(f"🏆 Your score: {score}")
        break

    show_attempts(attempts)
    show_difference(secret, guess)
    show_trend(secret, attempts)