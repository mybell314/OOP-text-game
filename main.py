from Room import Room
from Character import Character, Enemy

commands = ["north", "south", "east", "west", "talk", "fight", "bribe", "help"]

if __name__ == "__main__":
    #rooms
    kitchen = Room("kitchen")
    kitchen.setDescription("A dank and dirty room buzzing with flies")

    diningHall = Room("Dining Hall")
    diningHall.setDescription("A large room with ornate golden decorations on every wall")

    ballRoom = Room("Ball Room")
    ballRoom.setDescription("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance")

    kitchen.link_room(diningHall, "south")
    diningHall.link_room(kitchen, "north")
    diningHall.link_room(ballRoom, "west")
    ballRoom.link_room(diningHall, "east")

    bedRoom = Room("bedroom")
    bedRoom.setDescription("A medium sized room with a large bed in the centre")
    bedRoom.link_room(ballRoom, "north")
    #bedRoom.getDescription()

    #characters
    dave = Enemy("Dave", "A smelly zombie")
    dave.describe()
    dave.set_conversation("let me eat your brain dude")
    #dave.talk()
    dave.set_weakness("work")

    diningHall.setCharacter(dave)

    leo = Character("Leo", "the main character")
    leo.set_conversation("kill dave")

    bob = Character("bob", "second character")
    bob.set_conversation("we should kill dave")

    kitchen.setCharacter(leo)
    kitchen.setCharacter(bob)

    #main game loop
    current_room = kitchen
    while True:
        print("\n")
        current_room.getDetails()

        ncp = current_room.getCharacter()
        if ncp is not None:
            ncp.describe()

        command = input("> ").lower()
        if command in ["north", "south", "east", "west"]:
            current_room = current_room.move(command)
        elif command == "talk":
            if ncp is not None:
                ncp.talk()
            else:
                print("There is nobody here to talk to")
        elif command == "fight":
            if ncp is not None:
                weapon = input("Pick your weapon")
                result = ncp.fight(weapon)
                if result == False:
                    print("Sorry, you were killed")
                    break
                else:
                    print("You beat", ncp.get_name())
                    current_room.remove_character()
            else:
                print("There is nobody here")
        elif command == "bribe":
            if ncp is not None:
                success = ncp.bribe
                if success == True:
                    print("Success, you managed to bribe", ncp.get_name())
                else:
                    print("You failed to bribe", ncp.get_name())
            else:
                print("There is nobody here to bribe")
        else:
            print("You have entered an invalid command")
            print("These are the commands you can use:")
            for c in commands:
                print(c)

