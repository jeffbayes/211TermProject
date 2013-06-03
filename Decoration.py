__author__ = 'kent'

import sys

class IceCream(object):
    BASIC_CALORIES = 200

    def __init__(self):
        self.calories = IceCream.BASIC_CALORIES

    def describe(self):
        return "vanilla ice cream"

    def getCalories(self):
        return self.calories

class IceCreamDecorator(IceCream):
    def __init__(self, decorated):
        super(IceCreamDecorator, self).__init__()
        self.decorated = decorated

    def describe(self):
        return self.decorated.describe() + " with "

class NuttyDecorator(IceCreamDecorator):
    NUTS_CALORIES = 100

    def __init__(self, decorated):
        super(NuttyDecorator, self).__init__(decorated)
        self.calories = self.decorated.calories + NuttyDecorator.NUTS_CALORIES

    def describe(self):
         return super(NuttyDecorator, self).describe() + "Nuts"


class HoneyDecorator(IceCreamDecorator):
    HONEY_CALORIES = 150

    def __init__(self, decorated):
        super(HoneyDecorator, self).__init__(decorated)
        self.calories = self.decorated.calories + HoneyDecorator.HONEY_CALORIES

    def describe(self):
       return super(HoneyDecorator, self).describe() + "Honey"


class SpamDecorator(IceCreamDecorator):
    SPAM_CALORIES = 20

    def __init__(self, decorated):
        super(SpamDecorator, self).__init__(decorated)
        self.calories = self.decorated.calories + SpamDecorator.SPAM_CALORIES

    def describe(self):
        return super(SpamDecorator, self).describe() + "Spam"

#===============================================================================

simpleDessert = IceCream()
print ("simple desert: " + simpleDessert.describe())
print ("calories = " + str(simpleDessert.getCalories()))

dessert1 = NuttyDecorator(simpleDessert)
print ("desert1: " + dessert1.describe())
print ("calories = " + str(dessert1.getCalories()))

#dessert2 = HoneyDecorator(NuttyDecorator(IceCream()))
dessert2 = HoneyDecorator(NuttyDecorator(simpleDessert))
print ("desert2: " + dessert2.describe())
print ("calories = " + str(dessert2.getCalories()))

dessert3 = NuttyDecorator(HoneyDecorator(IceCream()))
print ("desert3: " + dessert3.describe())
print ("calories = " + str(dessert3.getCalories()))

dessert4 = SpamDecorator(SpamDecorator(SpamDecorator(IceCream())))
print ("desert4: " + dessert4.describe())
print ("calories = " + str(dessert4.getCalories()))