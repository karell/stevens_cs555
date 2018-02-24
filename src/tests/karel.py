import unittest
import individual
import family
import sys

import datetime

##US01 test cases HW04
class TestDatesBeforeCurrent(unittest.TestCase):

    def test_BornTomorrow(self):
        testIndividual = individual.Individual()
        tmpDate = datetime.datetime.today()
        tmpDate += datetime.timedelta(days=1)
        testIndividual.birthDate =  tmpDate
        result = individual.compareDates(testIndividual.birthDate)
        self.assertTrue(result)

    def test_BornYesterday(self):
        testIndividual = individual.Individual()
        tmpDate = datetime.datetime.today()
        tmpDate += datetime.timedelta(days=-1)
        testIndividual.birthDate =  tmpDate
        result = individual.compareDates(testIndividual.birthDate)
        self.assertFalse(result)

    def test_BornToday(self):
        testIndividual = individual.Individual()
        tmpDate = datetime.datetime.today()
        testIndividual.birthDate =  tmpDate
        result = individual.compareDates(testIndividual.birthDate)
        self.assertFalse(result)

    def test_dieNextYear(self):
        testIndividual = individual.Individual()
        tmpDate = datetime.datetime.today()
        tmpDate += datetime.timedelta(days=365)
        testIndividual.deathDate = tmpDate
        result = individual.compareDates(testIndividual.deathDate)
        self.assertTrue(result)
    
    def test_dieLastYear(self):
        testIndividual = individual.Individual()
        tmpDate = datetime.datetime.today()
        tmpDate += datetime.timedelta(days=-365)
        testIndividual.deathDate = tmpDate
        result = individual.compareDates(testIndividual.deathDate)
        self.assertFalse(result)

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

##US06
class TestDivorceBeforeDeath(unittest.TestCase):
    def test_divorcecBeforeDeath(self):
        husband = individual.Individual()
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.divorceDate = datetime.date(2000,1,1)

        husband.deathDate =  datetime.date(2001,2,1)
        wife.deathDate =  datetime.date(2001,2,1)
        self.assertTrue(myFamily.divorceBeforeDeath(husband.deathDate,wife.deathDate))

    def test_divorcecAfterDeath(self):
        husband = individual.Individual()
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.divorcedDate = datetime.date(2000,1,1)

        husband.deathDate =  datetime.date(1999,2,1)
        wife.deathDate =  datetime.date(2001,2,1)
        self.assertFalse(myFamily.divorceBeforeDeath(husband.deathDate,wife.deathDate))

if __name__ == "__main__":
        unittest.main()
        