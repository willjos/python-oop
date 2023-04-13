class Pet:
    def __init__(self, name, age, owner): # these are the properties that any pet will have
        self.name = name
        self.age = age
        self.owner = owner

    def print_attributes(self): # a method for any pet that prints their attributes.
        print(f"Name: {self.name}, Age: {self.age}, Owner: {self.owner}")

    def speak(self):
        print("I am not sure what to say yet.")

class Dog(Pet): # this is the syntax for a Dog inheriting from Pet.
    def speak(self): # this overrides the speak function declared in the Pet class, polymorphism example.
        print("Woof")

class Cat(Pet):
    def __init__(self, name, age, owner, colour): # all params and self
        super().__init__(name, age, owner) # call super().__init__() with the parent params
        self.colour = colour # set the new property in the child

    def speak(self): # another instance of polymorphism, overriding the speak function. 
        print("Meow")

bertie = Dog("Bertie", 14, "Simms Family")
bertie.print_attributes()
bertie.speak()