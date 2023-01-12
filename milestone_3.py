#%%
while True:
    guess = input('guess the letter')
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print('invalid letter. Please enter a valid letter')

#%%
guess

#%%
word = 'secret'

# %%
if guess in word:
    print(f'Good guess! {guess} is in the word')
else:
    print(f'Sorry, {guess} is not in the word')
# %%
def check_guess(letter):
    guessed_letter = letter.lower()
    if guessed_letter in word:
        print(f'Good guess! {guessed_letter} is in the word')
    else:
        print(f'Sorry, {guessed_letter} is not in the word')

#%%
def ask_for_input():
    while True:
        guess = input('guess the letter')
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('invalid letter. Please enter a valid letter')