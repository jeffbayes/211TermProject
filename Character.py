from Weapon import *
from Defenses import *
from ObserverPattern import *
from StatePattern import *

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

class Hero(Character):
    """
    The "Hero" class shows a basic CIVILIAN or TRAINING DUMMY. If it is an advanced character (e.g. a hero), it will be given traits by the
    strategy pattern. More classes will be added as I define distances, starting points, etc.
    """
    # what if I put a while loop in the main() function, where the state pattern will hand the turn off to the next person.
    def __init__(self, name, level, faction = "FFA"):
        self.name = name # character name
        self.level = level # character level
        self.faction = faction # for large scale battles later down the road, I want to implement factions as a way of telling friend from foe
        Character.__init__(self)
        TurnBased.__init__(self)

    def attack(self, target):
        b = Buffer()
        d = Debuffer()
        if self.currentState == self.notMyTurn or self.health <= 0:
            return
        if self.faction != "FFA":
            if target.faction == self.faction:
                return
        if self.name == target.name or target.health <= 0:
            return

        notBloody = None
        if target.health > (target.maxhealth / 2):
            notBloody = True
        atkRoll = self.weapon.attackRoll()
        dmgRoll = self.weapon.damageRoll()
        if atkRoll >= target.defenses:
            target.health -= dmgRoll
            print(self.name + " strikes " + target.name + ", dealing " + str(dmgRoll) + " damage.")
            if target.health <= 0:
                print(target.name + " has fallen unconscious!")
                return
            if notBloody == True and target.health < (target.maxhealth / 2):
                target.notifyObservers()
        else:
            print(self.name + " cannot penetrate " + target.name + "'s defenses.")
        self.acceptVisitor(d)



#=======================================================================================================================

def main():
    """
    Here is the driver for the program. I'm just creating some generic heroes right now, equipping them, then having one
    hero rip a training dummy to shreds.
    """
    characters = []
    inits = []
    heroes = []



    gardakan = Hero("Gardakan", 5, "Red")
    mordak = Hero("Mordak", 7, "Blue") #Mordak and the dummy are on the same faction, so they cannot attack one another.
    dummy = Hero("Training Dummy", 1, "Blue")
    a = Hero("Anakin", 6, "Red")
    b = Hero("Balthazar", 19, "Blue")
    c = Hero("Cantar", 17, "Red")

    dummy.health = 150


    # set the weapons and armors of my heroes
    mordak.setArmor(BestArmor())
    mordak.setWeapons(BadWeapon())
    gardakan.setArmor(BestArmor())
    gardakan.setWeapons(BadWeapon())

    ### ======================================================= ###
    # this disgustingly long chunk of code is to sort my heroes by their initiative roll.
    characters.append(gardakan)
    characters.append(mordak)
    characters.append(dummy)
    characters.append(a)
    characters.append(b)
    characters.append(c)
    blueTeam = []
    redTeam = []

    for hero in characters:
        #don't really care about initiatives right now. I can deal with this later if necessary.
        """inits.append(hero.initiative)
    inits.sort(reverse = True)
    for hero in characters:
        health = HealthObserver(hero)
        for num in inits:
            if hero.initiative == num:
                heroes.append(hero)"""
        if hero.faction == "Blue":
            blueTeam.append(hero)
        if hero.faction == "Red":
            redTeam.append(hero)
    ### ======================================================= ###

    for hero in heroes:
        hero.announce(hero.name)
    print("!!!!! FIGHT !!!!!")
    while redTeam != [] and blueTeam != []:
        for blues in blueTeam:
            for reds in redTeam:
                reds.attack(blues)
                if blues.health <= 0:
                    blueTeam.remove(blues)
                    for blues in blueTeam:
                        print(blues.name + " fights on for the Blue team.")
        for reds in redTeam:
            for blues in blueTeam:
                blues.attack(reds)
                if reds.health <= 0:
                    redTeam.remove(reds)
                    for reds in redTeam:
                        print(reds.name + " fights on for the Red team.")
        for hero in characters:
            hero.myTurnNow()

    if redTeam == []:
        print("Blue team is victorious!")
    else:
        print("Red team is victorious!")




main()