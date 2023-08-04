class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f"Hi, my name is {self.name}. I am {self.age} years old")
    def voice(self):
        print(type(self).my_voice)
class Dog(Animal):
    my_voice = "wof, wof"
class Cat(Animal):
    mu_voice = "meow, meow"