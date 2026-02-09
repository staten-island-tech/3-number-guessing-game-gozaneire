import random
number = random.randint(0,100)

guess = int(input("Guess number between 0 and 100"))

if guess == number:
    print("You were correct")
    quit()
elif guess > number:
    print("The number was lower")
elif guess < number:
    print("The number was higher")