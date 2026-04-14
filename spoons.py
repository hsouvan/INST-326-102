# python file for the game

# algorithm 1 - Gosi
def set_hiding_spot_likelihood(hiding_rooms, difficulty):
    from random import randint
    """Dictates how likely a spoon is to be in a hiding_spot based on chosen 
       difficulty. 

    Args:
        hiding_rooms (dict): collection of hiding spots (list of tuples) where 
        the spoons may be hidden, containing the name of the hiding spot and its
        likelihood value, rooms do not have likelihoods
        difficulty (str): value of 'easy', 'medium', or 'hard', that dictates 
        the range of likelihood between the hiding spots and how many decoy
        spoons there are.
    Side effects: 
        Changes the likelihood value of hiding spots in the dictionary of hiding
        rooms.
    """
    
    rooms = hiding_rooms.keys()
    
    for room in rooms:
        for hiding_spot in hiding_rooms[room]:
            if(difficulty == 'easy'):
                hiding_spot[1] = 1
            elif(difficulty == 'medium'):
                hiding_spot[1] = randint(1, 2)
            else: 
                hiding_spot[1] = randint(1, 3)
    

# algorithm 2 - Andrew
def set_skill(cpus, player, skills_list):
    """Gives each of the players a skill.
    The human picks whilst the computer is given a random skill.
    No two players share the same skill.
    
    Args:
        cpu (str): name of the computer player
        player (str): name of the human player
        skills_list (list): list of premade skills
    Side effects:
        Asks what skill the player wants to choose from.
    Returns:
        dict: mapping of the player and their skill    
    """
    import random
    
    assigned_skills = {}
    available_skills = skills_list.copy()
    
    print("Available skills:")
    for i, skill in enumerate(skills_list):
        print(f"{1 + i}. {skill}")
        
    choice = int(input("Pick your skill: "))
    player_skill = skills_list[choice - 1]
    
    assigned_skills[player] = player_skill
    available_skills.remove(player_skill)
    
    for cpu in cpus:
        skill = random.choice(available_skills)
        assigned_skills[cpu] = skill

        available_skills.remove(skill)
        
    return assigned_skills

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
