class NPC:
    def __init__(self,name):
        self.name=name

    def greet(self):
        print(f"Hello player my name is {self.name}")

class BadAction:
    def action(self):
        print("Kill player")

class GoodAction:
    def action (self):
        print("Help player")


class GoodNPC(NPC,GoodAction):
    pass

class BadNPC(NPC,BadAction):
    pass

good_character=GoodNPC("Obi Wan")
good_character.greet()
good_character.action()
bad_character=BadNPC("Darth Vader")
bad_character.greet()
bad_character.action()