from item import  Item
import random

items = [
    Item("Rock", "A small rock."),
    Item("Stick", "A large stick."),
    Item("Jewlery box", "A collection of necklaces."),
    Item("Pen", "A pen."),
    Item("Sword", "a small sword."),
    ]
    
def add_room_items(): 
    items_in_room = []
    for num in range(1, 4):
        random_int = random.randint(0, 3)
        if(random_int >= num):
            items_in_room.append(items[random.randint(0, len(items) - 1)])
        return items_in_room

