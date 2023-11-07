import random

class Hangman:

    def __init__(self, word_list, num_lives = 5) -> None:
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess: str):
        guess = guess.lower()

        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')

            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')


    def ask_for_input(self):
        while True:

            guess = input('Enter a single letter: ')

            if len(guess) != 1 and not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)


if __name__ == '__main__':

    word_list = ['apple', 'kiwi', 'pear', 'blueberry', 'banana']

    h = Hangman(word_list=word_list)
    print(h.word)