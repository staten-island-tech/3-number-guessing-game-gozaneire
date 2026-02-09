import random
number = random.randint(0,1000)

guess = int(input("Guess number"))
for i in number:
    if guess == number:
        print("You were correct")
        quit()
    else:
        print("Wrong guess")
        print(guess)