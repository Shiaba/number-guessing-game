import random

'''
Add min & max value to variable and
generate random numbers between 1-100 in the game.
'''
min_value = 1
max_value = 100
random_number = random.randint(min_value, max_value)

'''
Guess a number and the if/else statements will calculate
whether it is too high, low or correct answer.
'''
def guess_number():
    guesses = 0
    while guesses < 3:
        print(f'Times guessed: {guesses}')

        guess = int(input('Enter number between 1-100: '))

        if guess < random_number:
            print('Number is higher than your guess')

        elif guess > random_number:
            print('Number is lower than your guess')

        else:
            print('Congrats, You guessed correctly!')
            break

        guesses = guesses + 1


def start():
    name = input('Write your name here: ')
    print(f'Hello {name}, good luck!')
    guess_number()


print('Add welcome text & rules here')
start()