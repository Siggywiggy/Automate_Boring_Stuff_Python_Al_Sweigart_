import zombiedice
import random


class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        shotguns = 0

        while diceRollResults is not None:
            random_choice = random.randint(0, 1)
            print(random_choice)
            if random.randint(0, 1) == 0:
                break
            else:
                diceRollResults = zombiedice.roll()  # roll again


class MyZombie_2_brains:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0

        while diceRollResults is not None:
            brains += diceRollResults["brains"]
            if brains < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class MyZombie_2_shotguns:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()

        shotguns = 0

        while diceRollResults is not None:
            shotguns += diceRollResults["shotgun"]
            if shotguns >= 2:
                break
            else:
                diceRollResults = zombiedice.roll()  # roll again


class MyZombie_4_rolls:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()

        dice_rolls = random.randint(1, 4)
        shotguns = 0

        while diceRollResults is not None:
            shotguns += diceRollResults["shotgun"]
            dice_rolls -= 1
            if shotguns >= 2 or dice_rolls == 0:
                break
            else:
                diceRollResults = zombiedice.roll()  # roll again


class MyZombie_more_shotguns:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()

        shotguns = 0
        brains = 0
        while diceRollResults is not None and brains >= shotguns and shotguns != 3:
            brains += diceRollResults["brains"]
            shotguns += diceRollResults["shotgun"]
            diceRollResults = zombiedice.roll()  # roll again


zombies = (
    MyZombie(name="My Zombie Bot random choice"),
    # Add any other zombie players here.
    MyZombie_2_brains(name="My Zombie until 2 brains"),
    MyZombie_2_shotguns(name="My Zombie until 2 shotguns"),
    MyZombie_4_rolls(name="My Zombie 4 rolls"),
    MyZombie_more_shotguns(name="My Zombie more shotguns"),
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
# zombiedice.runWebGui(zombies=zombies, numGames=1000)
