from textuilib3 import menu, menuItem, clear, setHeader
import os
import sys
import random

class Person:
    def __init__(self, npc, is_random, name, age, sex, nationality, occupation, education, criminal_record, parents, finance):
        if npc == True or is_random == True:
            self.is_random = True
            self.generate()
        else:
            self.npc = False
            self.is_random = False
            self.name = name
            self.age = age
            self.sex = sex
            self.nationality = nationality
            self.occupation = occupation
            self.education = education
            self.criminal_record = criminal_record
            self.parents = parents
            self.finance = finance
            
    def generate(self):
        if self.is_random != True:
            return False
        self.nationality = randomNationality()
        self.sex = randomSex()
        self.name = randomName(self.nationality)
        
def randomNationality():
    nationalities = ["American", "Mexican", "Canadian", "British", "Irish", "Spanish", "German", "Swedish", "Finnish", "Dutch", "Italian"]
    return nationalities[random.randint(0, len(nationalities) - 1]
    
def randomName(nationality, sex):
    m_american = ["Noah", "Liam", "William", "Mason", "James", "Benjamin", "Jacob", "Elijah", "Michael", "Ethan", "Timothy", "Kyle", "David"]
    f_american = ["Emma", "Olivia", "Ava", "Sophia", "Isabella", "Mia", "Charlotte", "Abigail", "Emily", "Harper", "Starlow", "Elizabeth", "Ethel"]
    m_mexican = ["José", "Juan", "Miguel", "Francisco", "Jesús", "Antonio", "Alejandro", "Pedro", "Carlos", "Jorge", "Victor"]
def randomSex():
    if randint(0, 1) == 1:
        return "m"
    return "f"
