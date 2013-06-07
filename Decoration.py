class ArmorColor(object):
    def __init__(self):
        self.armorColor = None

    def describe(self):
        return "The combatant is equipped in armor"

    def getArmorColor(self):
        return self.armorColor

class ArmorColorDecorator(ArmorColor):
    def __init__(self, decorated):
        super(ArmorColorDecorator, self).__init__()
        self.decorated = decorated

    def describe(self):
        return self.decorated.describe() + " with "

class RedArmor(ArmorColorDecorator):
    def __init__(self, decorated):
        super(RedArmor, self).__init__(decorated)

    def describe(self):
         return super(RedArmor, self).describe() + "red lacquer."


class BlueArmor(ArmorColorDecorator):
    def __init__(self, decorated):
        super(BlueArmor, self).__init__(decorated)

    def describe(self):
       return super(BlueArmor, self).describe() + "blue lacquer."


class GreenArmor(ArmorColorDecorator):
    def __init__(self, decorated):
        super(GreenArmor, self).__init__(decorated)

    def describe(self):
        return super(GreenArmor, self).describe() + "green lacquer."

class NormalArmor(ArmorColorDecorator):
    def __init__(self, decorated):
        super(NormalArmor, self).__init__(decorated)

    def describe(self):
        return super(NormalArmor, self).describe() + "no lacquer."