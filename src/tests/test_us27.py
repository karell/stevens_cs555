'''
Created on Feb 26, 2018

@author: esther
'''
import sys
import unittest

from datetime import date

sys.path.append('../')
sys.argv.append("../inputA.ged")
import individual




##US 27 testcases 
class TestAgeCalculation(unittest.TestCase):
#Mother should be less than 60 years older than her children and father should be less than 80 years older than his children
          

      
    def test_BornTodayAgeEquals0(self):
        testPerson = individual.Individual()
        testPerson.birthDate = date.today()
        individual.Individual.calculateAge(testPerson)
        result = testPerson.age
        self.assertEqual(int(result), 0)
        
    def test_TwoHundred(self):
        testPerson = individual.Individual()
        testPerson.birthDate = date(1736, 12, 1)
        testPerson.deathDate = date(1936, 12, 1)
        individual.Individual.calculateAge(testPerson)
        result = testPerson.age
        self.assertEqual(int(result), 200)
                
    def test_SeventyFive(self):
        testPerson = individual.Individual()
        testPerson.birthDate = date(1736, 12, 1)
        testPerson.deathDate = date(1811, 12, 1)
        individual.Individual.calculateAge(testPerson)
        result = int(testPerson.age)
        self.assertEqual(result, 75)

    def test_AliveAndTwentyFive(self):
        testPerson = individual.Individual()
        testPerson.birthDate = date(1993, 2, 1)
        individual.Individual.calculateAge(testPerson)
        result = int(testPerson.age)
        self.assertEqual(result, 25)
        

if __name__ == "__main__":
        if len(sys.argv) != 2:
                sys.exit("ERROR need GEDCOM file on command line")
        command_line = sys.argv[1]
        del sys.argv[1:]
        unittest.main()
        