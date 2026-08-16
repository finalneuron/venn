"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""

from evennia.objects.objects import DefaultCharacter

from .objects import ObjectParent


class Character(ObjectParent, DefaultCharacter):
    """
    The Character just re-implements some of the Object's methods and hooks
    to represent a Character entity in-game.

    See mygame/typeclasses/objects.py for a list of
    properties and methods available on all Object child classes like this.

    """

    def at_object_creation(self):
        """
        Called only once, when the character is first created.
        ###TUTORIAL
        """
        # Persistent attributes (saved to the database)
        self.db.strength = 5
        self.db.agility = 4
        self.db.magic = 2
        self.db.level = 1
        self.db.desc = "A normal adventurer."

    pass
