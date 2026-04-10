# python file for the game

# algorithm 1

# algorithm 2

# algorithm 3 - Anna
def swap_card (player, next_player):
  """Manage player’s turn in discarding one of their card
  Args: 
    player (list):  the player card deck
    next_player (list): the next player card deck
  Side effects:
    ask player what card to discard to the next player, 
      delete the card from player’s card deck, 
      add the card to the next player’s card deck
  """
  print(player)
  chosen_card = input("What card do you want to discard to the next player?\n")
  for card in player:
    if card == chosen_card:
      del player[card]
  next_player.append(card)
  print(f"Player's Card Deck: {player}\nNext Player's Card Deck: {next_player}")

# algorithm 4

