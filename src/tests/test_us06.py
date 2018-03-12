import unittest
import sys
sys.path.append('../')
import individual
import family
import datetime


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
    if len(sys.argv) != 2:
        sys.exit("ERROR need GEDCOM file on command line")
    command_line = sys.argv[1]
    del sys.argv[1:]
    unittest.main()