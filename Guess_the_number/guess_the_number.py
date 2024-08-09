from art import logo
import random

def compare(guess, NUMBER):
    """Comparing the players number and the computers number"""
    if guess > NUMBER:
        print("Too high\n")
        return False
    elif guess < NUMBER:
        print("Too low\n")
        return False
    else:
        print(f"{guess} is the number! You win!")
        return True
        
def get_num_of_attempts(difficulty):
    """Set number of attempts"""
    # you can also use global variables
    if difficulty == 'easy':
        return 10
    return 5

print(logo)
#computer chooses a random number
NUMBER = random.randrange(1,100)

print("Welcome to the number Guessing Game! \nI'm thinking of a number between 1 and 100.")
print(f"Psss! the number is {NUMBER}")

#setting a game difficulty: Easy - 10 tries to guess, Hard - 5 tries

difficulty = input("Please select a difficulty. Type 'easy' or 'hard': ").lower()
tries = get_num_of_attempts(difficulty)



while tries > 0:
    guess = int(input(f"You have {tries} attempts remaining to guess the number.\nMake a guess: "))
    if compare(guess, NUMBER) == True:
        break
    else:
        tries -= 1
        if tries > 0:
            print("Guess again\n")
        else:
            print("You are out of tries. You loose!")

