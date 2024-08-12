import random
from art import logo, vs
from game_data import data


def compare(a,b):
    """Comparing number of followers for Choise A nad Choice B"""
    if a['follower_count'] > b['follower_count']:
        return 'a'
    else:
        return 'b'
    
def get_user_choice():
    """Asking for users choice, limiting options to A or B"""
    choices = ['a', 'b']
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(logo)

    while user_input not in choices:
        print("Invalid choice. Please try again.")
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    return user_input
def high_or_low():
    """play High or Low game"""
    game_over = False
    score = 0
    index_a = random.randint(0, len(data) - 1)
    index_b = random.randint(0, len(data) - 1)
    while game_over == False:
        #use randomizer to choose a pair of items from Data list
        index_a = index_b
        index_b = random.randint(0, len(data) - 1)
        while index_a == index_b:
            index_b = random.randint(0, len(data) - 1) 
        a = data[index_a]
        b = data[index_b]

        #printing two items to compare and VS logo
        print(f"\nCompare A: {a['name'].title()}, {a['description'].title()}, from {a['country'].title()}\n")
        print(vs)
        print(f"\nAgainst B: {b['name'].title()}, {b['description'].title()}, from {b['country'].title()}\n")

        #checking the correct answer
        choice = get_user_choice()
        if choice == compare(a, b):
            score += 1
            print(f"\nYou're right! Current score: {score}.")
        else:
            game_over = True
            print(f"\nSorry, that's wrong. Final score: {score}.")

print(logo)
high_or_low()


