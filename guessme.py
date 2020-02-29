import random

name = input('What\'s your name: ')
print(f'Hi there {name}, today we\'ll play a little guessing game. Try your best to guess a number between 1-20.')
random_int = random.randint(1, 20)
no_tries = int(input('Enter the number of guesses you want to take: '))
guess_took = 0
while guess_took < no_tries:
    guess = int(input('Enter your guess: '))
    guess_took += 1
    if guess > random_int:
        print('Too high')
    elif guess < random_int:
        print('Too low')
    elif guess == random_int:
        break

if guess == random_int:
    print(f'Hooray, you guessed the number, which is {random_int}, in {guess_took} tries ')

if guess != random_int:
    print(f'Oof, the number was {random_int}, sorry')