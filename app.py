import random
number = random.randint(0,100)

guess = int(input("Guess number"))

if guess == number:
    print("You were correct")
    quit()
else:
    print("Wrong guess")
    print(guess)