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


avery = turtle.Pen()
kate = turtle.Pen()

avery.forward(50)
avery.right(90)
avery.forward(20)

kate.left(90)
kate.forward(100)

jacob = turtle.Pen()
jacob.left(180)
jacob.forward(80)

kate = turtle.Pen()
kate.right(90)
kate.forward(100)

input("Here to keep the window from closing, don't mind me")
