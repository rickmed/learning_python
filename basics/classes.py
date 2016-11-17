# Classes are used similar to objects in JS
# (an abstract representation of a real life concept)


class Animal:
    # __name = ''  # __ means its a private property
    # __height = 54

    def __init__(self, name, height):  # this is the constructor
        self.name = name
        self.__height = height

    def bark(self):  # self is this in other languages
        return 'Hi my name is: ' + self.name

    # def set_name(self, name):
    #     self.__name = name

wolf = Animal('charlie', 45)  # here I call the constructor (__init__)

wolf.name = 'wuffles'

print(wolf.name)
print(wolf.bark())


# You can't add methods on the fly to a class as using protorypes in JS
