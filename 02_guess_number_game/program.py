import random

print("------------------------------------")
print("       Guess That Number Game       ")
print("------------------------------------")
print()


the_number = random.randint(0, 100)


guess = -1

name = input("Player, what is your name? ")
#print(guess, type(guess))
#print(guess_text, type(guess_text))

while guess != the_number:
    guess_text = input("Guess a number between 0 and 100: ")
    guess = int(guess_text)
    if guess < the_number:
        print("Sorry {1}, your guess of {0} was too LOW".format(guess, name))
    elif guess > the_number:
        print("Sorry {1}, your guess of {0} was too HIGH".format(guess, name))
    else:
        print("Excellent work {1}, you won, it was {0}!".format(guess, name))

print("done")


