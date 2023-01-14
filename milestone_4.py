#%%
import random

class Hangman():
    def __init__(self,word_list,num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = list('_'*len(self.word))
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self,guess):
        if guess.lower() in self.word:
            print(f'Good guess! {guess.lower()} is in the word.')
    
    def ask_for_input(self):
        while True:
            guess = input('enter your guess: ')
            if len(guess) != 1 and not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                break



    
