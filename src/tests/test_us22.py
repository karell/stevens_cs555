import unittest
import sys


sys.path.append('../')
sys.argv.append("../inputA.ged")
import unique_record_id

import individual
import family

class Test_uniqueRecords(unittest.TestCase):

    def test_IndividualIdExists(self):
        newPerson = individual.Individual()
        newPerson.id = "123"
        newPerson2 = individual.Individual()
        newPerson2.id = "123"
        individualDic = {}
        individualDic[newPerson.id] = newPerson
        self.assertFalse(unique_record_id.isUniqueRecordId(newPerson2.id, individualDic))
    
    def test_FamilyIdExists(self):
        newFamily = family.Family()
        newFamily.id = "123"
        newFamily2 = family.Family()
        newFamily2.id = "123"
        familyDic = {}
        familyDic[newFamily.id] = newFamily
        self.assertFalse(unique_record_id.isUniqueRecordId(newFamily2.id, familyDic))

    def test_IndividualIdAvailable(self):
        newPerson = individual.Individual()
        newPerson.id = "123"
        individualDic = {}
        self.assertTrue(unique_record_id.isUniqueRecordId(newPerson.id, individualDic))

    def test_FamilyIdAvailable(self):
        newFamily = family.Family()
        newFamily.id = "123"
        familyDic = {}
        self.assertTrue(unique_record_id.isUniqueRecordId(newFamily.id, familyDic))

    def test_IndividualAddedAndRemoved(self):
        newPerson = individual.Individual()
        newPerson.id = "123"
        individualDic = {}
        individualDic[newPerson.id] = newPerson
        individualDic.clear()
        self.assertTrue(unique_record_id.isUniqueRecordId(newPerson.id, individualDic))

    def test_FamilyAddedAndRemoved(self):
        newFamily = family.Family()
        newFamily.id = "123"
        familyDic = {}
        familyDic[newFamily.id] = newFamily
        familyDic.clear()
        self.assertTrue(unique_record_id.isUniqueRecordId(newFamily.id, familyDic))


if __name__ == "__main__":
        del sys.argv[1:]
        unittest.main()