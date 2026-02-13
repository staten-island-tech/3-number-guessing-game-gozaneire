import random
number = random.randint(0,50)

guess_history = []
guess = int(input("Guess number between 0 and 50"))

while guess != number:
    if guess > number:
        print(f"The number is lower than {guess}")
        guess_history.append(guess)
        guess = int(input("Guess number between 0 and 50"))
    if guess < number:
        print(f"The number is greater than {guess}")
        guess_history.append(guess)
        guess = int(input("Guess number between 0 and 50"))
    
print(f"You were correct! The number is {number}.")
print(guess_history)