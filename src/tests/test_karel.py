import unittest
import sys
sys.path.append('../')
import individual
import family
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

if __name__ == "__main__":
        unittest.main()
        