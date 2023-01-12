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
