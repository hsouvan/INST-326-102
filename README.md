# Game Project: Spoons Card Game


# File Breakdown #

The .json file _hiding_location_info_default.json_ is an example of the json the user would provide, complete with the rooms and hiding spots in which spoons can be hidden. This file is accessed in our code to get the dictionaries with the json file. This file is also inputted throw the terminal.

The _mainfunc_ file is where we run our main function where we create and use the classes the have all the Game and Player functionality. 

The _spoons.py_ file is where we create our Game and Player classes that allow us to run the Game. The Player class focuses on player abilities like taking turns and searching for spoons, while the Game sets up the more overarching aspects like hiding the spoons and fixing the setting of the game.



| **Method/function**  | **Primary Author** | **Techniques Demonstrated** |
|------------------|-----------------|-------------------------|
| set_likelihood() | Gosi Alilonu    |                         |
| hide_spoons()    | Gosi Alilonu    |                         |
| calc_spoons()    | Gosi Alilonu    |                         |
| json_to_dict()   | Gosi Alilonu    | json.load(), with()     |
| __str__()        |                 |                         |
| __repr__()       |                 |                         |
| main()           |                 |                         |
| check_four_of_a_kind() | Andrew Nicolosi | list comprehension |
| search()         | Andrew Nicolosi |                         |
| check_spot()     | Andrew Nicolosi | helper methods, conditional statement |
| set_skill()      | Andrew Nicolosi | list removal            |
| spoon_compass()  | Andrew Nicolosi | nested iteration        |
| oh_shiny()       | Andrew Nicolosi | helper method reuse     |



Works Cited

W3schools.com. W3Schools Online Web Tutorials. (n.d.). https://www.w3schools.com/js/js_json_syntax.asp.


Card Number:
|       **Heart**     |     **Diamond**       |     **Club**       |      **Spade**      |
|---------------------|-----------------------|--------------------|---------------------|
| AH - Ace of Heart   | AD - Ace of Diamond   | AC - Ace of Club   | AS - Ace of Spade   |
| 2H - 2 of Heart     | 2D - 2 of Diamond     | 2C - 2 of Club     | 2S - 2 of Spade     |
| 3H - 3 of Heart     | 3D - 3 of Diamond     | 3C - 3 of Club     | 3S - 3 of Spade     |
| 4H - 4 of Heart     | 4D - 4 of Diamond     | 4C - 4 of Club     | 4S - 4 of Spade     |
| 5H - 5 of Heart     | 5D - 5 of Diamond     | 5C - 5 of Club     | 5S - 5 of Spade     |
| 6H - 6 of Heart     | 6D - 6 of Diamond     | 6C - 6 of Club     | 6S - 6 of Spade     |
| 7H - 7 of Heart     | 7D - 7 of Diamond     | 7C - 7 of Club     | 7S - 7 of Spade     |
| 8H - 8 of Heart     | 8D - 8 of Diamond     | 8C - 8 of Club     | 8S - 8 of Spade     |
| 9H - 9 of Heart     | 9D - 9 of Diamond     | 9C - 9 of Club     | 9S - 9 of Spade     |
| 10H - 10 of Heart   | 10D - 10 of Diamond   | 10C - 10 of Club   | 10S - 10 of Spade   |
| JH - Joker of Heart | JD - Joker of Diamond | JC - Joker of Club | JS - Joker of Spade |
| QH - Queen of Heart | QD - Queen of Diamond | QC - Queen of Club | QS - Queen of Spade |
| KH - King of Heart  | KD - King of Diamond  | KC - King of Club  | KS - King of Spade  |
