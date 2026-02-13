import random
number = random.randint(0,50)

guess = int(input("Guess number between 0 and 50"))
guess_history = " "

def guess_history():
    return guess

while guess != number:
    if guess > number:
        print(f"The number is lower than {guess}")
        guess_history =+ guess
        guess = int(input("Guess again from 0 to 50"))
    if guess < number:
        print(f"The number is greater than {guess}")
        guess_history =+ guess
        guess = int(input("Guess again from 0 to 50"))

print("You were correct!")
print(guess_history)