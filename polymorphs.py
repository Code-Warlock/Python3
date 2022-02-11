""" Other features of OOP """

class School():
  def __init__(self, name , established):
    self.name = name
    self.established = established

  def profile(self):
    return f"""School name : {self.name}
Established : {self.established} """




class Teacher():
  def __init__(self, name, school):
    self.name = name
    self.school = school
  def profile(self):
    return f"""Teacher's name : {self.name}
Teacher's school : {self.school}"""
  
  
class Student:
  def __init__(self , name , school , teachers , courses):
    self.name = name
    self.school = school 
    self.teachers = teachers.split(',')
    self.courses = courses.split(',')
  
  def profile(self):
    return f"""Student's name : {self.name}
Student's school : {self.school}
Student's teachers : {self.teachers}
Student's courses : {self.courses}"""
  
  
# ap = School(input("Enter the name of your school : "), input("Enter the year of the establishment : "))

# d1 = Teacher(input("Enter your name : "), ap.name)

# des = Student(input("Enter your name : "), ap.name, input("Enter your teacher(s) name : "), input("Enter your courses : "))

# objects = [ap , des , d1]

# for each in objects:
#   print(each.profile())

class Animal():
  def __init__(self , name , specie , legs):
    raise NotImplementedError("This method should not be implemented")
  
class Dog(Animal):
  def __init__(self, name, specie, legs , breed):
    self.name = name
    self.specie = specie
    self.legs = legs
    self.breed = breed

class Cat(Animal):
  def __init__(self, name, specie, legs , fur):
    self.name = name
    self.specie = specie
    self.legs = legs
    self.fur = fur

class Monkey(Animal):
  def __init__(self, name, specie, legs , tail):
    self.name = name
    self.specie = specie
    self.legs = legs
    self.tail = tail
    
    
try:
  dog1 = Dog("Max" , "test" , 4 , "German shepherd")
  # print(dog1.name)

  snake = Animal("serp", "long snakes", 0)
  print(snake)
except NotImplementedError:
  print("Base Class 'Animal' must be inherited before use")