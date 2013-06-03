from ObserverPattern import *
from random import randint

class Monster (Observable):
    def __init__(self, name, level, faction = "FFA"):
        Observable.__init__(self)
        self.name = name # character name
        self.level = level # character level
        self.faction = faction # for large scale battles later down the road, I want to implement factions as a way of telling friend from foe
        self.initiative = randint(1, 20) + (self.level // 2)
        self.atkMod = 10
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
        atkRoll = self.atkMod.attackRoll()
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