from art import logo
from random import randint

def play_game():
    answer = randint(1, 100)
    chances_left = 0
    quit_game = False

    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Choose difficulty level
    difficulty_level = input("Choose a difficulty. Type 'easy'/'hard' or 'extreme': ").lower()

    if difficulty_level == "easy":
        chances_left += 10
    elif difficulty_level == "hard":
        chances_left += 5
    elif difficulty_level == "extreme":
        chances_left += 3
    else:
        print("Invalid Input. You Lost!")
        return

    while chances_left > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess > answer:
            print("Too high.")
            chances_left -= 1
        elif user_guess < answer:
            print("Too low.")
            chances_left -= 1
        elif user_guess == answer:
            print(f"You got it! The answer was {answer}")
            print(f"You completed the game with {chances_left} chances remaining.")
            break
        print(f"You have {chances_left} chances left.")
    
    if chances_left == 0:
        print(f"Sorry, you've run out of chances. The correct answer was {answer}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    play_game()
