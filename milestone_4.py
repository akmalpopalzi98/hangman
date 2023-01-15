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
            for index,item in enumerate(self.word):
                if item == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1

        else:
            self.num_lives -=1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} left.')
    

    def ask_for_input(self):
        while True:
            guess = input('enter your guess: ')
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break



    
