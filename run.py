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
    win = False
    continue_playing = True


    while guesses < 3 and win == False and continue_playing == True:
        print(f'Times guessed: {guesses}\n')

        try:
            guess = int(input(f'Enter a number between {min_value} & {max_value}: \n'))

            if guess < min_value:
                print('Below 1\n')
                continue
            elif guess > max_value:
                print('Above 100\n')
                continue
        except:
            print(f'Error! Write a number between {min_value} & {max_value}.\n')
            continue

        '''
        If there are no errors and the user has entered a number between the min & max value,
        the if/else statement will check if the conditions match.
        '''
        if guess == random_number:
            win = True
            break

        elif guess < random_number:
            print('Number is higher than your guess\n')

        else:
            print('Number is lower than your guess\n')


        guesses = guesses + 1
        '''
        Quit game option during gameplay 
        '''
        quit_game = input('Enter any key to continue or n to quit game: ')
        if quit_game == 'n':
            continue_playing = False
            break


    return win


def start_game():
    print('Add welcome text & rules here')
    name = input('Write your name here: \n')
    print(f'Hello {name}, good luck!\n')


def main():
    start_game()
    result = guess_number()
    '''
    Get win/loss result
    '''
    if result == True:
        print('Congratulations, You guessed correctly!\n')
    else:
        print(f'You lost, the correct number was {random_number}. Better luck next time!')


main()