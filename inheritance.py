
class Student():
  
  def __init__(self , name  , course , level , school="Aptech"):
    self.name = name
    self.course = course
    self.level = level
    self.school = school
  def say_name(self):
    return f"Hello I am a Student.\nMy name is {self.name}"
  def graduate(self):
    self.level += 1
  def change_school(self ,school):
    change_school = input("Do you want to change your school : y/n ")
    self.school = school
  def print_profile(self):
    return f"Student Name : {self.name}\nStudent's Level : {self.level}\nStudent's course : {self.course}\nSchool : {self.school}"


s1 = Student(name = input("Enter your name : ") , course = input("Enter your course : ") , level = int(input("Enter your level : ")), school = input("Enter your school : "))

s2 = Student(name = input("Enter your name : ") , course = input("Enter your course : ") , level = int(input("Enter your level : ")), school = input("Enter your school : "))
s3 = Student(name = input("Enter your name : ") , course = input("Enter your course : ") , level = int(input("Enter your level : ")), school = input("Enter your school : "))
students = [s1 , s2 , s3]

# print(s1.level)
# print(s1.say_name())
# s1.graduate()
# print(s1.level)


# s1 = Student(name , course , level ,school)

# print(s1.change_school('MiddleSex'))
# print(s1.print_profile())



class Course():
  def __init__(self , name , duration):
    self.name = name
    self.duration = duration
    self.students = []
    
  def course_profile(self):
    return f"""
  Course : {self.name}
  Duration : {self.duration}
  No of Student : {len(self.students)}
  """
  def add_student(self , student):
   self.students.append(student)


course_name = input("Enter your course name : ")
course_duration = input("Enter your course's duration : ")


c1 = Course(course_name , course_duration)
for student in students:
  if student.course.lower() == c1.name.lower():
    c1.add_student(student)
    
print(c1.students)
print(c1.course_profile())

add_student_confirm = input("Do you want to add students (y/n) : ")
if 'y' in add_student_confirm:
    while True:
      temp = Student(name = input("Enter your name : ") , course = input("Enter your course : ") , level = int(input("Enter your level : ")), school = input("Enter your school : "))
      if temp.course.lower() == c1.name.lower():
        c1.add_student(temp)
      ans = "Do want to add more? : "
      if not('y' in ans):
        break

print(c1.course_profile())