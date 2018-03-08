import unittest
import sys
sys.path.append('../')
import individual
import family
import datetime
import gedcom_parser
'''
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

##US05
class TestMarriageBeforeDeath(unittest.TestCase):
    def test_marriageDateNone(self):
        husband = individual.Individual()
        wife = individual.Individual()
        myFamily = family.Family()
        husband.deathDate =  datetime.date(2000,2,1)
        wife.deathDate =  datetime.date(2000,2,1)
        self.assertTrue(myFamily.marriageBeforeDeath(husband.deathDate,wife.deathDate))

    def test_husbandWifeAlive(self):
        myFamily = family.Family()
        myFamily.marriageDate = datetime.date(2000,1,1)
        self.assertTrue(myFamily.marriageBeforeDeath(None,None))

    def test_marriageBeforeDeathWifeAlive(self):
        husband = individual.Individual()
        myFamily = family.Family()
        myFamily.marriageDate = datetime.date(2000,1,1)
        husband.deathDate =  datetime.date(2000,2,1)
        self.assertTrue(myFamily.marriageBeforeDeath(husband.deathDate,None))
    
    def test_marriageBeforeDeathHusbandAlive(self):
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.marriageDate = datetime.date(2000,1,1)
        wife.deathDate =  datetime.date(2000,2,1)
        self.assertTrue(myFamily.marriageBeforeDeath(None,wife.deathDate))

    def test_marriageBeforeDeath(self):
        husband = individual.Individual()
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.marriageDate = datetime.date(2000,1,1)
        wife.deathDate =  datetime.date(2000,2,1)
        husband.deathDate =  datetime.date(2000,2,1)
        self.assertTrue(myFamily.marriageBeforeDeath(husband.deathDate,wife.deathDate))
    
    def test_marriageAfterDeathHusbandAlive(self):
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.marriageDate = datetime.date(2000,1,1)
        wife.deathDate =  datetime.date(1999,2,1)
        self.assertFalse(myFamily.marriageBeforeDeath(None,wife.deathDate))
    
    def test_marriageAfterDeathWifeAlive(self):
        husband = individual.Individual()
        myFamily = family.Family()
        myFamily.marriageDate = datetime.date(2000,1,1)
        husband.deathDate =  datetime.date(1999,2,1)
        self.assertFalse(myFamily.marriageBeforeDeath(husband.deathDate,None))

    def test_marriageAfterDeathHusband(self):
        husband = individual.Individual()
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.marriageDate = datetime.date(2000,1,1)
        husband.deathDate =  datetime.date(1999,2,1)
        wife.deathDate =  datetime.date(2000,2,1)
        self.assertFalse(myFamily.marriageBeforeDeath(husband.deathDate,wife.deathDate))

    def test_marriageAfterDeathWife(self):
        husband = individual.Individual()
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.marriageDate = datetime.date(2000,1,1)
        husband.deathDate =  datetime.date(2001,2,1)
        wife.deathDate =  datetime.date(1999,2,1)
        self.assertFalse(myFamily.marriageBeforeDeath(husband.deathDate,wife.deathDate))
    
    def test_marriageAfterDeathBoth(self):
        husband = individual.Individual()
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.marriageDate = datetime.date(2000,1,1)
        husband.deathDate =  datetime.date(1999,2,1)
        wife.deathDate =  datetime.date(1999,2,1)
        self.assertFalse(myFamily.marriageBeforeDeath(husband.deathDate,wife.deathDate))


##US06
class TestDivorceBeforeDeath(unittest.TestCase):
    def test_divorceNone(self):
        husband = individual.Individual()
        wife = individual.Individual()
        myFamily = family.Family()
        husband.deathDate =  datetime.date(2001,2,1)
        wife.deathDate =  datetime.date(2001,2,1)
        self.assertTrue(myFamily.divorceBeforeDeath(husband.deathDate,wife.deathDate))

    def test_divorceHusbandAlive(self):
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.divorceDate = datetime.date(2000,1,1)
        wife.deathDate =  datetime.date(2001,2,1)
        self.assertTrue(myFamily.divorceBeforeDeath(None,wife.deathDate))
    
    def test_divorceWifeAlive(self):
        husband = individual.Individual()
        myFamily = family.Family()
        myFamily.divorcedDate = datetime.date(2000,1,1)
        husband.deathDate =  datetime.date(2001,2,1)
        self.assertTrue(myFamily.divorceBeforeDeath(husband.deathDate,None))
    
    def test_divorceBothAlive(self):
        myFamily = family.Family()
        myFamily.divorcedDate = datetime.date(2000,1,1)
        self.assertTrue(myFamily.divorceBeforeDeath(None,None))

    def test_divorceBothDead(self):
        husband = individual.Individual()
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.divorcedDate = datetime.date(2000,1,1)
        husband.deathDate =  datetime.date(2001,2,1)
        wife.deathDate =  datetime.date(2001,2,1)
        self.assertTrue(myFamily.divorceBeforeDeath(husband.deathDate,wife.deathDate))
    
    def test_divorceHusbandAlive2(self):
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.divorcedDate = datetime.date(2000,1,1)
        wife.deathDate =  datetime.date(1999,2,1)
        self.assertFalse(myFamily.divorceBeforeDeath(None,wife.deathDate))
    
    def test_divorceWifeAlive2(self):
        husband = individual.Individual()
        myFamily = family.Family()
        myFamily.divorcedDate = datetime.date(2000,1,1)
        husband.deathDate =  datetime.date(1999,2,1)
        self.assertFalse(myFamily.divorceBeforeDeath(husband.deathDate,None))

    def test_divorceAfterDeathWife(self):
        husband = individual.Individual()
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.divorcedDate = datetime.date(2000,1,1)
        husband.deathDate =  datetime.date(1999,2,1)
        wife.deathDate =  datetime.date(2001,2,1)
        self.assertFalse(myFamily.divorceBeforeDeath(husband.deathDate,wife.deathDate))

    def test_divorceAfterDeathHusband(self):
        husband = individual.Individual()
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.divorcedDate = datetime.date(2000,1,1)
        husband.deathDate =  datetime.date(2001,2,1)
        wife.deathDate =  datetime.date(1999,2,1)
        self.assertFalse(myFamily.divorceBeforeDeath(husband.deathDate,wife.deathDate))
    
    def test_divorceAfterDeathBoth(self):
        husband = individual.Individual()
        wife = individual.Individual()
        myFamily = family.Family()
        myFamily.divorcedDate = datetime.date(2000,1,1)
        husband.deathDate =  datetime.date(1999,2,1)
        wife.deathDate =  datetime.date(1999,2,1)
        self.assertFalse(myFamily.divorceBeforeDeath(husband.deathDate,wife.deathDate))
'''
#US 14
class testFiveSiblings(unittest.TestCase):
    def test_allFivearedifferentDates(self):
        date1 = datetime.date(1990,1,1)
        date2 = datetime.date(1991,1,1)
        date3 = datetime.date(1992,1,1)
        date4 = datetime.date(1993,1,1)
        date5 = datetime.date(1994,1,1)
        date6 = datetime.date(1995,1,1)
        siblingsDates = (date1,date2,date3,date4,date5,date6)
        self.assertTrue(gedcom_parser.verifySiblingsDates(siblingsDates))

    def test_someDifferentDates(self):
        date1 = datetime.date(1990,1,1)
        date2 = datetime.date(1990,1,1)
        date3 = datetime.date(1990,1,1)
        date4 = datetime.date(1993,1,1)
        date5 = datetime.date(1994,1,1)
        date6 = datetime.date(1995,1,1)
        siblingsDates = (date1,date2,date3,date4,date5,date6)
        self.assertTrue(gedcom_parser.verifySiblingsDates(siblingsDates))

    def test_allSameDates(self):
        date1 = datetime.date(1990,1,1)
        date2 = datetime.date(1990,1,1)
        date3 = datetime.date(1990,1,1)
        date4 = datetime.date(1990,1,1)
        date5 = datetime.date(1990,1,1)
        date6 = datetime.date(1990,1,1)
        siblingsDates = (date1,date2,date3,date4,date5,date6)
        self.assertFalse(gedcom_parser.verifySiblingsDates(siblingsDates))
    
    def test_someWithDayDifference(self):
        date1 = datetime.date(1990,1,2)
        date2 = datetime.date(1990,1,1)
        date3 = datetime.date(1990,1,2)
        date4 = datetime.date(1990,1,1)
        date5 = datetime.date(1990,1,1)
        date6 = datetime.date(1990,1,1)
        siblingsDates = (date1,date2,date3,date4,date5,date6)
        self.assertFalse(gedcom_parser.verifySiblingsDates(siblingsDates))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("ERROR need GEDCOM file on command line")
    command_line = sys.argv[1]
    del sys.argv[1:]
    unittest.main()
        