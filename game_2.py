class Street:
    """Class for street representation"""
    def __init__(self, name):
        self.name = name
        self.description = ""
        self.link_streets = {}
        self.lst_characters = []
        self.lst_items = []

    def set_description(self, description):
        """
        (Room, str) -> NoneType
        Creates a description of a street
        """
        self.description = description

    def link_street(self, linked_room, side):
        """
        (Room, dict, str) -> NoneType
        Fills in the dictionary with linked streets as keys and sides as values
        """
        self.link_streets[side] = linked_room

    def set_character(self, character):
        """
        (Room, str) -> NoneType
        Fills in the list of characters in the street
        """
        self.lst_characters = [character]

    def set_item(self, item):
        """
        (Room, str) -> NoneType
        Fills in the list of items in the street
        """
        if item is not None:
            self.lst_items = [item]

    def get_details(self):
        """
        (Room) -> str
        Prints a string where are next streets
        """
        print(self.name + "\n" + "-" * 20 + "\n" + self.description)
        for side in self.link_streets:
            print(str(self.link_streets[side]) + " є на " + str(side))

    def get_character(self):
        """
        (Room) -> str
        Returns one character from the list of characters in the street
        """
        if len(self.lst_characters) == 0:
            return None
        else:
            for character in self.lst_characters:
                return character

    def get_item(self):
        """
        (Room) -> str
        Returns one item from the list of items in the street
        """
        if len(self.lst_items) == 0:
            return None
        else:
            for i in self.lst_items:
                return i

    def move(self, side):
        """
        (Room, str) -> str
        Returns the next street
        """
        if side in self.link_streets:
            return self.link_streets[side]

    def __str__(self):
        return self.name


class Enemy:
    """Class for enemy representation"""
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.conversation = ""
        self.weaknesses = []
        self.killed_enemies = 0
        self.dead = False

    def set_conversation(self, conversation):
        """
        (Enemy, str) -> NoneType
        Creates conversation with an enemy
        """
        self.conversation = conversation

    def set_weakness(self, weakness):
        """
        (Enemy, str) -> NoneType
        Fills in the list of weaknesses of enemy
        """
        self.weaknesses = [weakness]

    def describe(self):
        """
        (Enemy) -> str
        Prints the information about an enemy which is on the street
        """
        print(self.name, "тут!" + "\n" + self.race)

    def talk(self):
        """
        (Enemy) -> NoneType
        Prints what the enemy says
        """
        print("[" + self.name + " каже ]: " + self.conversation)

    def fight(self, fight_with):
        """
        (Enemy, str) -> bool
        Returns True if the item beats an enemy and False if not
        """
        if fight_with in self.weaknesses:
            self.killed_enemies += 1
            return True
        return False

    def get_defeated(self):
        """
        (Enemy) -> int
        Returns number of killed enemies
        """
        return self.killed_enemies

    def __str__(self):
        return self.name


class Item:
    """Class for item representation"""
    def __init__(self, name):
        self.name = name
        self.description = ""

    def set_description(self, description):
        """
        (Item, str) -> NoneType
        Creates a description of an item
        """
        self.description = description

    def describe(self):
        """
        (Item) -> str
        Prints a description of an item
        """
        print("[" + self.name + "] тут - " + self.description)

    def get_name(self):
        """
        (Item) -> str
        Returns the name of an item
        """
        return self.name

    def __str__(self):
        return self.name
