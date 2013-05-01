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
        return 30
    def display(self):
        return "mediocre armor"

class AverageArmor(Defenses):
    def armor(self):
        return 40
    def display(self):
        return "decent armor"

class GoodArmor(Defenses):
    def armor(self):
        return 60
    def display(self):
        return "good armor"

class GreatArmor(Defenses):
    def armor(self):
        return 70
    def display(self):
        return "great armor"

class BestArmor(Defenses):
    def armor(self):
        return 90
    def display(self):
        return "the finest armor"