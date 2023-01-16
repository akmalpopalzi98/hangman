Milestone 2 consists of 5 main tasks:


Prior to starting this task, a git repository had to be set up in order save and track all changes

Task 1:

The aim of this task was to define a list containing 5 of your favourite fruits.
This list is then assigned to a variable named word_list


Task 2:

The aim of this task was to import a library called Random and to call to create a function that outputs random fruit from the list in Task 1

Task 3:

The aim of this task is to write a piece of code that asks the user to input a single string

Task 4:

Aim was to check whether the input to the previous task was a string or not

Task 5:

Create a read me file that describes the set of tasks in milestone 2. This was the final task for milestone 2
 
Milestone 3 consists of 3 main tasks:

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




