#=======================================================================================================================
# Defenses and Armor Category #

class Defenses(object):
    def armor(self):
        pass
    def display(self):
        pass

class Defenseless(Defenses):
    def armor(self):
        return 0
    def display(self):
        return "defenseless"

class BadArmor(Defenses):
    def armor(self):
        return 3
    def display(self):
        return "mediocre armor"

class AverageArmor(Defenses):
    def armor(self):
        return 4
    def display(self):
        return "decent armor"

class GoodArmor(Defenses):
    def armor(self):
        return 6
    def display(self):
        return "good armor"

class GreatArmor(Defenses):
    def armor(self):
        return 7
    def display(self):
        return "great armor"

class BestArmor(Defenses):
    def armor(self):
        return 9
    def display(self):
        return "the finest armor"