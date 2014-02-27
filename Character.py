from Weapon import *
from Defenses import *
from ObserverPattern import *
from StatePattern import *
from Decoration import *


#=======================================================================================================================
# Character and Hero Category #

class Character(Observable, TurnBased):
    global MAX_BASE_HEALTH
    MAX_BASE_HEALTH = 20
    def __init__(self):
        Observable.__init__(self)
        self.initiative = randint(1, 20) + (self.level // 2)
        self.weapon = Unarmed() #attack mod of 0 and damage mod of 0 - basic civilian.
        self.armor = Defenseless() #defenses of 10. simple town clothing.
        self.health = (MAX_BASE_HEALTH + self.level) # 20 + your level
        self.maxhealth = (MAX_BASE_HEALTH + self.level) # 20 + your level
        self.defenses = self.armor.armor() + (self.level // 2) + 10 # armor stats + 1/2 level + base 10

    def getHealth(self):
        return self.health

    def setWeapons(self, arms):
        self.weapon = arms

    def setArmor(self, armor):
        self.armor = armor

    def announce(self, name):
        print(name + " is " + self.weapon.display() + " and " + self.armor.display() + ".")

class Hero(Character, ArmorColor):
    """
    The "Hero" class shows a basic CIVILIAN or TRAINING DUMMY. If it is an advanced character (e.g. a hero), it will be given traits by the
    strategy pattern. More classes will be added as I define distances, starting points, etc.
    """
    def __init__(self, name, level, faction = "FFA"):
        self.name = name # character name
        self.level = level # character level
        self.faction = faction # for large scale battles later down the road, I want to implement factions as a way of telling friend from foe
        Character.__init__(self)
        TurnBased.__init__(self)

    def attack(self, target):
        d = Debuffer()
        self.currentState.action(self, target)
        self.acceptVisitor(d)