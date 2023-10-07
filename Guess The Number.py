from art import logo_list
from random import randint, choice

def play_game():
    max = 0

    chances_left = 0
    quit_game = False

    print(choice(logo_list))
    print("Welcome to the Number Guessing Game!")

    
    # Choose difficulty level
    print("Choose a difficulty:")
    print(" (0) - Child's Play")
    print(" (1) - Easy")
    print(" (2) - Hard")
    print(" (3) - Extreme")
    print(" (4) - Nightmare")
    user_input = input("Input: ").lower()

    if int(user_input) == 0:
        max = 10
        chances_left += 10
    elif int(user_input) == 1:
        max = 20
        chances_left += 10
    elif int(user_input) == 2:
        max = 50
        chances_left += 5
    elif int(user_input) == 3:
        max = 50
        chances_left += 3
    elif int(user_input) == 4:
        max = 100
        chances_left += 1
    else:
        print("Invalid Input. You Lost!")
        return

    print("I'm thinking of a number between 1 and {}.".format(max))
    print(f"You have {chances_left} chances left.")
    answer = randint(1, max)

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
        print(f"You have {chances_left} chances left.\n")
    
    if chances_left == 0:
        print(f"Sorry, you've run out of chances. The correct answer was {answer}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    play_game()
