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

# algorithm 4 - Hunter
def cpu_discard(cpu, next_player, cpu_hand, next_player_pile):
    """
    Allows the computer to decide what card to discard in Spoons.
    
    Parameters:
        cpu (str): Name of the computer player
        next_player (str): Name of the next player
        cpu_hand (list of str): The computer's current hand
        next_player_pile (list of str): The next players trash pile

    Returns:
        str or None: The card that was discarded, or None

    Side Effects:
        Removes the discarded card from cpu_hand
        Adds the discarded card to the next_player_pile
    """
    for i in range(len(cpu_hand)):
        for j in range(i + 1, len(cpu_hand)):
            if cpu_hand[i][:-1] == cpu_hand[j][:-1]:
                for card in cpu_hand:
                    if card[:-1] != cpu_hand[i][:-1]:
                        cpu_hand.remove(card)
                        next_player_pile.append(card)
                        return card
    return None
