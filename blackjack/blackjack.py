import random
from art import logo

def deal_card():
  """This function ramdomly deals a card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  """Takes the cards and calculates the summ"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if sum(cards) > 21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(player_score, computer_score):
  """Compares the player and computer scores and declares the result"""
  if player_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if player_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif player_score == 0:
    return "Win with a Blackjack 😎"
  elif player_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif player_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"
  
def play_game():
  print(logo)
  cards = []
  players_cards = []
  computers_cards = []
  is_game_over = False
  
  for i in range(2):
    players_cards.append(deal_card())
    computers_cards.append(deal_card())

  while not is_game_over:
    player_score = calculate_score(players_cards)
    computer_score = calculate_score(computers_cards)
    print(f"   Your cards: {players_cards}, current score: {player_score}")
    print(f"   Computer's first card: {computers_cards[0]}")

    if player_score == 0 or computer_score == 0 or player_score > 21:
      is_game_over = True
    else:
      player_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if player_should_deal == "y":
        players_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computers_cards.append(deal_card())
    computer_score = calculate_score(computers_cards)

  print(f"   Your final hand: {players_cards}, final score: {player_score}")
  print(f"   Computer's final hand: {computers_cards}, final score: {computer_score}")
  print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  #print("\n" * 200)
  play_game()