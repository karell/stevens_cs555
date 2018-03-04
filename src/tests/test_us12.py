'''
Created on Feb 25, 2018

@author: esthe
'''
import unittest
import sys
import datetime


sys.path.append('../')
sys.argv.append("../inputA.ged")
import parents_not_to_old


class Test_AreParentsTooOld(unittest.TestCase):


    def test_motherAgeDiffToChildLessThan60(self):
        motherBirthdate = datetime.date(1945, 1, 12)
        childBirthdate = datetime.date(1975, 1, 12)
        result = parents_not_to_old.isValidMotherAge(childBirthdate, motherBirthdate)
        self.assertTrue(result, True)
    def test_fatherAgeDiffToChildLessThan80(self):
        motherBirthdate = datetime.date(1945, 1, 12)
        childBirthdate = datetime.date(1975, 1, 12)
        result = parents_not_to_old.isValidFatherAge(childBirthdate, motherBirthdate)
        self.assertTrue(result, True)
     
    def test_motherAgeDiffToChildMoreThan60(self):
        motherBirthdate = datetime.date(1945, 1, 12)
        childBirthdate = datetime.date(2006, 1, 12)
        result = parents_not_to_old.isValidMotherAge(childBirthdate, motherBirthdate)
        self.assertFalse(result)
        
    def test_fatherAgeDiffToChildMoreThan80(self):
        motherBirthdate = datetime.date(1945, 1, 12)
        childBirthdate = datetime.date(2026, 1, 12)
        result = parents_not_to_old.isValidFatherAge(childBirthdate, motherBirthdate)
        self.assertFalse(result)       


if __name__ == "__main__":
        if len(sys.argv) != 2:
                sys.exit("ERROR need GEDCOM file on command line")
        command_line = sys.argv[1]
        del sys.argv[1:]
        unittest.main()