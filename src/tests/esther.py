'''
Created on Feb 11, 2018

@author: esther
'''
import unittest
import individual
import sys
from datetime import date

##US 7 testcases HW04
class TestAgeLessThan150(unittest.TestCase):

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
        