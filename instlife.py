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
        self.name = randomName(self.nationality, self.sex)
        if self.npc == True:
            #Call random gen functions here
            None
        else:
            self.age = 0
            self.occupation = None
            self.education = None
            self.criminal_record = None
            self.parents = generateParents(self.nationality)
            self.finance = None
        return True
        
def randomNationality():
    nationalities = ["American", "Mexican", "Canadian", "British", "Irish", "Spanish", "German", "Swedish", "Finnish", "Dutch", "Italian"]
    return nationalities[random.randint(0, len(nationalities) - 1)]
    
def randomName(nationality, sex):
    m_american = ["Noah", "Liam", "William", "Mason", "James", "Benjamin", "Jacob", "Elijah", "Michael", "Ethan", "Timothy", "Kyle", "David"]
    f_american = ["Emma", "Olivia", "Ava", "Sophia", "Isabella", "Mia", "Charlotte", "Abigail", "Emily", "Harper", "Starlow", "Elizabeth", "Ethel"]
    m_mexican = ["José", "Juan", "Miguel", "Francisco", "Jesús", "Antonio", "Alejandro", "Pedro", "Carlos", "Jorge", "Victor"]
    # TODO
    if nationality == "American":
        if sex == "m":
            return m_american[random.randint(1, len(m_american) - 1)]
        elif sex == "f":
            return f_american[random.randint(1, len(f_american) - 1)]
    elif nationality == "Mexican":
        if sex == "m":
            return m_mexican[random.randint(1, len(m_american) - 1)]
        elif sex == "f":
            return f_american[random.randint(1, len(f_american) - 1)] # Placeholder
def randomSex():
    if randint(0, 1) == 1:
        return "m"
    return "f"
def generateParents(nationality):
    mother = Person(True, True, None, None, None, None, None, None, None, None, None) # Will incorportate finances and occupation later
