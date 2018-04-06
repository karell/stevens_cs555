import unittest
import sys
sys.path.append('../')
sys.argv.append("../inputB.ged")

import family_relationships
import individual
import family

class Test_uniqueFamilyBySpouses(unittest.TestCase):

    def test_DuplicateFamilyRecords(self):

        newFamily = family.Family()
        newFamily.id = "F1"
        newFamily.husbandId = "1"
        newFamily.husbandName = "BILL SMITH"
        newFamily.wifeId = "2"
        newFamily.wifeName = "SARA DOE"
        newFamily.marriageDateStr = "1/1/2000"

        newFamily2 = family.Family()
        newFamily2.id = "F1"
        newFamily2.husbandId = "1"
        newFamily2.husbandName = "BILL SMITH"
        newFamily2.wifeId = "2"
        newFamily2.wifeName = "SARA DOE"
        newFamily2.marriageDateStr = "1/1/2000"

        familyDic = {}
        familyDic["F1"] = newFamily
        familyDic["F2"] = newFamily2

        self.assertFalse(family_relationships.uniqueFamilyBySpouses(familyDic))

    def test_UniqueFamilyRecordsYear(self):

        newFamily = family.Family()
        newFamily.id = "F1"
        newFamily.husbandId = "1"
        newFamily.husbandName = "BILL SMITH"
        newFamily.wifeId = "2"
        newFamily.wifeName = "SARA DOE"
        newFamily.marriageDateStr = "1/1/2000"

        newFamily2 = family.Family()
        newFamily2.id = "F1"
        newFamily2.husbandId = "1"
        newFamily2.husbandName = "BILL SMITH"
        newFamily2.wifeId = "2"
        newFamily2.wifeName = "SARA DOE"
        newFamily2.marriageDateStr = "1/1/2002"

        familyDic = {}
        familyDic["F1"] = newFamily
        familyDic["F2"] = newFamily2

        self.assertTrue(family_relationships.uniqueFamilyBySpouses(familyDic))
    
    def test_UniqueFamilyRecordsHusband(self):

        newFamily = family.Family()
        newFamily.id = "F1"
        newFamily.husbandId = "1"
        newFamily.husbandName = "JOHN SMITH"
        newFamily.wifeId = "2"
        newFamily.wifeName = "SARA DOE"
        newFamily.marriageDateStr = "1/1/2000"

        newFamily2 = family.Family()
        newFamily2.id = "F1"
        newFamily2.husbandId = "1"
        newFamily2.husbandName = "BILL SMITH"
        newFamily2.wifeId = "2"
        newFamily2.wifeName = "SARA DOE"
        newFamily2.marriageDateStr = "1/1/2002"

        familyDic = {}
        familyDic["F1"] = newFamily
        familyDic["F2"] = newFamily2

        self.assertTrue(family_relationships.uniqueFamilyBySpouses(familyDic))

if __name__ == "__main__":
        if len(sys.argv) != 2:
                sys.exit("ERROR need GEDCOM file on command line")
        command_line = sys.argv[1]
        del sys.argv[1:]
        unittest.main()
        