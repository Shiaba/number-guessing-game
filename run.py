import random

'''
Add min & max value to variable and
generate random numbers between 1-100 in the game.
'''
min_value = 1
max_value = 100
random_number = random.randint(min_value, max_value)


def guess_number():

    '''
    Guess a number and the if/else statements will calculate
    whether it is too high, low or correct answer.
    '''
    random_number = random.randint(min_value, max_value)

    guesses = 0
    win = False
    continue_playing = True

    while guesses < 7 and win is False and continue_playing is True:
        '''
        Inside the try, Raises Error if the guess is either not an integer or
        if it is below or above the min/max value.
        '''
        try:
            guess = int(input(f'Enter a number between {min_value} & {max_value}: \n'))

            if guess < min_value:
                print(f'Error! You need to write a number above {min_value}\n')
                continue
            elif guess > max_value:
                print(f'Error! You need to write a number below {max_value}\n')
                continue
        except ValueError:
            print(f'''
            Error! Write a number between {min_value} & {max_value}.\n
            ''')
            continue

        '''
        If there are no errors and the user has entered a
        number between the min & max value,
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
        print(f'Times guessed: {guesses}\n')
        '''
        Quit game option during gameplay
        '''
        quit_game = input('Enter any key to continue or n to quit game: \n')
        if quit_game == 'n':
            continue_playing = False
            break

    return win


def game_over():
    '''
    Quits or restarts the game.
    '''
    play_again = True
    restart_game = input('Enter any key to play again or n to quit game: ')
    if restart_game == 'n':
        play_again = False
        print('Thank you for playing!')

    else:
        return main()


def start_game():
    print(f"""
    Welcome!
    You get 7 tries to guess a number between {min_value} & {max_value}.
    If you can guess the correct number within your tries, you win.
    If you can't, you lose. Good luck!
    """)
    name = input('Write your name here: \n')
    print(f'Hello {name}, good luck!\n')


def main():
    '''
    Runs all the program functions
    '''
    start_game()
    result = guess_number()
    '''
    Get win/loss result
    '''
    if result is True:
        print(f'Congratulations, You guessed correctly!\n')
    else:
        print(f'''
        You lost, the correct number was {random_number}.
        Better luck next time!\n
        ''')

    game_over()


main()
