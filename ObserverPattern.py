#=======================================================================================================================
# Observer Pattern Base #

class Observable(object):
    def __init__(self):
        self._observers = []

    def addObserver(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def removeObserver(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notifyObservers(self):
        for observer in self._observers:
            observer.update(self)

class Observer(object):
    def update(self, observable):
        pass ## any subclass pulls data from observable here.

class HealthObserver(Observer):
    def __init__(self, observable):
        self.observable = observable
        self.maxhealth = observable.health
        self.health = None
        observable.addObserver(self)

    def update(self, observable):
        self.health = observable.getHealth()
        if self.health < (self.maxhealth / 2):
            self.display(observable)

    def display(self, observable):
        print(observable.name + " is bloodied! ")