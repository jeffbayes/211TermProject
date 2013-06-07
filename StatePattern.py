# Credits to Kent Stevens. Used the outline code and modified it to my needs.

class DivineInfluence(object):
    def __init__(self, owner):
        self.owner = owner

    def action(self, hero, target):
        pass


class NotMyTurn(DivineInfluence):
    def action(self, hero, target):
        pass

class MyTurn(DivineInfluence):
    def action(self, hero, target):
        if hero.currentState == hero.notMyTurn or hero.health <= 0:
            return
        if hero.faction != "FFA":
            if target.faction == hero.faction:
                return
        if hero.name == target.name or target.health <= 0:
            return

        notBloody = None
        if target.health > (target.maxhealth / 2):
            notBloody = True
        atkRoll = hero.weapon.attackRoll()
        dmgRoll = hero.weapon.damageRoll()
        if atkRoll >= target.defenses:
            target.health -= dmgRoll
            print(hero.name + " strikes " + target.name + ", dealing " + str(dmgRoll) + " damage.")
            if target.health <= 0:
                print(target.name + " has fallen unconscious!")
                return
            if notBloody == True and target.health < (target.maxhealth / 2):
                target.notifyObservers()
        else:
            print(hero.name + " cannot penetrate " + target.name + "'s defenses.")

class TurnBased(MyTurn, NotMyTurn):
    def __init__(self):
        self.myTurn = MyTurn(self)
        self.notMyTurn = NotMyTurn(self)
        self.currentState = None

        self.myTurnNow()

    def myTurnNow(self):
        self.currentState = self.myTurn

    def turnEnds(self):
        self.currentState = self.notMyTurn

    def turnChange(self):
        if self.currentState == self.myTurn:
            self.currentState = self.notMyTurn
        else:
            self.currentState = self.myTurn

    def acceptVisitor(self, visitor):
        visitor.visit(self)


class Visitor(object):
    def visit(self, visited):
        pass

class Buffer(Visitor):
    def visit(self, visited):
        visited.myTurnNow()

class Debuffer(Visitor):
    def visit(self, visited):
        visited.turnEnds()