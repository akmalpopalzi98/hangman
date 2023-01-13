import random

class Hangman():
    def __init__(self,word_list,num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        self.num_letters = None
        self.word_guessed = None
        self.word = random.choice(self.word_list)
        self.list_of_guesses = None

    

    
