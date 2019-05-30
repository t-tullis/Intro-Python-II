# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def movement(self, direction):
        if(direction == 'n'):
            if(self.current_room.n_to is not None):
                self.current_room = self.current_room.n_to
            else:
                print("There is no room in that direction")
        elif(direction == 's'):
            if(self.current_room.s_to is not None):
                self.current_room = self.current_room.s_to
            else:
                print("There is no room in that direction")
        elif(direction == 'e'):
            if(self.current_room.e_to is not None):
                self.current_room = self.current_room.e_to
            else:
                print("There is no room in that direction")
        elif(direction == 'w'):
            if(self.current_room.w_to is not None):
                self.current_room = self.current_room.w_to
            else:
                print("There is no room in that direction")

    def __str__(self):
        return f"Player: {self.name}\nCurrent Room: {self.current_room}"