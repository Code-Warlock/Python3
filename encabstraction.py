"""Encapsulation and Data Abstraction in Python """
import random

class User():
  def __init__(self, first_name , last_name , email):
    rand = random.randint(1, 4)
    self.name = first_name + " " + last_name
    self.user_name = last_name[0] +  last_name[rand] + str((rand * 10))
    self.__password = self._generate_password()
    
  def _generate_password(self):
    seed = []
    password = ""
    for each in range(48, 123):
      if each in range(48 , 58) or each in range(97 , 123):
        seed.append(each)
    for each in range(1,8):
      rand = random.randint(0,20)
      password += chr(seed[rand])
    return password
  
  def show_password(self):
    return self.__password
  def change_password(self , new_password):
    self.__password = new_password
    
    
    
user1 = User("Desmond", "Michael", "dessymichaeltgp123@gmail.com")
# user1.name = "I changed the name"
# user1.__password = "gxafshgdbjm"
print(user1.change_password("dessyMMM123"))
print(user1.show_password())
# print(user1.pass)


# 48-57 === numbers
# small_letter === 97 ,122