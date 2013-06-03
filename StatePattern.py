# Credits to Kent Stevens. Used the outline code and modified it to my needs.


class DivineInfluence(object):
    def __init__(self, owner):
        self.owner = owner

"""    def whatz4DinDin(self):
        pass

    def wannaGo2PDX(self):
        pass"""


class NotMyTurn(DivineInfluence):
    """def whatz4DinDin(self):
        print ("road kill")

    def wannaGo2PDX(self):
        print ("no")
        self.owner.myTurnNow()"""

class MyTurn(DivineInfluence):
    """def action(self):
        pass

    def whatz4DinDin(self):
        print ("chicken")

    def wannaGo2PDX(self):
        print ("yeah!!!")
        self.owner.myTurnNow()"""

class TurnBased(object):
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

    """def whatz4DinDin(self):
        self.currentState.whatz4DinDin()

    def wannaGo2PDX(self):
        self.currentState.wannaGo2PDX()"""

    def acceptVisitor(self, visitor):
        visitor.visit(self)
    #    self.currentState.acceptVisitor(self, visitor)


class Visitor(object):
    def visit(self, visited):
        pass

class Buffer(Visitor):
    def visit(self, visited):
        visited.myTurnNow()

class Debuffer(Visitor):
    def visit(self, visited):
        visited.turnEnds()

class TurnChange(Visitor):
    def visit(self, visited):
        visited.turnChange()

def main():
    """
p = TurnBased()
p.turnEnds()
print ("Hi honey, I'm home!!! What's for din-din?")
p.whatz4DinDin()
print ("Don't be grumpy.  So you bombed the midterm. <Sheesh>   Maybe I'll just order pizza instead")
fedEx = Buffer()
print ("Hey, FedEx is out in front.  Looks like you've got a visitor")
p.acceptVisitor(fedEx)
print ("Wow, an espresso maker! That's pretty cool, ...")
print ("... and by the way, if we were to eat here, what's for dinner?")
p.whatz4DinDin()"""
    pass