# python file for the game
import random

# this function could probably add to a Game class - Anna
card_suits = ["Heart", "Diamond", "Club", "Spade"]
number_card = ["A", "2", "3", "4", "5", "6", "7", "8", "9", 
                       "10", "J", "Q", "K"]
def card_generate():
    """Generate the card deck to play with
    
    Returns:
        list: a list of the newly generated card deck"""
    card_deck = []
    for suit in card_suits:
        for number in number_card:
            card = suit + " " + number
            card_deck.append(card)
    return card_deck
card_deck = card_generate()

class Player:
    """Representation of player
    
    Attributes:
        name (str): name of the player
        cards (list): player's current card deck
    """
    
    def __init__(self, name):
        """Create a player
        
        Args:
            name (str): name of the player
        
        Side effects:
            initialize the attributes"""
        self.name = name
        self.cards = []
    
    def dealing(self, card_deck):
        """Dealing the card for each player
        
        Args:
            card_deck (list): pile of cards
        
        Side effects:
            add cards into players's card deck
                remove card from the card_deck
                print player's current card deck
        """
        self.cards = random.sample(card_deck, 4)
        for card in self.cards:
            card_deck.remove(card)
        print(f"{self.name}'s card deck: {self.cards}")
    
    def first_player_turn(self, card_deck):
        """Manage first player's turn
        
        Args:
            card_deck (list): pile of cards
            
        Side effects:
            add a card into player's card deck
                remove card from the card_deck
                print player's current card deck
        """
        card = random.choice(card_deck)
        self.cards.append(card)
        card_deck.remove(card)
        print(self.cards)
        
    def search(hiding_spot):
        """_summary_

        Args:
            hiding_spot (_type_): _description_
            
        Raises:
            Value Error: Hiding spots must be within the list of hiding spots or
            else this error is raised.
        """
        if hiding_spot not in hiding_rooms:
            pass
        
        
    def player_seek_spoons(hiding_rooms):
        """ Dictates how a player is able to find spoons from list of hiding 
            spots. Spoon-seeking ability may be affected by the player's given
            skill.
            
            Primary author: Gosi
            
            Techniques used:
            
            Args:
                hiding_rooms (dict): collection of hiding spots (list of tuples)
                where the spoons may be hidden, containing the name of the 
                hiding spot and its likelihood value, rooms do not have 
                likelihoods.
            
            Side Effects:
        """
        
        
        
        
    
    def swap_card (self, other):
        """Manage player’s turn in discarding one of their card
        
        Args: 
            other (Player): the next player
        
        Side effects:
            print player's current card deck
                ask player what card to discard to the next player, 
                delete the card from player’s card deck, 
                add the card to the next player’s card deck
        """
        print(f"{self.name}'s current card deck: {self.cards}")
        chosen_card = input("What card do you want to discard to the next player?\n")
        for card in self.cards:
            if card == chosen_card:
                del self.cards[card]
        other.cards.append(card)

# algorithm #1 - Gosi
"""
may not need hiding_rooms parameter if we place hiding methods in the Game class 
and make hiding_rooms a variable upon intialization

if in Game class, add randint import at beginning of game class 
"""
def set_hiding_spot_likelihood(hiding_rooms, difficulty = 2):
    from random import randint
    """Dictates how likely a spoon is to be in a hiding_spot based on chosen 
       difficulty. 

    Primary Author: Gosi
    
    Techniques Demonstrated:
    
    Args:
        hiding_rooms (dict): collection of hiding spots (list of tuples) where 
        the spoons may be hidden, containing the name of the hiding spot and its
        likelihood value, rooms do not have likelihoods. All hiding spots must
        have unique names.
        difficulty (str): value of 'easy', 'medium', or 'hard', that dictates 
        the range of likelihood between the hiding spots.
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

"""
may not need hiding_rooms parameter if we place hiding methods in the Game class 
and make hiding_rooms a variable upon intialization, same with hiding spots

if in Game class, add randint import at beginning of game class 
"""
def hide_spoons(hiding_rooms, hiding_spots, num_spoons):
    from random import randint
    """Sets index two of of a hiding spot in the dictionary hiding rooms to True
    if a spoon will be placed there. There will be number of players - 1 spoons
    hidden in a given game. To ensure proper randomization, rooms w

    Primary Author: Gosi
    
    Techniques Used: 
    
    Args: 
        hiding_rooms (dict): collection of hiding spots (list of tuples) where 
        the spoons may be hidden, containing the name of the hiding spot and its
        integer likelihood value, its boolean has_spoon value (rooms do not have
        likelihoods)
        hiding_spots(dict): complete key of all the hiding spots and their rooms
        num_players: an integer representing the number of spoons to be hidden
        
    
    Side Effects: 
        Changes the value of hiding_spot[2] where hiding spot is a 
        value in hiding rooms. True means a spoon is hidden there.
    """
    all_rooms = hiding_rooms.values()
    all_hiding_spots = set()
    for room in all_rooms:
        all_hiding_spots = set(room) | all_hiding_spots
    all_hiding_spots = list(all_hiding_spots)
    
    weighted_hiding_spots = all_hiding_spots.copy()
    for spot in all_hiding_spots:
        if spot[2] > 1:
            for likelihood in range(spot[2] - 1):
                weighted_hiding_spots.append(spot)
    
    for spoon in range(num_spoons):
        hide_spot = weighted_hiding_spots[
            randint(0, len(weighted_hiding_spots))]
        hiding_rooms[hiding_spots[hide_spot[0]]][hide_spot[0]][2] = True
        
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
