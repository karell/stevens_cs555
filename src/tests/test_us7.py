'''
Created on Feb 11, 2018

@author: esther
'''
import sys
import unittest


sys.path.append('../')
sys.argv.append("../inputA.ged")
import individual




##US 7 testcases HW04
class TestAgeLessThan150(unittest.TestCase):
#Mother should be less than 60 years older than her children and father should be less than 80 years older than his children
          

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
        testPerson.age = 0
        result = individual.Individual.isAgeLessThan150(testPerson)
        self.assertTrue(result, True)
        
    def test_TwoHundred(self):
        testPerson = individual.Individual()
        testPerson.age = 200
        result = individual.Individual.isAgeLessThan150(testPerson)
        self.assertFalse(result)
                
    def test_SeventyFive(self):
        testPerson = individual.Individual()
        testPerson.age = 75
        result = individual.Individual.isAgeLessThan150(testPerson)
        self.assertTrue(result, True)
        

if __name__ == "__main__":
        if len(sys.argv) != 2:
                sys.exit("ERROR need GEDCOM file on command line")
        command_line = sys.argv[1]
        del sys.argv[1:]
        unittest.main()
        