import unittest
import individual
import sys
from datetime import date
from datetime import datetime
from datetime import timedelta

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


if __name__ == "__main__":
        if len(sys.argv) != 2:
                sys.exit("ERROR need GEDCOM file on command line")
        command_line = sys.argv[1]
        del sys.argv[1:]
        unittest.main()
        