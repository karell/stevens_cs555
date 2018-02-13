import sys
import unittest
import datetime

sys.path.append('../')
import individual
import gedcom_parser

##US 22 testcases
class isUniqueRecordIdTest(unittest.TestCase):

    def test_IndividualIdExists(self):
        newPerson = individual.Individual()
        newPerson.id = "123"
        newPerson2 = individual.Individual()
        newPerson2.id = "123"
        individualDic = {}
        individualDic[newPerson.id] = newPerson
        self.assertFalse(gedcom_parser.isUniqueRecordId(newPerson2.id, individualDic))
    
    def test_FamilyIdExists(self):
        newFamily = individual.Individual()
        newFamily.id = "123"
        newFamily2 = individual.Individual()
        newFamily2.id = "123"
        familyDic = {}
        familyDic[newFamily.id] = newFamily
        self.assertFalse(gedcom_parser.isUniqueRecordId(newFamily2.id, familyDic))

    def test_IndividualIdAvailable(self):
        newPerson = individual.Individual()
        newPerson.id = "123"
        individualDic = {}
        self.assertTrue(gedcom_parser.isUniqueRecordId(newPerson.id, individualDic))

    def test_FamilyIdAvailable(self):
        newFamily = individual.Individual()
        newFamily.id = "123"
        familyDic = {}
        self.assertTrue(gedcom_parser.isUniqueRecordId(newFamily.id, familyDic))

    def test_IndividualAddedAndRemoved(self):
        newPerson = individual.Individual()
        newPerson.id = "123"
        individualDic = {}
        individualDic[newPerson.id] = newPerson
        individualDic.clear()
        self.assertTrue(gedcom_parser.isUniqueRecordId(newPerson.id, individualDic))

    def test_FamilyAddedAndRemoved(self):
        newFamily = individual.Individual()
        newFamily.id = "123"
        familyDic = {}
        familyDic[newFamily.id] = newFamily
        familyDic.clear()
        self.assertTrue(gedcom_parser.isUniqueRecordId(newFamily.id, familyDic))
        
if __name__ == "__main__":
        if len(sys.argv) != 2:
                sys.exit("Need GEDCOM Argument")
        command_line = sys.argv[1]
        del sys.argv[1:]
        unittest.main()
        