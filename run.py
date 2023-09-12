import random

'''
Generate random numbers between 1-100 in the game.
'''
random_number = random.randint(1, 100)

'''
Guess a number and the if/else statements will calculate
whether it is too high, low or correct answer.
'''
def guess_number():
    guess = None
    while guess != random_number:

        guess = int(input('Enter number between 1-100: '))

        if (guess < random_number):
            print('Number is higher than your guess')

        elif (guess > random_number):
            print('Number is lower than your guess')

        else:
            print('Congrats, You guessed correctly!')
            break


def start():
    name = input('Write your name here: ')
    print(f'Hello {name}, good luck!')
    guess_number()


print('Add welcome text & rules here')
start()