"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game(best_score):
	"""Psuedo-code Hints
	
	When the program starts, we want to:
	------------------------------------
	1. Display an intro/welcome message to the player.
	2. Store a random number as the answer/solution.
	3. Continuously prompt the player for a guess.
	  a. If the guess greater than the solution, display to the player "It's lower".
	  b. If the guess is less than the solution, display to the player "It's higher".
	
	4. Once the guess is correct, stop looping, inform the user they "Got it"
		 and show how many attempts it took them to get the correct number.
	5. Let the player know the game is ending, or something that indicates the game is over.
	
	( You can add more features/enhancements if you'd like to. )
	"""
	# write your code inside this function.

	#Note: I left the instructions as reference

	correct_ans = random.randint(1,10) #Stores a value between 1 and 10
	guesses = 1 #Guess count variable 
	


	print("Hello! We are going to play a number guessing game!")
	print("I will guess a number and you will try to figure it out")
	print("There will be hints if your guess is either too high or too low, so dont worry!\n")

	print("OK! I got a number picked in my noggin', so take a guess!")
	print("...I'll give you a hint, it's between 1 and 10....\n")

	#This should only show after the first game is played
	if best_score < 50:
		print("The best score thus far is {}, try to beat that!".format(best_score))


	while True:

		user_guess = input("Your number please  ")

		#handles non int values or outside number range
		try:
			user_guess = int(user_guess)
			if user_guess > 10 or user_guess < 1:
				raise ValueError()
		except ValueError:
			print("You either guessed outside the answer range or you entered something that was not a number. Let's try this again!\n")
			continue
		else:
			if user_guess == correct_ans:
				print("You got it right! WHOOP!")
				print("You got it right in {} guesses".format(guesses))
				#Can't seem to get the highscore to keep track
				if guesses < best_score:
					best_score = guesses
				break
			elif user_guess > correct_ans:
				print("Try going a bit lower")
				guesses += 1
				continue
			else:
				print("Try going a bit higher")
				guesses += 1
				continue


	print("That was fun, right? Thanks for playing the game!")

	#loops back to the beginning of the game
	play_again = input("Would you like to play again? Huh huh huh? Yes or no?").lower()
	if play_again == "yes" or play_again == "y":
		start_game(best_score)
	else:
		print("Goodbye!")

		

	



if __name__ == '__main__':
	# Kick off the program by calling the start_game function.
	start_game(50)
