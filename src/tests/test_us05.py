import unittest
import sys
sys.path.append('../')
import individual
import family
import datetime
import gedcom_parser

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

        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("ERROR need GEDCOM file on command line")
    command_line = sys.argv[1]
    del sys.argv[1:]
    unittest.main()