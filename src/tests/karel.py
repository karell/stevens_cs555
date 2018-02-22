import unittest
import individual
import family
import sys

import datetime

##US01 test cases HW04
class TestDatesBeforeCurrent(unittest.TestCase):

    def test_BornTomorrow(self):
        testIndividual = individual.Individual()
        tmpDate = datetime.today()
        tmpDate += timedelta(days=1)
        testIndividual.birthDate =  tmpDate
        result = individual.compareDates(testIndividual.birthDate)
        self.assertTrue(result, True)

    def test_BornYesterday(self):
        testIndividual = individual.Individual()
        tmpDate = datetime.today()
        tmpDate += timedelta(days=-1)
        testIndividual.birthDate =  tmpDate
        result = individual.compareDates(testIndividual.birthDate)
        self.assertFalse(result, True)

    def test_BornToday(self):
        testIndividual = individual.Individual()
        tmpDate = datetime.today()
        testIndividual.birthDate =  tmpDate
        result = individual.compareDates(testIndividual.birthDate)
        self.assertTrue(result, True)

    def test_dieNextYear(self):
        testIndividual = individual.Individual()
        tmpDate = datetime.today()
        tmpDate += timedelta(days=365)
        testIndividual.deathDate = tmpDate
        result = individual.compareDates(testIndividual.deathDate)
        self.assertTrue(result, True)
    
    def test_dieLastYear(self):
        testIndividual = individual.Individual()
        tmpDate = datetime.today()
        tmpDate += timedelta(days=-365)
        testIndividual.deathDate = tmpDate
        result = individual.compareDates(testIndividual.deathDate)
        self.assertFalse(result, True)

##US05
class TestMarriageBeforeDeath(unittest.TestCase):
    def test_marriageBeforeDeath(self):
        husband = individual.Individual()
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.marriageDate = datetime.date(2000,1,1)

        husband.deathDate =  datetime.date(2000,2,1)
        wife.deathDate =  datetime.date(2000,2,1)
        self.assertTrue(myFamily.marriageBeforeDeath(husband.deathDate,wife.deathDate))
    
    def test_marriageAfterDeath(self):
        husband = individual.Individual()
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.marriageDate = datetime.date(2000,1,1)

        husband.deathDate =  datetime.date(1999,2,1)
        wife.deathDate =  datetime.date(2000,2,1)
        self.assertFalse(myFamily.marriageBeforeDeath(husband.deathDate,wife.deathDate))

if __name__ == "__main__":
        unittest.main()
        