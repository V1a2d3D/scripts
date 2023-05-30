from random import randint


class Dice:
    """Создание шестигранного кубика"""

    def __init__(self, sides_dice=6):
        self.sides_dice = sides_dice

    def roll_dice(self):
        return randint(1, self.sides_dice)
