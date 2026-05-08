# python file for the game
import random
import json
from argparse import ArgumentParser
from sys import argv

class Player:
    """Representation of player
    
    Attributes:
        name (str): name of the player
        cards (list): player's current card deck
        is_cpu (bool): whether or not a player is a computer, True if yes,
            default is False / human player
    """
    
    def __init__(self, name):
        """Create a player
        
        Args:
            name (str): name of the player
        
        Side effects:
            initialize the attributes"""
        self.name = name
        self.cards = []
        self.mode = "cards"
    
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
    
    def draw_card(self, card_deck):
        """Draws a card from the deck (random) and add to player's hand
        
        Args:
            card_deck (list): pile of cards remaining
            
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
        """Manage human player’s turn in discarding one of their card
        
        Args: 
            other (Player): the next player
        
        """
        raise NotImplementedError
        
    def check_four_of_a_kind(self):
        """Checks for four of a kind in a player's hand.
        
        Side effects:
            Once a player is confirmed to have four of a kind,
            they start checking for spoons.
        """
        # ranks = [card.split(" ", 1)[1] for card in self.cards]
        ranks = [card[0] for card in self.cards]
    
        for rank in ranks:
            if ranks.count(rank) == 4:
                self.mode = "spoons"
                print(f"{self.name} has 4 of a kind! They can now search for " +
                      "the spoon!")

    def search(self, hiding_rooms):
        """Allows a player to determine whether a hiding spot has a spoon (True)
        or not (False). If a spoon is found, they win and the game ends.
        
        Args:
            hiding_rooms (dict): hiding rooms which each have lists of hiding
            spots. Each hiding spot is a list that looks like this:
            [spot_name (str), likelihood (int), has_spoon (bool)]
        
        Returns:
            bool: True or False depending on whether there is a spoon hidden in 
                that hiding spot
        """
        raise NotImplementedError
    
    def set_skill(self, skills_list):
        """
        """
        pass
        
    

class HumanPlayer(Player):
    
    def __init__(self, name):
        """Create a player
        
        Args:
            name (str): name of the player
        
        Side effects:
            initialize the attributes"""
        self.name = name
        self.cards = []
        self.skill = None
        self.mode = "cards"
    
    def swap_card (self, other):
        """Manage human player’s turn in discarding one of their card
        
        Args: 
            other (Player): the next player
        
        Side effects:
            print player's current card deck
            ask player what card to discard to the next player, 
            delete the card from player’s card deck, 
            add the card to the next player’s card deck
        """
        print(f"{self.name}'s current card deck: {self.cards}")
        chosen_card = input("What card do you want to discard to the next" + 
                            "player?\n")
        for card in self.cards:
            if card == chosen_card:
                self.cards.remove(card)
        other.cards.append(card)
    
    def search(self, hiding_rooms):
        """Allows a player to determine whether a hiding spot has a spoon (True)
        or not (False). If a spoon is found, they win and the game ends.
        
        Args:
            hiding_rooms (dict): hiding rooms which each have lists of hiding
            spots. Each hiding spot is a list that looks like this:
            [spot_name (str), likelihood (int), has_spoon (bool)]
        
        Returns:
            bool: True or False depending on whether there is a spoon hidden in 
                that hiding spot
            
        Side Effects: 
            Prompts user for inputs for selecting room and hiding spot.
            Prints result of a search to the terminal (includes invalid)
            input messages or success/failure messages
        """
        
        print("Rooms:")
        for room in hiding_rooms:
            print(room)

        searched_room = input("Where do you want to search?\n").lower()
        
        if searched_room not in hiding_rooms:
            print("Invalid room.")
            return False
        
        print("Hiding spots:")
        for spot in hiding_rooms[searched_room]:
            print(spot[0])
        
        selected_spot = input("Which spot do you want to search?\n").lower()
        return self.check_spot(hiding_rooms, searched_room, selected_spot)

    #separated this portion of the search method for reusability
    def check_spot(self, hiding_rooms, room, selected_spot):
        for spot in hiding_rooms[room]:
            if spot[0] == selected_spot:
                if spot[2]:
                    print(f"A spoon has been found! {self.name} WINS!!!")
                    return True
                else:
                    print("No spoon found.")
                    return False         
        print("Invalid hiding spot.")
        return False

    def set_skill(self, skills_list):
        """Give player a skill
        
        Args:
            skills_list (list): list of premade skills
            
        Side effects:
            Asks what skill the player wants to choose from.   
        """
        print("Available skills:")
        for i, skill in enumerate(skills_list):
            print(f"{i + 1}. {skill}")
            
        choice = int(input("Pick your skill: "))
        self.skill = skills_list[choice - 1]
        skills_list.remove(self.skill)
        
    #SKILLS RELATED TO SEARCHING FOR SPOONS
    #SPOON COMPASS
    def spoon_compass(self, hiding_rooms):
        rooms_with_spoons = []
        
        for room in hiding_rooms:
            for spot in hiding_rooms[room]:
                if spot[2]:
                    rooms_with_spoons.append(room)
        
        rooms_with_spoons = list(set(rooms_with_spoons))
        
        if len(rooms_with_spoons) == 1:
            print(f"The compass strongly points towards the {rooms_with_spoons}"
                  + "!")
        else:
            print("The compass is spinning its pointer between two rooms!")
            print(f"It points to the following rooms: {rooms_with_spoons}")
    
    #OH SHINY!
    def oh_shiny(self, hiding_rooms):
        room = input("Pick a room to scan:\n").lower()
        
        if room not in hiding_rooms:
            print("Invalid room")
            return False
        
        spoon_found = any(spot[2] for spot in hiding_rooms[room])
        
        if not spoon_found:
            print(f"The room has no spoons in the {room}")
            return False
        
        print(f"Your scan revealed a spoon in the {room}!")
        #now that a spoon was scanned in selected room, follow-up
        #in the same turn for searching a spot
        print("Now you can search for a spot the spoon might be in:")
        for spot in hiding_rooms[room]:
            print(spot[0])
        
        selected_spot = input("Which spot do you select?\n").lower()
        return self.check_spot(hiding_rooms, room, selected_spot)
    
    
class ComputerPlayer(Player):

    def swap_card(self, other):
        """Allows the computer to decide what card to discard in Spoons.
        
        Parameters:
            other (Player): the next player 


        Side Effects:
            Removes the discarded card from cpu_hand
            Adds the discarded card to the next player
            print current card deck of the computer 
        """
        for i in range(len(self.cards)):
            for j in range(i + 1, len(self.cards)):
                if self.cards[i][:-1] == self.cards[j][:-1]:
                    for card in self.cards:
                        if card[:-1] != self.cards[i][:-1]:
                            self.cards.remove(card)
                            other.cards.append(card)
                            print(f"{self.name}'s current card deck: " + 
                                self.cards)
    
    def search(self, hiding_rooms):
        """Control how the computer search for spoons
        
        Args:
            hiding_rooms (dict): hiding rooms which each have lists of hiding
            spots. Each hiding spot is a list that looks like this:
            [spot_name (str), likelihood (int), has_spoon (bool)]
        
        Returns:
            bool: True or False depending on whether there is a spoon hidden in 
                that hiding spot
        """
        room = random.choice(list(hiding_rooms.keys()))
        spot = random.choice(hiding_rooms[room])
    
        print(f"{self.name} searches the {room} - {spot[0]}")
    
        if spot[2]:
            print(f"{self.name} found a spoon! {self.name} WINS!!!")
            return True
        else:
            print(f"{self.name} found nothing.")
            return False
    
    
class Game:
    """Class Representation of Spoons
    
    Attributes:
        hiding_rooms (dict): collection of hiding spots (list of tuples)
            where the spoons may be hidden, containing the name of the 
            hiding spot and its likelihood value, rooms do not have 
            likelihoods. All hiding spots musthave unique names.
        hiding_spots (dict): The keys are all possible hiding spots, and the 
            values are the rooms in which they are located 
        hiding_info (str): name of the json file in which the hiding spot and 
            hiding room dictionaries are located
        players (list): a list of Player objects, the human player will always
            be the first item in the list, followed by two computers
        num_spoons (int): number of spoons to be found, usually one less than 
            the number of players
    """
    
    def __init__(self, players, hiding_info):
        self.card_deck = ["AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", 
                       "10H", "JH", "QH", "KH", "AD", "2D", "3D", "4D", "5D", 
                       "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AC", 
                       "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", 
                       "JC", "QC", "KC", "AS", "2S", "3S", "4S", "5S", "6S", 
                       "7S", "8S", "9S", "10S", "JS", "QS", "KS"]
        self.players = players
        self.hiding_spots = None
        self.hiding_rooms = None
        self.num_spoons = len(players) - 1
        self.json_to_dict(hiding_info)
        self.skills_list = ["oh shiny", "spoon compass"]
        
    def json_to_dict(self, hiding_info):
        """Converts json file instance variable to relevant dictionaries.
        
        Primary Author: Gosi
        
        Techniques Demonstrated: json.load(), with keyword
        
        Side Effects: 
            Changes values of hiding_rooms and hiding_spots to the dictionaries
            in the json file
        """
        with open(hiding_info, 'r', encoding = 'utf-8') as reader:
            dict1 = dict(json.load(reader))
            self.hiding_rooms = dict(dict1['hiding_rooms'])
            self.hiding_spots = dict(dict1['hiding_spots'])
            
    def set_likelihood(self, difficulty):
        """Dictates how likely a spoon is to be in a hiding_spot based on chosen 
        difficulty. 
        
        Primary Author: Gosi
        
        Args:
            difficulty (str): value of 'easy', 'medium', or 'hard', that 
                dictates the range of likelihood between the hiding spots.
        
        Side effects: 
            Changes the likelihood value of hiding spots in the dictionary of 
                hiding rooms.
        
        Raises:
            ValueError: if provided a invalid difficulty level
        """
        rooms = self.hiding_rooms.keys()
        
        for room in rooms:
            for hiding_spot in self.hiding_rooms[room]:
                if(difficulty == "easy"):
                    hiding_spot[1] = 1
                elif(difficulty == "medium"):
                    hiding_spot[1] = random.randint(1, 2)
                elif(difficulty == "hard"): 
                    hiding_spot[1] = random.randint(1, 3)
                else:
                    return ValueError("Invalid Difficulty Level.")
    
                
    def hide_spoons(self):
        """Sets index two of of a hiding spot in the dictionary hiding rooms to 
        True if a spoon will be placed there. There will be number of 
        players - 1 spoons hidden in a given game most often. 
        
        Primary Author: Gosi
        
        Side Effects: 
            Changes the value of hiding_spot[2] where hiding spot is a 
            value in hiding rooms. True means a spoon is hidden there.
        """
        all_rooms = self.hiding_rooms.values()
        all_hiding_spots = set()
        for room in all_rooms:
            all_hiding_spots |= set((spot[0], spot[1], spot[2]) for spot in 
                                    room)
                        
        all_hiding_spots = list(all_hiding_spots)
        
        weighted_hiding_spots = all_hiding_spots.copy()
        for spot in all_hiding_spots:
            if spot[1] > 1:
                for likelihood in range(spot[1] - 1):
                    weighted_hiding_spots.append(spot)
        
        for spoon in range(self.num_spoons):
            hide_spot = weighted_hiding_spots[random.randint(0, 
                            len(weighted_hiding_spots)-1)][0]
            room = self.hiding_spots[hide_spot]
            for key in self.hiding_rooms[room]:
                if key[0] == hide_spot:
                    key[2] = True

    def turn(self, player):
        """Determines if a player is still trying for four of a kind,
        or searching for spoons.
        """
        player_index = self.players.index(player)
        if (player_index + 1) == len(self.players):
            other = self.players[0]
        else:
            other = self.players[self.players.index(player) + 1]
        if player.mode == "cards":
            player.swap_card(other)
            player.check_four_of_a_kind()
            return False
        elif player.mode == "spoons":
            if isinstance(player, HumanPlayer):
                skill_use = input("Do you want to use your skill? (y/n) ")
                if skill_use.ower() == "y":
                    if player.skill == "Name":
                        player.spoon_compass(self.hiding_rooms)
                        return False
                    elif player.skill == "Name":
                        return player.oh_shiny(self.hiding_rooms)
                else:
                    return player.search(self.hiding_rooms)
            else:    
                return player.search(self.hiding_rooms)   
    
    def play(self):
        """Play the Game
        """
        win = False
        for player in self.players:
            player.dealing(self.card_deck)
            player.set_skill(self.skills_list)
        turn = -1
        player = self.players[0].draw_card(self.card_deck)
        while not win:
            turn += 1
            player = self.players[turn % len(self.players)]
            win = self.turn(player)
        print("Game End!")           
        
            
def main(filepath): 
    players = []
    player_name = input("What is your name? ").capitalize()
    difficulty = input("What level of difficulty do you want to play? ").lower()
    players.append(HumanPlayer(player_name))
    players.append(ComputerPlayer('Computer1'))
    players.append(ComputerPlayer('Computer2'))
    
    game = Game(players, filepath)
    game.set_likelihood(difficulty)
    game.hide_spoons()
    
    game.play()
        
    
def parse_args(arglist):
    """Reads in filepath to json file of hiding spot information with hiding 
    room and hiding spot dictionaries
    
    Primary Author: Gosi
    """
    argpar = ArgumentParser()
    argpar.add_argument("filepath", help = """a filepath to json file of hiding
                        locations, should be two dictionaries named hiding_rooms
                        and hiding_spots""")
    return argpar.parse_args(arglist)
    
    
if __name__ == "__main__":
    args = parse_args(argv[1:])
    main(args.filepath)