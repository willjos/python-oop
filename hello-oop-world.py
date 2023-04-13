# Note: If we have a large class, it is best practice to make its own file and then import this into the main program
# e.g from will import Will
# e.g from world import World

class Person:
    def __init__(self, name, age, fav_food): # this is the constructor, it must always have self as an argument
        self.name = name # all properties are declared with self to bind them to the object.
        self.age = age
        self.fav_food = fav_food

    def say_hello(self): # methods are declared just as normal functions, but self is always required.
        print(f"Hello, World. My name is {self.name}") # access property via self keyword
    
    def say_other_facts(self):
        print(f"I am {self.age}, and my favourite food is {self.fav_food}")


class World:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello. I am {self.name}.")

    def say_age(self):
        print(f"I am {self.age} years old.")

myself = Person("Will", 23, "Burrito")
myself.say_hello()
myself.say_other_facts()

earth = World("Earth", int(5e9))
earth.say_hello()
earth.say_age()