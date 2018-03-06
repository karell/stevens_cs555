import unittest
import datetime
import sys

sys.path.append('../')
sys.argv.append("../inputA.ged")
import corresponding_records
import individual
import family

# -----------------------------------------------------------------------------
# User Story #26: All family roles (spouse, child) specified in an individual record 
# should have corresponding entries in the corresponding family records. Likewise, 
# all individual roles (spouse, child) specified in family records should have corresponding 
# entries in the corresponding  individual's records.  I.e. the information in the 
# individual and family records should be consistent.
# -----------------------------------------------------------------------------

class Test_CorrespondingEntries(unittest.TestCase):

    def test_FamilyChildDoesNotExist(self):
        fam = family.Family()
        fam.id = "@FAM"
        fam.children.append("@testchild")
        famDict = {}
        famDict[fam.id] = fam
        individualDict = {}
        self.assertFalse(corresponding_records.validateCorrespondingRecords(individualDict,famDict))
    def test_IndividualNotInFamily(self):
        fam = family.Family()
        fam.id = "@FAM"
        fam.children.append("@testchild")
        famDict = {}
        famDict[fam.id] = fam
        individualDict = {}
        indiv = individual.Individual()
        indiv.id = "@INDV"
        individualDict[indiv.id] = indiv
        self.assertFalse(corresponding_records.validateCorrespondingRecords(individualDict,famDict))
    def test_ChildNotInFamilyRecord(self):
        fam = family.Family()
        fam.id = "@FAM"
        fam.husbandId = "@INDV"
        fam.children.append("@testchild")
        famDict = {}
        famDict[fam.id] = fam
        individualDict = {}
        indiv = individual.Individual()
        indiv.id = "@INDV"
        indiv.children = ["@CHILD"]
        individualDict[indiv.id] = indiv
        self.assertFalse(corresponding_records.validateCorrespondingRecords(individualDict,famDict))

if __name__ == "__main__":
        if len(sys.argv) != 2:
                sys.exit("ERROR need GEDCOM file on command line")
        command_line = sys.argv[1]
        del sys.argv[1:]
        unittest.main()