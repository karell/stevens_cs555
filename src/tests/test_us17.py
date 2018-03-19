import unittest
import sys
sys.path.append('../')
sys.argv.append("../inputB.ged")

import family_relationships
import individual
import family

class Test_marriageToDecendants(unittest.TestCase):

    def test_MarriageToChild(self):
        mom = individual.Individual()
        mom.id = "1"
        dad = individual.Individual()
        dad.id = "2"
        dad.spouse = ["1"]
        mom.spouse = ["2", "3"]
        child = individual.Individual()
        child.id = "3"
        child.spouse = ["1"]
        newFamily = family.Family()
        newFamily.id = "F1"
        newFamily.children = ["3"]
        newFamily.husbandId = "1"
        newFamily.wifeId = "2"

        familyDic = {}
        familyDic["F1"] = newFamily
        individualDic = {}
        individualDic[mom.id] = mom
        individualDic[dad.id] = dad
        individualDic[child.id] = child

        self.assertFalse(family_relationships.validParentDecendantMarriages(familyDic,individualDic))
    
    def test_NoMarriageToChild(self):
        mom = individual.Individual()
        mom.id = "1"
        dad = individual.Individual()
        dad.id = "2"
        dad.spouse = ["1"]
        mom.spouse = ["2"]
        child = individual.Individual()
        child.id = "3"
        newFamily = family.Family()
        newFamily.id = "F1"
        newFamily.children = ["3"]
        newFamily.husbandId = "1"
        newFamily.wifeId = "2"

        familyDic = {}
        familyDic["F1"] = newFamily
        individualDic = {}
        individualDic[mom.id] = mom
        individualDic[dad.id] = dad
        individualDic[child.id] = child

        self.assertTrue(family_relationships.validParentDecendantMarriages(familyDic,individualDic))

if __name__ == "__main__":
        if len(sys.argv) != 2:
                sys.exit("ERROR need GEDCOM file on command line")
        command_line = sys.argv[1]
        del sys.argv[1:]
        unittest.main()
        