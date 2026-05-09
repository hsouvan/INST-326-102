# python file for the game
import random
import json
from argparse import ArgumentParser
from sys import argv

class Player:
    """Abstract Representation of Player
    
    Attributes:
        name (str): name of the player
        cards (list): player's current card deck
        mode (str): current mode of the player, default is "cards"
    """
    def __init__(self, name):
        """Create a player
        
        Args:
            name (str): name of the player
        
        Side effects:
            initialize the attributes
        """
        self.name = name
        self.cards = []
        self.mode = "cards"
    
    def dealing(self, card_deck):
        """Deal the cards for each player
        
        Args:
            card_deck (list): pile of cards from the Game class
        
        Side effects:
            add cards into players's card deck
            remove card from the card_deck
            print player's current card deck
        
        Techniques demonstrated:
            f-strings containing expressions
        """
        self.cards = random.sample(card_deck, 4)
        for card in self.cards:
            card_deck.remove(card)
        print(f"{self.name}'s card deck: {self.cards}")
    
    def draw_card(self, card_deck):
        """Draw a card from card_deck randomly and add to player's card deck
        
        Args:
            card_deck (list): pile of cards from the Game class
            
        Side effects:
            add a card into player's card deck
            remove card from card_deck
        """
        card = random.choice(card_deck)
        self.cards.append(card)
        card_deck.remove(card)
    
    def trash_pile(self, card_deck):
        """Allow player to discard one of their card to card_deck 
        (abstract method)
        
        Args:
            card_deck (list): pile of cards from the Game class
        """
        raise NotImplementedError  
        
    def swap_card (self, other):
        """Allow player to discard one of their card to the next player 
        (abstract method)
        
        Args: 
            other (Player): the next player
        
        Techniques demonstrated:
            abstract methods
        """
        raise NotImplementedError
        
    def check_four_of_a_kind(self):
        """Checks if a player has four of a kind.
        
        Side effects:
            change the mode attribute to "spoons" if they have four of a kind
            print the message the player have four of a kind and can start
                searching for the spoons
        
        Techniques demonstrated:
            list comprehension
        """
        ranks = [card[:-1] for card in self.cards]

        for rank in ranks:
            if ranks.count(rank) == 4:
                self.mode = "spoons"
        if self.mode == "spoons":
            print(f"{self.name} has 4 of a kind! They can now search for the " 
                      "spoon!")

    def search(self, hiding_rooms):
        """Allow player to search for the spoon (abstract method)
        
        Args:
            hiding_rooms (dict): hiding rooms which each have lists of hiding
                spots
        """
        raise NotImplementedError
    
    def set_skill(self, skills_list):
        """Give player a skill (abstract method)
        
        Args:
            skills_list (list): list of premade skills
        """
        pass


class HumanPlayer(Player):
    """Representation of Human Player
    
    Attributes:
        skill (str) = name of the skill that the player chose
    """
    def __init__(self, name):
        """Create a player
        
        Args:
            name (str): name of the player
        
        Side effects:
            initialize the parent class and subclass attributes
        """
        self.name = name
        self.cards = []
        self.skill = None
        self.mode = "cards"
    
    def swap_card (self, other):
        """Allow player to discard one of their card to the next player
        
        Args: 
            other (Player): the next player
        
        Side effects:
            print player's current card deck
            ask player what card to discard to the next player
            delete the card from player’s card deck
            add the card to the next player’s card deck
        """
        print(f"{self.name}'s current card deck: {self.cards}")
        chosen_card = input("What card do you want to discard to the next "
                            "player?\n").upper()
        self.cards.remove(chosen_card)
        other.cards.append(chosen_card)
        
    def trash_pile(self, card_deck):
        """Allow player to discard one of their card to card_deck 
        (Note: it is similar to swap_card)
        
        Args:
            card_deck (list): pile of cards from the Game class
        
        Side effects:
            print player's current card deck
            ask player what card to discard to card_deck
            delete the card from player’s card deck
            add the card back to card_deck
        """
        print(f"{self.name}'s current card deck: {self.cards}")
        chosen_card = input("What card do you want to discard to the next "
                            "player?\n").upper()
        self.cards.remove(chosen_card)
        card_deck.append(chosen_card)
    
    def search(self, hiding_rooms):
        """Allow player to search for the spoon
        
        Args:
            hiding_rooms (dict): hiding rooms which each have lists of hiding
                spots
        
        Returns:
            bool: True or False depending on whether there is a spoon hidden in 
                that hiding spot
            
        Side effects: 
            ask user for which room and hiding spot to search
            print result of the search, including invalid searches
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

    def check_spot(self, hiding_rooms, room, hiding_spot):
        """Search for the spoon, specifically the hiding spot
        
        Args:
            hiding_rooms (dict): hiding rooms which each have lists of hiding
                spots
            room (str): room of the hiding spot
            hiding_spot (str): hiding spot that is selected
        
        Returns:
            bool: True or False depending on whether there is a spoon hidden in 
                that hiding spot
        
        Side effects: 
            print result of the search, including invalid searches
        
        Techniques demonstrated:
            helper methods
        """
        for spot in hiding_rooms[room]:
            if spot[0] == hiding_spot:
                if spot[2]:
                    print(f"A spoon has been found! {self.name} WINS!!!")
                    return True
                else:
                    print("No spoon found.")
                    return False         
        print("Invalid hiding spot.")
        return False

    def set_skill(self, skills_list):
        """Lets the player choose a skill.
        
        Args:
            skills_list (list): list of premade skills
            
        Side effects:
            prints all available skills
            asks what skill the player wants to choose
            set skill attribute to the chosen skill
            remove the chosen skill from skills_list
        
        Techniques demonstrated:
            list removal
        """
        print("Available skills:")
        for i, skill in enumerate(skills_list):
            print(f"{i + 1}. {skill}")
            
        self.skill = input("Pick your skill (enter the name): ").lower()
        skills_list.remove(self.skill)
        
    #SKILLS RELATED TO SEARCHING FOR SPOONS
    def spoon_compass(self, hiding_rooms):
        """Point to the room(s) where the spoon(s) is hiding in
        
        Args:
            hiding_rooms (dict): hiding rooms which each have lists of hiding
                spots
        
        Side effects:
            print the statement of the room(s) the compass is pointing to
        
        Techniques demonstrated:
            nested iteration
        """
        rooms_with_spoons = []
        
        for room in hiding_rooms:
            for spot in hiding_rooms[room]:
                if spot[2]:
                    rooms_with_spoons.append(room)
        
        rooms_with_spoons = list(set(rooms_with_spoons))
        
        if len(rooms_with_spoons) == 1:
            print(f"The compass strongly points towards the {rooms_with_spoons}"
                    "!")
        else:
            print("The compass is spinning its pointer between two rooms!")
            print(f"It points to the following rooms: {rooms_with_spoons}")
    
    def oh_shiny(self, hiding_rooms):
        """Tell the player if the selected room have spoons or not, and if the 
        room have spoons, player get a free chance to pick a hiding spot to
        search
        
        Args:
            hiding_rooms (dict): hiding rooms which each have lists of hiding
                spots
        
        Returns:
            bool: True or False depending on whether there is a spoon hidden in 
                that hiding spot
        
        Side effects: 
            ask user for which room and hiding spot to search
            print result of the search, including invalid searches
        
        Techniques demonstrated:
            helper method reuse, user input validations 
        """
        room = input("Pick a room to scan:\n").lower()
        
        if room not in hiding_rooms:
            print("Invalid room")
            return False
        
        spoon_found = any(spot[2] for spot in hiding_rooms[room])
        
        if not spoon_found:
            print(f"The room has no spoons in the {room}")
            return False
        
        print(f"Your scan revealed a spoon in the {room}!")
        
        print("Now you can search for a spot the spoon might be in:")
        for spot in hiding_rooms[room]:
            print(spot[0])
        
        selected_spot = input("Which spot do you select?\n").lower()
        return self.check_spot(hiding_rooms, room, selected_spot)
    
    
class ComputerPlayer(Player):
    """Representation of Human Player
    """
    def swap_card(self, other):
        """Allow player to discard one of their card to the next player
        
        Argss:
            other (Player): the next player 


        Side effects:
            print player's current card deck after discarding it
            delete the card from player’s card deck
            add the card to the next player’s card deck
        """
        ranks = [card[:-1] for card in self.cards]
        card_to_discard = None
        
        for card in self.cards:
            if ranks.count(card[:-1]) < 2:
                card_to_discard = card
                break
        
        if card_to_discard == None:
            card_to_discard = self.cards[0]
        
        self.cards.remove(card_to_discard)
        other.cards.append(card_to_discard)
        print(f"{self.name}'s current card deck: {self.cards}")
    
    def trash_pile(self, card_deck):
        """Allow player to discard one of their card to card_deck 
        (Note: it is similar to swap_card)
        
        Args:
            card_deck (list): pile of cards from the Game class
        
        Side effects:
            print player's current card deck after discarding it
            delete the card from player’s card deck
            add the card back to card_deck
        """
        ranks = [card[:-1] for card in self.cards]
        card_to_discard = None
        
        for card in self.cards:
            if ranks.count(card[:-1]) < 2:
                card_to_discard = card
                break
        
        if card_to_discard == None:
            card_to_discard = self.cards[0]
        
        self.cards.remove(card_to_discard)
        card_deck.append(card_to_discard)
        print(f"{self.name}'s current card deck: {self.cards}")
    
    def search(self, hiding_rooms):
        """Allow player to search for the spoon
        
        Args:
            hiding_rooms (dict): hiding rooms which each have lists of hiding
                spots
        
        Returns:
            bool: True or False depending on whether there is a spoon hidden in 
                that hiding spot
        
        Side effects: 
            print result of the search, including invalid searches
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
    """Representation of Spoons Game
    
    Attributes:
        hiding_rooms (dict): collection of hiding spots (list of tuples)
            where the spoons may be hidden, containing the name of the 
            hiding spot and its likelihood value, rooms do not have 
            likelihoods. All hiding spots musthave unique names.
        hiding_spots (dict): The keys are all possible hiding spots, and the 
            values are the rooms in which they are located
        players (list): a list of Player objects, the human player will always
            be the first item in the list, followed by two computers
        num_spoons (int): number of spoons to be found, usually one less than 
            the number of players
        skills_list (list): list of premade skills
    """ 
    def __init__(self, players, hiding_info):
        """Description
        
        Args:
            players (list): a list of players
            hiding_info (str): name of the json file in which the hiding spot 
                and hiding room dictionaries are located
        
        Side effects:
            initialize the attributes
        """
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
        
        Args:
            hiding_info (str): name of the json file in which the hiding spot 
                and hiding room dictionaries are located
        
        Side effects: 
            changes values of hiding_rooms and hiding_spots to the dictionaries
                in the json file
        
        Techinques demonstrated:
            use of json.load(), with statements
        """
        with open(hiding_info, 'r', encoding = 'utf-8') as reader:
            dict1 = dict(json.load(reader))
            self.hiding_rooms = dict(dict1['hiding_rooms'])
            self.hiding_spots = dict(dict1['hiding_spots'])
            
    def set_likelihood(self, difficulty):
        """Indicate how likely a spoon is to be in a hiding_spot based on chosen 
        difficulty level
        
        Args:
            difficulty (str): value of 'easy', 'medium', or 'hard', that 
                dictates the range of likelihood between the hiding spots
        
        Side effects: 
            changes the likelihood value of hiding spots in the dictionary of 
                hiding rooms
        
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
        
        Side Effects: 
            changes the value of hiding_spot[2] to true if a spoon is hidden 
                there
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
        or searching for spoons
        
        Args:
            player (Player): the player
        
        Returns:
            bool: True or False depending on whether the player has found a 
                spoon
        
        Side effects:
            ask human player if they want to use their skill during their search
                turn
        
        Techniques demonstrated:
            conditional statement
        """
        player_index = self.players.index(player)
        if player.mode == "cards":
            if player_index == 0:
                player.draw_card(self.card_deck)
                other = self.players[self.players.index(player) + 1]
                player.swap_card(other)
            elif (player_index + 1) == len(self.players):
                player.trash_pile(self.card_deck)
            else:
                other = self.players[self.players.index(player) + 1]
                player.swap_card(other)
            player.check_four_of_a_kind()
            return False
        elif player.mode == "spoons":
            if isinstance(player, HumanPlayer):
                skill_use = input("Do you want to use your skill? (y/n) ")
                if skill_use.lower() == "y":
                    if player.skill == "spoon compass":
                        player.spoon_compass(self.hiding_rooms)
                        return False
                    elif player.skill == "oh shiny":
                        return player.oh_shiny(self.hiding_rooms)
                else:
                    return player.search(self.hiding_rooms)
            else:    
                return player.search(self.hiding_rooms)   
    
    def play(self):
        """Play the Game
        
        Side effects:
            print a message that the game ended
        
        Techniques demonstrated:
            while statement
        """
        win = False
        for player in self.players:
            player.set_skill(self.skills_list)
            player.dealing(self.card_deck)
        turn = -1
        self.players[0].draw_card(self.card_deck)
        while not win:
            turn += 1
            player = self.players[turn % len(self.players)]
            win = self.turn(player)
        print("Game End!")           


def main(filepath):
    """Set up and run the game

    Args:
        filepath (str): name of the json file in which the hiding spot 
            and hiding room dictionaries are located
    
    Side effects:
        ask the player's name and difficulty level
    """
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
    """Parse command-line arguments
    
    Args:
        arglist (list of str): arguments from the command line
    
    Returns:
        namespace: the parsed arguments, as a namespace
    
    Techinques demonstrated:
        ArgumentParser class
    """
    argpar = ArgumentParser()
    argpar.add_argument("filepath", help="a filepath to json file of hiding "
                        "locations, should be two dictionaries named "
                        "hiding_rooms and hiding_spots")
    return argpar.parse_args(arglist)
    
if __name__ == "__main__":
    args = parse_args(argv[1:])
    main(args.filepath)
    
    