## Hangman: introductory project of the AiCore curriculum.

The project is an implementation of the classic hangman game, where the computer selects a word at random from a list of words, and the user attempts to guess it.

To play the game, run the play_game function in the file play_hangman.py, passing in a list of words as an argument, from which one will be randomly chosen for the user to guess.
Project Documentation

This introductory project in the AiCore curriculum introduces core concepts such as version control, object oriented programming, and programming good practice by the implementation of the classic game of hangman.
Milestone 1

Technologies / Skills:

    Command line (Bash and Command Prompt)
    Git
    GitHub

Gained familiarity with navigating the command line and the use of Git for version control and GitHub for web hosting.
Milestone 2

Technologies / Skills:

    VSCode
    Markdown
    Python data types

Milestone 3

Technologies / Skills:

    Python functions
    Comments, docstrings, and typing.

The ask_for_input function asks the user for input of a single, alphabetic character until a valid input is given. It then calls the check_guess function which checks if the inputed character is contained within the randomly selected word from the word list.
Milestone 4

Technologies / Skills:

    Object Oriented Programming

Implements ask_for_input and check_guess as methods in the Hangman class.
Milestone 5

Defines a function called play_game to insantiate and instance of the Hangman class and run the game as expected.


### Below is a quick summary detailing the logic of the code:

Task 1:

The aim of this task was to iteratively check if the input is a valid guess using a while in combination with if and else statements

Task 2:

The aim of this task was to check whether the guess is in the word

Task 3:

The aim of this task was to clean up the preceeding code by creating functions. Functions check_guess and ask_for_input were created.
check_guess checks whether the guess letter in the arg is in the word or not.
ask_for_input checks whether the entered letter is actually a letter or not.


Task 4:

For this task, the aim was to modify the check_guess method to deal with letters that are not in the chosen word. 
Within the else statement:
1. The value for num_Lives is reduced by 1 each time an incorrect guess is made
2. printing a messege that says the letter was incorrect
3. printing a final messege return the number of lives left


Task 5:

For this final task, the code in milestone 4 was put together called inside another function called play_game which took in a list of words.
Within the function, a hangman object was created which took in the word_list arg and num_lives arg.

a while statement was created and set to True. Within that block of code a num_lives check was made to see if it was = 0. If so, then the game would end.

An elif statement then checked whether the num_letters was > 0. If so, then the ask_for_input block would run and ask the user for the input. Finally, an if statement made the final checks to see if the game was completed. If so, the game would end and print winner. 
Technologies / Skills:

