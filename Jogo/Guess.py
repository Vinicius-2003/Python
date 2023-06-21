import random

import Guess


def playing():
    print('*' * 25)
    print('     Guessing Game')
    print('*' * 25)

    number_of_tries = 3
    points = 1000
    secret_number = round(random.randrange(1, 101))

    print('''
    (1) Easy Level 
    (2) Medium Level 
    (3) Hard Level\n ''')
    difficulty_game = int(input('Choose the difficult of the game : '))
    if difficulty_game == 1:
        number_of_tries = 20
    if difficulty_game == 2:
        number_of_tries = 10
    if difficulty_game == 3:
        number_of_tries = 5

    for rounds in range(1, number_of_tries + 1):
        print('Try {} of {}'.format(rounds, number_of_tries))
        guess_number = int(input('Pick up a number between 1 to 100 : '))

        correct_guess = guess_number == secret_number
        bigger_guess = guess_number > secret_number
        lower_guess = guess_number < secret_number

        if guess_number < 1 or guess_number > 100:
            continue
        if correct_guess:
            print('You were RIGHT, you made {} points!!\n'.format(points))
            break
        else:
            if bigger_guess:
                print('The number you guess is BIGGER than the right number!\n')
                if rounds == number_of_tries:
                    print("The secret number was {}. You made {} points".format(secret_number, points))
            elif lower_guess:
                print('The number you choose is LOWER than the right number!\n')
                if rounds == number_of_tries:
                    print("The secret number was {}. You made {} points".format(secret_number, points))

            lost_points = abs(secret_number - guess_number)
            points = points - lost_points
    number_tries = number_of_tries - 1

    print('Game Over')


if (__name__ == "__main__"):
    playing()
