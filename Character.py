from random import randint

class Character(object):
    def setWeapons(self, arms):
        self.weapon = arms

    def setArmor(self, armor):
        self.armor = armor
#=======================================================================================================================

class Weapon(object):
    def weapon(self):
        pass

class Unarmed(Weapon):
    def weapon(self):
        Hero.attackMod = 0
        print("INSERTNAME is unarmed!")

class BadWeapon(Weapon):
    def weapon(self):
        Hero.attackMod = 3
        print("INSERTNAME is equipped with a mediocre weapon...")

class AverageWeapon(Weapon):
    def weapon(self):
        Hero.attackMod = 4  + (Hero.level // 2)
        print("INSERTNAME is equipped with a decent weapon.")

class GoodWeapon(Weapon):
    def weapon(self):
        Hero.attackMod = 6  + (Hero.level // 2)
        print("INSERTNAME is equipped with a good weapon.")

class GreatWeapon(Weapon):
    def weapon(self):
        Hero.attackMod = 7  + (Hero.level // 2)
        print("INSERTNAME is equipped with a great weapon.")

class BestWeapon(Weapon):
    def weapon(self):
        Hero.attackMod = 9
        print("INSERTNAME is equipped with the finest weapons seen! A mighty warrior, indeed!")

#=======================================================================================================================

class Defenses(object):
    def armor(self):
        pass

class Defenseless(Defenses):
    def armor(self):
        self.defense = 10
        print("INSERTNAME is defenseless!")

class BadArmor(Defenses):
    def armor(self):
        self.defense = 13
        print("INSERTNAME is equipped with mediocre armor...")

class AverageArmor(Defenses):
    def armor(self):
        self.defense = 14
        print("INSERTNAME  is equipped with decent armor.")

class GoodArmor(Defenses):
    def armor(self):
        self.defense = 16
        print("INSERTNAME is equipped with good armor.")

class GreatArmor(Defenses):
    def armor(self):
        self.defense = 17
        print("INSERTNAME is equipped with great armor.")

class BestArmor(Defenses):
    def armor(self):
        self.defense = 19
        print("INSERTNAME is equipped with the finest armor in the land! A mighty warrior, indeed!")


#=======================================================================================================================

class Hero(Character):
    """
    The "Character" class shows a basic CIVILIAN or TRAINING DUMMY. If it is an advanced character (e.g. a hero), it will be given traits by the
    strategy pattern.
    """
    def __init__(self, name, level):
        self.weapon = Unarmed()
        self.armor = Defenseless()
        self.health = 20
        self.damageMod = 0
        self.name = name
        self.level = level
        self.defense = 10
        self.attackMod = 0

    def attack(self, target):
        if target.health <= 0:
            print(target.name + " is already unconscious! Move to the next target!")
            return
        attackRoll = randint(1,20) + self.attackMod
        if attackRoll >= target.defense:
            target.health -= (5 + self.damageMod)
            if target.health <= 0:
                print(target.name + " has fallen unconscious!")

#=======================================================================================================================

"""
Here is the driver for the program. I'm just creating some generic heroes right now, equipping them, then having one
hero rip a training dummy to shreds.
"""

def main():
    gardakan = Hero("Gardakan", 5)
    mordak = Hero("Mordak", 7)
    dummy = Hero("Training Dummy", 1)

    mordak.setArmor(BadArmor())
    mordak.setWeapons(GreatWeapon())
    gardakan.setArmor(GoodArmor())
    gardakan.setWeapons(BestWeapon())

    dummy.weapon.weapon()
    dummy.armor.armor()
    gardakan.weapon.weapon()
    gardakan.armor.armor()

    gardakan.attack(dummy)
    gardakan.attack(dummy)
    gardakan.attack(dummy)
    gardakan.attack(dummy)
    gardakan.attack(dummy)
    gardakan.attack(dummy)

main()

