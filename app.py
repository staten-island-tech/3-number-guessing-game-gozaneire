random = range(20)
guess = input("Guess a number from 0 to 20")
history = int(guess)
for i in guess:
    if guess == random:
        print("You were correct")
        quit()
    else:
        print("Wrong guess")
        print(guess)
        guess = input("Guess a number from 0 to 20")