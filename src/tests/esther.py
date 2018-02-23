'''
Created on Feb 11, 2018

@author: esther
'''
import sys
import unittest
import datetime
from datetime import date

sys.path.append('../')
import individual
import gedcom_parser
import parents_not_to_old



##US 7 testcases HW04
class TestAgeLessThan150(unittest.TestCase):
#Mother should be less than 60 years older than her children and father should be less than 80 years older than his children
    def test_motherAgeDiffToChildLessThan60(self):
        motherBirthdate = datetime.date(1945, 1, 12)
        childBirthdate = datetime.date(1975, 1, 12)
        result = parents_not_to_old.isValidMotherAge(childBirthdate, motherBirthdate)
        self.assertTrue(result, True)
        
    def test_fatherAgeDiffToChildLessThan80(self):
        motherBirthdate = datetime.date(1945, 1, 12)
        childBirthdate = datetime.date(1975, 1, 12)
        result = parents_not_to_old.isValidFatherAge(childBirthdate, motherBirthdate)
        self.assertTrue(result, True)
     
    def test_motherAgeDiffToChildMoreThan60(self):
        motherBirthdate = datetime.date(1945, 1, 12)
        childBirthdate = datetime.date(2006, 1, 12)
        result = parents_not_to_old.isValidMotherAge(childBirthdate, motherBirthdate)
        self.assertFalse(result)
        
    def test_fatherAgeDiffToChildMoreThan80(self):
        motherBirthdate = datetime.date(1945, 1, 12)
        childBirthdate = datetime.date(2026, 1, 12)
        result = parents_not_to_old.isValidFatherAge(childBirthdate, motherBirthdate)
        self.assertFalse(result)       
        

    def test_Equals149(self):
        testPerson = individual.Individual()
        testPerson.age = 149
        result = individual.Individual.isAgeLessThan150(testPerson)
        self.assertTrue(result, True)
        
    def test_GreaterThan150(self):
        testPerson = individual.Individual()
        testPerson.age = 151
        result = individual.Individual.isAgeLessThan150(testPerson)
        self.assertFalse(result, False)
        
    def test_BornToday(self):
        testPerson = individual.Individual()
        testPerson.birthDate = date.today()
        result = individual.Individual.calculateAge(testPerson)
        self.assertLess(result, True)
        
    def test_TwoHundred(self):
        testPerson = individual.Individual()
        testPerson.birthDate = date(1736, 12, 1)
        testPerson.deathDate = date(1936, 12, 1)
        result = individual.Individual.calculateAge(testPerson)
        self.assertFalse(result)
                
    def test_SeventyFive(self):
        testPerson = individual.Individual()
        testPerson.birthDate = date(1900, 12, 1)
        testPerson.deathDate = date(1975, 12, 1)
        result = individual.Individual.calculateAge(testPerson)
        self.assertTrue(result)
        

if __name__ == "__main__":
        if len(sys.argv) != 2:
                sys.exit("ERROR need GEDCOM file on command line")
        command_line = sys.argv[1]
        del sys.argv[1:]
        unittest.main()
        