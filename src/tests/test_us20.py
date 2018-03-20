import unittest
import sys
sys.path.append('../')
sys.argv.append("../inputB.ged")

import family_relationships
import individual
import family

class Test_marriageOfUnclesAuntsToNieceNephews(unittest.TestCase):

    def test_MarriageToSiblingChild(self):
        mom = individual.Individual()
        mom.id = "1"
        dad = individual.Individual()
        dad.id = "2"
        dad.spouse = ["1"]
        mom.spouse = ["2"]

        child = individual.Individual()
        child.id = "3"
        child.children = ["5"]
        
        child2 = individual.Individual()
        child2.id = "4"
        child2.spouse = ["5"]

        neice = individual.Individual()
        neice.id = "5"
        neice.spouse = ["4"]

        newFamily = family.Family()
        newFamily.id = "F1"
        newFamily.children = ["3", "4"]
        newFamily.husbandId = "1"
        newFamily.wifeId = "2"

        familyDic = {}
        familyDic["F1"] = newFamily
        individualDic = {}
        individualDic[mom.id] = mom
        individualDic[dad.id] = dad
        individualDic[child.id] = child
        individualDic[child2.id] = child2
        individualDic[neice.id] = neice

        self.assertFalse(family_relationships.validUncleAuntMarriages(familyDic,individualDic))

if __name__ == "__main__":
        if len(sys.argv) != 2:
                sys.exit("ERROR need GEDCOM file on command line")
        command_line = sys.argv[1]
        del sys.argv[1:]
        unittest.main()
        