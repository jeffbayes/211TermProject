Term Project for CIS 211
Jeff Bayes


Just as fair warning, I'm quite aware that this project is a bit bloated. We were told to use every design pattern
we learned in this class in one project, and as the term went on the designs became less and less useful for my
final goal: a battle simulator. I can think of a few things I would do now, such as asking for input to create the 
heroes rather than dependency on the driver. However, this is by far the most thorough project we have done in
class and all code is my own.


DEPENDENCIES:
Python 3.3


PATTERN USE:
STRATEGY: See the Defenses.py and Weapon.py files. I used the strategy pattern to assign the strength of armors and weaponry of my characters.
            These are set to Unarmed and Defenseless initially, so in order to properly simulate a battle, the driver must assign weaponry and armor to the combatants.
OBSERVER: See the ObserverPattern.py file. I used it to monitor the health of the opponent and notify the user when the opponent is bloodied (half health remaining).
            The bloodied notification doesn't do anything (yet), but it could be modified to add more functionality when a character is bloodied.
DECORATOR: See the Decoration.py file. I used it to decorate the combatants' armor to reflect the faction they're fighting for. Red lacquer for redTeam, blue for blueTeam.

STATE: See the StatePattern.py file and my attack function in the Character.py file. I used it to make it so each character only had one action per turn. In order to make this work, I cooked in the...
            VISITOR pattern in the StatePattern.py file, to visit each character and give another action at the end of each round.


GENERAL THOUGHTS:
    The usage for this is to simply run the driver.py file.

While we're on general thoughts, I thought it was very challenging (in a not-good way) to implement all of these patterns into one project. I could understand if there were an
outline of where to start and some suggestion on how to meaningfully implement the patterns, but both without guidance and with very unique projects across the spectrum,
it felt like I was bloating my project rather than giving it something new and exciting. I would prefer either tighter guidelines (or at least tighter suggestions) to
the project, or perhaps breaking the patterns into smaller projects, maybe two patterns per project.
