from random import randint
#=======================================================================================================================
# Weapons Category #

class Weapon(object):
    def __init__(self):
        pass
    def display(self):
        pass
    def attackRoll(self):
        pass
    def damageRoll(self):
        pass

class Unarmed(Weapon):
    def __init__(self):
        self.atkMod = 0
        self.dmgMod = 0
    def display(self):
        return "unarmed"
    def attackRoll(self):
        roll = randint(1, 20) + self.atkMod
        return roll
    def damageRoll(self):
        roll = randint(1, 4) + self.dmgMod
        return roll

class BadWeapon(Weapon):
    def __init__(self):
        self.atkMod = 3
        self.dmgMod = 3
    def display(self):
        return "equipped with a mediocre weapon"
    def attackRoll(self):
        roll = randint(1, 20) + self.atkMod
        return roll
    def damageRoll(self):
        roll = randint(1, 6) + self.dmgMod
        return roll

class AverageWeapon(Weapon):
    def __init__(self):
        self.atkMod = 4
        self.dmgMod = 4
    def display(self):
        return "equipped with a decent weapon"
    def attackRoll(self):
        roll = randint(1, 20) + self.atkMod
        return roll
    def damageRoll(self):
        roll = randint(1, 8) + self.dmgMod
        return roll

class GoodWeapon(Weapon):
    def __init__(self):
        self.atkMod = 6
        self.dmgMod = 6
    def display(self):
        return "equipped with a good weapon"
    def attackRoll(self):
        roll = randint(1, 20) + self.atkMod
        return roll
    def damageRoll(self):
        roll = randint(1, 8) + self.dmgMod
        return roll

class GreatWeapon(Weapon):
    def __init__(self):
        self.atkMod = 7
        self.dmgMod = 7
    def display(self):
        return "equipped with a great weapon"
    def attackRoll(self):
        roll = randint(1, 20) + self.atkMod
        return roll
    def damageRoll(self):
        roll = randint(1, 10) + self.dmgMod
        return roll

class BestWeapon(Weapon):
    def __init__(self):
        self.atkMod = 9
        self.dmgMod = 9
    def display(self):
        return "equipped with a majestic weapon"
    def attackRoll(self):
        roll = randint(1, 20) + self.atkMod
        return roll
    def damageRoll(self):
        roll = randint(1, 6) + randint(1, 6) + self.dmgMod
        return roll