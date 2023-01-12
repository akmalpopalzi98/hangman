while True:
    guess = input('guess the letter')
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print('invalid letter. Please enter a valid letter')