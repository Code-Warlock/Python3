""" Dictionaries in Python """
# Key-Value paired data structure
students = {
    "student1" : "Desmond",
    "student2" : "Samuel",
    "student3" : "Julius",
    "student4" : "Mubarak"
}
# students["student5"] = "Michael"
# students["student1"] = ""
# students.update({"student6" : "Lawal","student7" : "Abidemi"})
# # print(students["student5"])
# print(students.get("student1"))


# print(students.items())
# print(students.keys())
# print(students.values())
# for key,value in students.items():
#     print(f"{key}=======================> {value}")

# school = dict()
# counter = 1
# while True:
#     name = input("Enter student name : ")
#     gender = input("Gender : M/F ")
#     age = input("Enter student age : ")
#     school.update({"student"+str(counter) : [name,gender,age]})
#     add = input("Add another? : y/n ").lower()
#     if add == "y":
#         counter += 1
#         continue
#     else:
#         print(f"""=================Students List.======================""")
        # for key,value in school.items():
        #     print(f"{key} : {value}")
for each in students.items():
    print(students.items()[0])




















#
