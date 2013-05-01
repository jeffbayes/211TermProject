from Weapon import *
from Defenses import *
from ObserverPattern import *

#=======================================================================================================================
# Character and Hero Category #

class Character(object):
    def setWeapons(self, arms):
        self.weapon = arms

    def setArmor(self, armor):
        self.armor = armor

    def announce(self, name):
        print(name + " is " + self.weapon.display() + " and " + self.armor.display() + ".")

class Hero(Character, Observable):
    """
    The "Hero" class shows a basic CIVILIAN or TRAINING DUMMY. If it is an advanced character (e.g. a hero), it will be given traits by the
    strategy pattern. More classes will be added as I define distances, starting points, etc.
    """
    global MAX_BASE_HEALTH
    MAX_BASE_HEALTH = 20
    def __init__(self, name, level, faction = "FFA"):
        Observable.__init__(self)
        self.name = name # character name
        self.level = level # character level
        self.faction = faction # for large scale battles later down the road, I want to implement factions as a way of telling friend from foe
        self.initiative = randint(1, 20) + (self.level // 2)
        self.weapon = Unarmed() #attack mod of 0 and damage mod of 0 - basic civilian.
        self.armor = Defenseless() #defenses of 10. simple town clothing.
        self.health = (MAX_BASE_HEALTH + self.level) # 20 + your level
        self.maxhealth = (MAX_BASE_HEALTH + self.level) # 20 + your level
        self.defenses = self.armor.armor() + (self.level // 2) + 10 # armor stats + 1/2 level + base 10

    def getHealth(self):
        return self.health

    def attack(self, target):
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
    #dummy = Hero("Training Dummy", 1, "Blue")
    #dummy.health = 150


    # set the weapons and armors of my heroes
    mordak.setArmor(BestArmor())
    mordak.setWeapons(BadWeapon())
    gardakan.setArmor(BestArmor())
    gardakan.setWeapons(BadWeapon())

    ### ======================================================= ###
    # this disgustingly long chunk of code is to sort my heroes by their initiative roll.
    characters.append(gardakan)
    characters.append(mordak)
    #characters.append(dummy)

    for hero in characters:
        inits.append(hero.initiative)
    inits.sort(reverse = True)
    for hero in characters:
        health = HealthObserver(hero)
        for num in inits:
            if hero.initiative == num:
                heroes.append(hero)
    ### ======================================================= ###

    for hero in heroes:
        hero.announce(hero.name)
    print("!!!!! FIGHT !!!!!")
    while gardakan.health > 0 and mordak.health > 0:
        for hero in heroes:
            if gardakan.health > 0 and mordak.health > 0:
                hero.attack(gardakan)
                if gardakan.health > 0 and mordak.health > 0:
                    hero.attack(mordak)


main()