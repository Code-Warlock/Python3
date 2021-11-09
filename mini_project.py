#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 09:35:07 2021

@author: babatundebolarinwa
"""


from random import randint as r
import time
import datetime as dt
_file = []


class Registration:
    
    _pin = r(1, 1000)
    _id = r(1, 1000000)
    _file = []

    def __init__(self, firstname, lastname, matric_number, gender, department,faculty, date_joined = dt.date.today()):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = (self.firstname + " " + self.lastname).upper()
        self.matric_number = matric_number
        self.gender = gender.upper()
        self.department = department
        self.faculty = faculty
        self.id = Registration._id
        self.pin = Registration._pin
        self.datejoined = date_joined
        self.file = "".join([x[0] + x[3] for x in firstname.split()])+".txt"
        Registration._file.append(self.file)

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

            """ .format(self.firstname,self.lastname, self.fullname, self.matric_number,  self.id, self.pin, self.gender, self.department, self.faculty)


class Admin(Registration):



    def ___init__(self, firsname, lastname, matric_number, gender, department, faculty, date_joined = dt.date.today()):
        super().__init__(firsname, lastname, gender,date_joined = dt.date.today())
        username = input("Enter your username correctly : ")
        self.username = username
        position = input("Position : ")
        self.position = position
        pin = int(input("Pin : "))
        while True:
            if len(pin) > len(4):
                print("MAXIMUM PIN REQUIRED EXCEEDED!!!!!!!")
            else:
                if len(pin) == len(4):
                    self.pin = pin
                    break

            """This method should allow the admin to access the members profile"""

        def read(self):
            with open(self.file, "r")as f:
                print(f.read())

        def datejoined(self):
            return"{} membership profile was autorized on {}".format(self.fullname,  self.datejoined)

student1 = Registration("Babatunde", "Bolarinwa", 16170619, "Male", "psychology", "Social science")
student2 = Registration("Ajibade", "Badmus", 1213198, "Female", "Computer science", "Science")

print(student1.RegistrationProfile())
print(student2.RegistrationProfile())