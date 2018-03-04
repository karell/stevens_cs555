'''
Created on Feb 11, 2018

@author: esther
'''
import sys
import unittest
import datetime

sys.path.append('../')
sys.argv.append("../inputA.ged")
import family


##US 04 testcases
class isMarriedBeforeDivorceTest(unittest.TestCase):

    def test_MarriedBeforeDivorced(self):
        fam = family.Family()
        fam.marriageDate = datetime.date(2000,1,1)
        fam.divorcedDate = datetime.date(2005,1,1)
        self.assertTrue(fam.marriageBeforeDivorce())

    def test_DivorceDateNoMarriage(self):
        fam = family.Family()
        fam.divorcedDate = datetime.date(2005,1,1)
        self.assertFalse(fam.marriageBeforeDivorce())

    def test_NoDivorceDate(self):
        fam = family.Family()
        fam.marriageDate = datetime.date(2000,1,1)
        self.assertTrue(fam.marriageBeforeDivorce())

    def test_MarriedAfterDivorced(self):
        fam = family.Family()
        fam.marriageDate = datetime.date(2005,1,1)
        fam.divorcedDate = datetime.date(2000,1,1)
        self.assertFalse(fam.marriageBeforeDivorce())
        

if __name__ == "__main__":
        if len(sys.argv) != 2:
                sys.exit("ERROR need GEDCOM file on command line")
        command_line = sys.argv[1]
        del sys.argv[1:]
        unittest.main()
