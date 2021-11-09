#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 15:28:18 2021

@author: babatundebolarinwa
"""

from random import randint as r
class SignUp:
    _fn = []
    def __init__(self,firstname,lastname,rank,association):
        pass
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = "Amb " + self.firstname + " " + self.lastname
        self.rank = rank
        self.association = association
        self.password = self.firstname
        self._id = r(1, 100000)
        with open(self.password + ".txt", "w") as up:
            up.write(self.password)
        with open(self.fullname+"_id"+".txt" , "w") as uid:
            uid.write(str(self._id))
        SignUp._fn.append(self.password)
        SignUp._fn.append(self._id)


class Login(SignUp):

    def __init__(self,firstname,lastname,rank,association,id_number,password):
        super().__init__(firstname,lastname,rank,association)
        try:
            self.id_number = id_number
            self.password = password
            with open(self.password+".txt", "r") as fpass:
                saved_password = f.read()
            with open(self.fullname+"_id"+".txt") as f_id:
                saved_id = f_id.read()
            if self.id_number != saved_id or self.password != saved_id:
                raise NotImplementedError("Details not found")
            else:
                print("Welcome user")
        except (FileNotFoundError):
            raise NotImplementedError("Details not found")


firstname = input("Enter your first name : ")
lastname = input("Enter your last name : ")
association = input("Enter your association : ")
rank = input("Enter your rank : ")
# user = SignUp(firstname, lastname,rank,association)
id_number = input("Enter your id number : ")
password = input("Enter your password : ")
try:
    user2 = Login(firstname, lastname,rank,association,id_number , password)
    print(f"{user2.fullname} \n{user2.rank}\n{user2.association}\n{user2._id}")
except (FileNotFoundError , NotImplementedError):
    user2 = SignUp(firstname, lastname,rank,association)
    print(f"{user2.fullname} \n{user2.rank}\n{user2.association}\n{user2._id}")
