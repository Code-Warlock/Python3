#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:35:07 2021
@author: babatundebolarinwa
"""


from random import randint as r
import time
import datetime as dt



class Registration:
    def __init__(self, firstname, lastname, matric_number, gender, department,faculty,date_joined = dt.date.today()):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = (self.firstname + " " + self.lastname).upper()
        self.matric_number = matric_number
        self.gender = gender
        self.department = department
        self.faculty = faculty
        self.id = r(1, 1000000)
        self.pin = r(1, 1000)
        self.date_joined = date_joined
        self.file = "".join([x[0] + x[3] for x in firstname.split()])+".txt"
        with open("reg.txt","a") as f:
            f.write(self.file)

    def RegistrationProfile(self):
        return """
                    PROFILE

            firstname = {}
            lastname = {}
            fullname = {}
            matric number = {}
            id = {}
            pin = {}
            gender = {}
            Department = {}
            Faculty = {}
            date joined = {}

            """.format(self.fir stname,self.lastname, self.fullname, self.matric_number,  self.id, self.pin, self.gender, self.department, self.faculty, self.date_joined)



class Admin(Registration):
    """This class should allow the admin to manage the membership portal"""

    _username = input("Username : ")
    _pin = r(1, 1000)
    while True:
        if len(str(_pin)) > 4:
            raise NotImplementedError("MAXIMUM PIN REQUIRED EXCEEDED")

        elif len(str(_pin)) == 4:
            _verified_pin = int(input(f"Welcome {_username}\nPlease verify pin : "))
            if _pin == _verified_pin:
                print("Welcome to the Admin portal")
                break

    def __init__(self, firstname, lastname, username, gender, pin, position):
        super().__init__(firstname, lastname, gender)
        self.username = Admin._username
        self.pin = Admin._verified_pin

    def read(self):
        with open(self.file, "r") as f:
            f.read = self.file
            print(f.read(self.file))


with open(Registration._file, "w") as f:
    f.write(
     student1 = Registration("Bolarinwa", "Bolarinwa",16170619,"m","Psychology","social science"),
     student2 = Registration("Ajibade","Adekoya",1617021,"f","Computer science","Science")
    )
admin1 = Admin()
print(admin1.read())
