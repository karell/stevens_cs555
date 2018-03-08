import unittest
import sys
sys.path.append('../')
import individual
import family
import datetime
import gedcom_parser

##US01 test cases
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
        tmpDate = datetime.datetime.now()
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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("ERROR need GEDCOM file on command line")
    command_line = sys.argv[1]
    del sys.argv[1:]
    unittest.main()