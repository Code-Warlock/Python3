""" Object Oriented Programming in Python """

class Animal:
  def __init__(self , name , specie , legs):
    self.name = name
    self.specie = specie
    self.legs = legs
  def say_class(self):
    return f"I belong to the Animal Class"
    
  def make_sound(self):
    print(f"Hello My name is  : {self.name}")
  

# print(Max.make_sound())
# print(felix.make_sound())

# Inheritance

        
class Dog(Animal):
  def __init__(self, name, specie, legs , breed):
    self.breed = breed
    super().__init__(name , specie , legs)
   
  def say_class(self):
    return f"I belong to the Dog Class"
  def say_breed(self):
    return f"I belong to the {self.breed}"
  def make_sound(self):
    super() .make_sound()
    print("I am a Dog")
    
class Cat(Animal):
  pass

Max = Dog("Max" , "Dog" , 4 , "German Shepherd")
panrer = Cat("Panrer","Cat", 4)
print(Max.make_sound())