import random
import argparse

def guess_number(start_range, end_range, guess_limit):
    random_number = random.randint(start_range, end_range)
    guess_count = 0
    while guess_count < guess_limit:
        guess = int(input("Enter your guess (between {} and {}): ".format(start_range, end_range)))
        if guess < random_number:
            print("Enter higher number")
        elif guess > random_number:
            print("Enter lower number")
        else:
            print("Congratulations! You guessed the number.")
            return
        guess_count += 1
    print("Sorry, you didn't guess the number. The number was {}.".format(random_number))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Number Guessing Game')
    parser.add_argument('-s', '--start', type=int, default=0,
                        help='start range for random number (default: 0)')
    parser.add_argument('-e', '--end', type=int, default=100,
                        help='end range for random number (default: 100)')
    parser.add_argument('-g', '--guesses', type=int, default=5,
                        help='number of guesses allowed (default: 5)')
    args = parser.parse_args()

    guess_number(args.start, args.end, args.guesses)


# python number_guessing_game.py -s START_RANGE -e END_RANGE -g GUESS_LIMIT
