#operater overloading
print(type(1+2)) #3
print(type("me "+" I"))#concatenation
print(type([1,2,3]+ [4,5,6]))#merge

#method overriding
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"  # Dog-specific implementation

class Cat(Animal):
    def speak(self):
        return "Meow! Meow!"  # Cat-specific implementation

# Creating objects
animals = [Dog(), Cat(), Animal()]

# Using polymorphism
for animal in animals:
    print(animal.speak())
