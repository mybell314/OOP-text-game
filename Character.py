import random

class Character():
    #constructor
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    #describe the character
    def describe(self):
        print(self.name + " is here!")
        print(self.description)

    #set character conversation
    def set_conversation(self, conversation):
        self.conversation = conversation

    #talk to character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
    def bribe(self):
        result = random.randint(0,10)
        if result > 6:
            print("Yes, I will leave you alone")
            self.will_fight = False
            return True
        else:
            print("Your bribe was unsuccessful")
            return False
        
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        print(self.name + "'s weakness is " + self.weakness)
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False