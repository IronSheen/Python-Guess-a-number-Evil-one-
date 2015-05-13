# This is a guess the number game.
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()
maxNumber = int(random.randint(1, 1000000))

number = random.randint(1,maxNumber)
print('Well, ' + myName + ', I am thinking of a number between 1 and ' + str(maxNumber) + '.')

while guessesTaken < 20:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print ('Your guess is to low.')

    if guess > number:
        print('Your guess is to high')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('WOW, that\'s fucking great, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print ('What the fuck? You thought I was thinking of ' + number + 'Your fucking twat')


