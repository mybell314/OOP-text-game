class Room():
    #constructor
    def __init__(self, room_name):
        self.name = room_name
        self.description = None #None makes it optional
        self.linked_rooms = {}
        self.character = None

    #setter - sets room description
    def setDescription(self, description):
        self.description = description

    def setCharacter(self, character):
        self.character = character

    #getter - gets room description
    def getDescription(self):
        return self.description
    
    def getName(self):
        return self.name
    
    def getDetails(self):
        print("You are in the " + self.getName())
        print("It is " + self.getDescription())
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.getName() + " is to the " + direction)

    def getCharacter(self):
        return self.character

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("you can't go that way")
            return self