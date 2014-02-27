"""
Author: Jeff Bayes
Class: CIS 211
"""

from Character import *

def main():
    """
    Here is the driver for the program. I created a bunch of heroes, assigned them to two opposing factions, and let the virtual text-based
    blood spill!
    """
    characters = []

    gardakan = Hero("Gardakan", 5, "Red")
    mordak = Hero("Mordak", 7, "Blue") #Mordak and the dummy are on the same faction, so they cannot attack one another.
    dummy = Hero("Training Dummy", 1, "Blue")
    a = Hero("Anakin", 6, "Red")
    b = Hero("Balthazar", 19, "Blue")
    c = Hero("Cantar", 17, "Red")
    d = Hero("Jimmy John", 12, "Red")
    dummy.health = 150
    ggg = Buffer()


    # set the weapons and armors of my heroes
    mordak.setArmor(BestArmor())
    mordak.setWeapons(BadWeapon())
    gardakan.setArmor(BestArmor())
    gardakan.setWeapons(BadWeapon())

    ### ======================================================= ###
    characters.append(gardakan)
    characters.append(mordak)
    characters.append(dummy)
    characters.append(a)
    characters.append(b)
    characters.append(c)
    characters.append(d)
    blueTeam = []
    redTeam = []

    for hero in characters:
        if hero.faction == "Blue":
            blueTeam.append(hero)
        if hero.faction == "Red":
            redTeam.append(hero)
    ### ======================================================= ###

    for reds in redTeam:
        reds.announce(reds.name)
        print(RedArmor(reds).describe())
    for blues in blueTeam:
        blues.announce(blues.name)
        print(BlueArmor(blues).describe())
    print("!!!!! FIGHT !!!!!")
    while redTeam != [] and blueTeam != []:
        for blues in blueTeam:
            for reds in redTeam:
                reds.attack(blues)
                if blues.health <= 0:
                    if blues in blueTeam:
                        blueTeam.remove(blues)
                    for blues in blueTeam:
                        print(blues.name + " fights on for the Blue team.")
        for reds in redTeam:
            for blues in blueTeam:
                blues.attack(reds)
                if reds.health <= 0:
                    if reds in redTeam:
                        redTeam.remove(reds)
                    for reds in redTeam:
                        print(reds.name + " fights on for the Red team.")
        for hero in characters:
            ggg.visit(hero)


    if redTeam == []:
        print("Blue team is victorious!")
    else:
        print("Red team is victorious!")




main()