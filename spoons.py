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
    
    def __init__(self, name, is_cpu = False):
        """Create a player
        
        Args:
            name (str): name of the player
        
        Side effects:
            initialize the attributes"""
        self.name = name
        self.cards = []
        self.skill = None
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
        """Draws a card from the deck (random) and adding to player's hand
        
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
        
        
    # GAME STATE MANAGEMENT
    def check_four_of_a_kind(self):
        """Checks for four of a kind in a player's hand.
        
        Side effects:
            Once a player is confirmed to have four of a kind,
            they start checking for spoons.
        """
        ranks = [card.split(" ", 1)[1] for card in self.cards]
    
        for rank in ranks:
            if ranks.count(rank) == 4:
                self.mode = "spoons"
                print(f"{self.name} has 4 of a kind, and wins the game!")
                return True
        return False
    
    
    
    # def card_turn(self, game):
    #     if self.is_cpu:
    #         self.draw_card(game.card_deck)
    #     else:
    #         # human player
    #         pass
    
    
    # def take_turn(self, other, hiding_rooms):
    #     """Determines if a player is still trying for four of a kind,
    #     or searching for spoons.
    #     """
    #     if self.mode == "cards":
    #         self.self.swap_card(other)
    #         self.check_four_of_a_kind()
    #     elif self.mode == "spoons":
    #         self.search(hiding_rooms)
    
    
    # def spoon_turn(self, game):
    #     if self.is_cpu:
    #         self.cpu_search(game.hiding_rooms)
    #     else:
    #         self.search(game.hiding_rooms)
            
    #SEARCHING FOR SPOONS
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


    def set_skill(players, skills_list):
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
        
        available_skills = skills_list.copy()
        
        print("Available skills:")
        for i, skill in enumerate(skills_list):
            print(f"{i + 1}. {skill}")
            
        choice = int(input("Pick your skill: "))
        players[0].skill = skills_list[choice - 1]
        available_skills.remove(players[0].skill)
        
        for player in players[1:]:
            skill = random.choice(available_skills)
            player.skill = skill
            available_skills.remove(skill)
        
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
            print(f"The compass strongly points towards the {rooms_with_spoons}!")
            return rooms_with_spoons[0]
        else:
            print("The compass is spinning its pointer between two rooms!")
            print(f"It points to the following rooms: {rooms_with_spoons}")
            return rooms_with_spoons
    
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
    

class HumanPlayer(Player):
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
                del self.cards[card]
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
    
    
class ComputerPlayer(Player):

    def swap_card(self, other):
        """Allows the computer to decide what card to discard in Spoons.
        
        Parameters:
            other (Player/ComputerPlayer): other player 


        Side Effects:
            Removes the discarded card from cpu_hand
            Adds the discarded card to the next_player_pile
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
    """Class Representation of Game
    
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
        self.hiding_info = hiding_info
        self.hiding_spots = None
        self.hiding_rooms = None
        self.num_spoons = len(players) - 1
        
        self.json_to_dict()
        
    def json_to_dict(self):
        """Converts json file instance variable to relevant dictionaries.
        
        Techniques: 
        
        Side Effects: 
            Changes values of hiding_rooms and hiding_spots to the dictionaries
            in the json file
        """
        with open(self.hiding_info, 'r', encoding = 'utf-8') as reader:
            dict1 = dict(json.load(reader))
            self.hiding_rooms = dict(dict1['hiding_rooms'])
            self.hiding_spots = dict(dict1['hiding_spots'])
            
    def set_diffculty_level(self, difficulty):
        """Dictates how likely a spoon is to be in a hiding_spot based on chosen 
        difficulty. 
        
        Args:
            difficulty (str): value of 'easy', 'medium', or 'hard', that 
                dictates the range of likelihood between the hiding spots.
        
        Side effects: 
            Changes the likelihood value of hiding spots in the dictionary of 
                hiding rooms.
        
        Raises:
            ValueError: if provided a wrong difficulty level
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
                    return ValueError("Wrong Difficulty Level.")
    
                
    def hide_spoons(self):
        """Sets index two of of a hiding spot in the dictionary hiding rooms to 
        True if a spoon will be placed there. There will be number of 
        players - 1 spoons hidden in a given game most often. 
        
        Techniques Used: 
        
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

    def take_turn(self, player):
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
            return player.check_four_of_a_kind()
        elif player.mode == "spoons":
            return player.search(self.hiding_rooms)
        
            
    #running the turn system
    def play_card_round(self):
        """All players take their turns in the card game. If all players have
        found their 4 of a kind, no card round will take place.
        """
        
        
        for player in self.players:
            pass

    def play_search_round(self): 
        """Players who have found 4 of a kind, or are the last to find 4 of a 
        kind may search for spoons in the designated hiding spots.
        """

            for player in self.players:
                while(self.calc_spoons() > 0):
                    
        
    def calc_spoons(self):
        """Counts the remaining spoons. If no spoons are remaining, the game
        ends.
        """
        remaining_spoons = 0
        for value in self.hiding_rooms.values():
            for spot in value:
                if spot[2]:
                    remaining_spoons += 1
                if remaining_spoons >= self.num_spoons:
                    break
            if remaining_spoons >= self.num_spoons:
                    break
        return remaining_spoons
    
    def __str__(self):
        return(f"There is/are {self.calc_spoons()} spoon(s) left!")
        
    def __repr__(self):
        return(f"Here are the hiding spot details: {self.hiding_rooms}")
        
            
def main(filepath): 
    is_playing = True
    
    while is_playing:
        player_name = input("What is your name? ")
        human = Player(player_name)
        cpu1 = Player('cpu1', True)
        cpu2 = Player('cpu2', True)
        
        game_state = Game([human, cpu1, cpu2], filepath)
        game_state.set_hiding_spot('hard')
        game_state.hide_spoons()
        
        
        print(game_state)

        keep_playing = input("Would you like to play again? Y/N: ")
        is_playing = True if keep_playing == 'Y' else False
        
    
def parse_args(arglist):
    """Reads in filepath to json file of hiding spot information with hiding 
    room and hiding spot dictionaries"""
    argpar = ArgumentParser()
    argpar.add_argument("filepath", help = """a filepath to json file of hiding
                        locations, should be two dictionaries named hiding_rooms
                        and hiding_spots""")
    return argpar.parse_args(arglist)
    
    
if __name__ == "__main__":
    args = parse_args(argv[1:])
    main(args.filepath)