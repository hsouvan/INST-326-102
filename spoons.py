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
