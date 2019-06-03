from room import Room
from player import Player
from colors import Color
from item import Item
from add_items import add_room_items
import os
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", add_room_items()), 

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", add_room_items()),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", add_room_items()),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", add_room_items()),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", add_room_items()),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

player_name = input("Hey newcomer what is your name? ")
os.system('clear')

player = Player(player_name, room['outside'])
print()
#Colors for game
purple = Color().PURPLE
cyan = Color().CYAN
bold = Color().BOLD
red = Color().RED
yellow = Color().YELLOW
green = Color().GREEN
blue= Color().BLUE
darkcyan = Color().DARKCYAN
end = Color().END


print(f"Hello,{cyan}{player_name}{end} are you ready to go on an adventure?")
while True:
    print(purple + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + end)
    print(f"{bold}Current Room{end}: {red}{bold}{player.current_room.name}{end}")
    for d in textwrap.wrap(player.current_room.description, width=40):
        print(d)
    
    for item in player.current_room.items:
        print(f"Items in Room : [{item.name}]")
    
    for item in player.inventory:
        print(f"Inventory: [{item.name}]")
    
    print(f"{red}[q] - Quit {end}\n{yellow}[n] - Move North{end}\n{green}[s] - Move South{end}\n{blue}[e] - Move East{end}\n{darkcyan}[w] - Move West{end}")
    print(purple + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + end)
    
    command = input("Enter command: ").lower()
    os.system('clear')

    if(command == 'q'):
        print("Thanks for playing!")
        break
    elif(command == 'grab'):
        player_choice = input("Do you want to grab this item? ")
        if(player_choice == 'yes'):
            item = player.current_room.items.pop()
            player.inventory.append(item)

            for item in player.inventory:
                print(f"Inventory: [{item.name}]")

    elif(command == 'n' or command == 's' or command == 'e' or command == 'w'):
        player.movement(command)
    else:
        print("Error: Invalid move please enter a valid move\n [q] Quit\n [n] Move North\n [s] Move South\n [e] Move East\n [w] Move West")
