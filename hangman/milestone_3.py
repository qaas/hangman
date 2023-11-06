import random

word_list = ['apple', 'kiwi', 'pear', 'blueberry', 'banana']

word = random.choice(word_list)

def check_guess(guess: str):
    guess = guess.lower()

    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')


def ask_for_input():
    while True:

        guess = input('Enter a single letter: ')

        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')


if __name__ == '__main__':
    ask_for_input()