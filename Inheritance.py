class Animal:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print("Hi")

    def __str__(self):
        return("Animal")

class Cat(Animal):
    # Cat inherits name, age, and say_hi from Animal
    def __init__(self, name, age, sound):
        #Animal.__int__(name, age)
        super().__int__(name, age) # Easier way to do it
        self.sound = sound

    def say_sound(self):
        print(self.sound)

    def __str__(self):
        return "Cat's Name: " + self.name

cat = Cat("Billy", 5, "Meow")
cat.say_hi()
cat.say_sound()
print(cat)

