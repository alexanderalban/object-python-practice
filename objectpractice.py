# Creating and manipulating objects in python

# Classes

import turtle


class things:
    pass

# Children and Parents


class inanimate(things):
    pass


class animate(things):
    pass


class sidewalks(inanimate):
    pass


class animals(animate):
    pass


class mammals(animals):
    pass


class giraffes(mammals):
    pass

# Adding objects
# a giraffe names Reginald


reginald = giraffes()

# Functions of classes


class SillyClass:
    def ClassFunction():
        print("This is a class function.")

    def AlsoClassFunction():
        print("This is also a class function.")


# Adding class characteristics as functions

class animals(animate):
    def breathe(self):
        pass

    def move(self):
        pass

    def eat_food(self):
        pass


class mammals(animals):
    def feed_young_with_milk(self):
        pass


class giraffes(mammals):
    def eat_leaves_from_trees(self):
        pass

# Why use classes and objects?


reginald = giraffes()
reginald.move()
reginald.eat_leaves_from_trees()

harold = giraffes()
harold.move()


# Proper objects and classes

class animals(animate):
    def breathe(self):
        print("breathing")

    def move(self):
        print("moving")

    def eat_food(self):
        print('eating food')


class mammals(animals):
    def feed_young_with_milk(self):
        print("feeding young")


class giraffes(mammals):
    def eat_leaves_from_trees(self):
        print("eating leaves")


reginald = giraffes()
harold = giraffes()
reginald.move()
harold.eat_leaves_from_trees()


# Let's make it visual


# avery = turtle.Pen()
# kate = turtle.Pen()

# avery.forward(50)
# avery.right(90)
# avery.forward(20)

# kate.left(90)
# kate.forward(100)

# jacob = turtle.Pen()
# jacob.left(180)
# jacob.forward(80)

# kate = turtle.Pen()
# kate.right(90)
# kate.forward(100)

# input("Here to keep the window from closing, don't mind me")


# Functions calling other functions

class giraffes(mammals):
    def find_food(self):
        self.move()
        print("I've found food!")
        self.eat_food()

    def eat_leaves_from_trees(self):
        self.eat_food()

    def dance(self):
        self.move()
        self.move()
        self.move()
        self.move()


reginald = giraffes()
reginald.dance()

# Initializing an object


class giraffes:
    def __init__(self, spots):
        self.giraffe_spots = spots


ozwald = giraffes(100)
gertrude = giraffes(150)

print(ozwald.giraffe_spots)
print(gertrude.giraffe_spots)


# More Practice!

class ironman_suit:
    def __init__(self, number):
        self.suitnumber = number

    def rightarmmove(self):
        print("Right arm move")

    def leftarmmove(self):
        print("Left arm move")

    def rightlegmove(self):
        print("Right leg move")

    def leftlegmove(self):
        print("Left leg move")

    def dance(self):
        self.rightarmmove()
        self.leftarmmove()
        self.rightlegmove()
        self.leftlegmove()
        print("Robot_Rock.mp4")


MK42 = ironman_suit(42)
MK42.dance()
print(MK42.suitnumber)


# Let's build another one

class power_ranger:
    def __init__(self, suitcolor, ranger_weapon, dinozord):
        self.color = suitcolor
        self.weapon = ranger_weapon
        self.zord = dinozord

    def teamcall(self):
        print("Go Go Power Rangers!")

    
Jason = power_ranger("Red", "Power Sword", "Tyrannosaurus")
Tommy = power_ranger("Green", "Dragon Dagger", "Dragonzord")
Kimberly = power_ranger("Pink", "Power Bow", "Pterodactyl")
Trini = power_ranger("Yellow", "Power Daggers", "Sabretooth Tiger")
Zack = power_ranger("Black", "Power Axe", "Mastodon")
Billy = power_ranger("Blue", "Power Lance", "Triceratops")

Tommy.teamcall()
Jason.teamcall()