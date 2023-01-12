#%%
import random

#%%
word_list = ['apple','banana','mango','orange','strawberry']


#%%
print(word_list)

#%%
word = random.choice(word_list)
print(word)

# %%
guess = input('enter a single letter')

# %%
if len(guess) == 1 and guess.isalpha():
    print('good guess')
else:
    print('Oops! That is not valid')
# %%
