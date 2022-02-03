""" Introduction to Object Oriented Programming in Python """

# Inheritance
# Abstraction
# Encapsulation
# Polymorphism


class Human:
  
  def __init__(self , name ,skin_color, legs = 2  , hands=2):
    self.name = name
    self.skin_color = skin_color
    self.hands = hands
    self.legs = legs


  def say_name(self):
    return f"Hello my name is {self.name}"


human = Human("Desmond" , "black")
human1 = Human("Samuel","black")
print(human1.legs)

# human1 = Human()
# des = Human()

































# def hello():
#   return 'Hello World'

# if __name__ != '__main__':
#   print("You didn't run this directly!")