from art import logo
from random import randint

answer = randint(1, 100)
chances_left = 0
quit_game = False
print(logo)
print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy'/'hard' or 'Extreme': ").lower()

if difficulty_level == "easy":
	chances_left += 10
elif difficulty_level == "hard":
	chances_left += 5
elif difficulty_level == "extreme":
	chances_left += 3
else:
	print("Invalid Input You Lost!")

while chances_left > 0:
	user_guess = int(input("Make a guess:"))
	if user_guess > answer:
		print("Too high.")
		chances_left -= 1
		if not user_guess == answer:
			print("Guess again.")
			print(f"You Have {chances_left} Chances Left")
	elif user_guess < answer:
		print("Too low.")
		if not user_guess == answer:
			print("Guess again.")
			print(f"You `Have {chances_left} Chances Left")
		chances_left -= 1
	elif user_guess == answer:
		print(f"You got it! The answer was {answer}")
		chances_left = 0

