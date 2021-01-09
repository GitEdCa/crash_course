from random import randint

class Dice():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_dice(self):
        side = randint(1, self.sides)
        print(side)

sides6 = Dice()
sides6.roll_dice()
sides6.roll_dice()
sides6.roll_dice()
sides6.roll_dice()
sides6.roll_dice()
sides6.roll_dice()
sides6.roll_dice()
sides6.roll_dice()
sides6.roll_dice()
sides6.roll_dice()

sides10 = Dice(10)
sides10.roll_dice()
sides10.roll_dice()
sides10.roll_dice()
sides10.roll_dice()
sides10.roll_dice()
sides10.roll_dice()
sides10.roll_dice()
sides10.roll_dice()
sides10.roll_dice()
sides10.roll_dice()

sides20 = Dice(20)
sides20.roll_dice()
sides20.roll_dice()
sides20.roll_dice()
sides20.roll_dice()
sides20.roll_dice()
sides20.roll_dice()
sides20.roll_dice()
sides20.roll_dice()
sides20.roll_dice()
sides20.roll_dice()
