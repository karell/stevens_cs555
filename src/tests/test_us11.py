'''
Created on Mar 22, 2018

@author: esther
'''
import unittest
import sys
sys.path.append('../')
import individual
import family
import datetime
from bigamy import is_bigamy


class TestNoBigamy(unittest.TestCase):
    def test_bigamyTrue(self):
        individual_dict = {}
        husband = individual.Individual()
        husband.id = "H1"
        husband.birthDate = datetime.datetime(1980,1,1)
        husband.firstAndMiddleName = "John James"
        husband.lastname = "Jamison"
        husband.spouse = ["W2", "W1"]
        husband.familyIdSpouse  = "F1"
        individual_dict.__setitem__(husband.id, husband)

        wife1 = individual.Individual()
        wife1.id = "W1"
        wife1.firstAndMiddleName = "Jane Janet"
        wife1.lastname = "Jamison"
        wife1.familyIdSpouse = "F1"
        wife1.birthDate = datetime.datetime(1981,1,1)

        individual_dict.__setitem__(wife1.id, wife1)
        
        wife2 = individual.Individual()
        wife2.id = "W2"
        wife2.firstAndMiddleName = "Mary Ann"
        wife2.lastname = "Jamison"
        wife2.familyIdSpouse = "F2"
        wife2.birthDate = datetime.datetime(1980,1,1)
        individual_dict.__setitem__(wife2.id, wife2)

        familyF1 = family.Family()
        familyF1.id = "F1"
        familyF1.marriageDate = datetime.datetime(2000,1,1)        
        familyF1.husbandId = husband.id
        familyF1.wifeId = wife1.id

        familyF2 = family.Family()
        familyF2.id = "F2"
        familyF2.marriageDate = datetime.datetime(2005,10,1)    
        familyF2.husbandId = husband.id
        familyF2.wifeId = wife2.id

        families_dict = {}
        families_dict[familyF1.id] = familyF1
        families_dict[familyF2.id] = familyF2

        self.assertTrue(is_bigamy(husband, families_dict, individual_dict))

        
    def test_bigamyFalse(self):
        individual_dict = {}
        husband = individual.Individual()
        husband.id = "H1"
        husband.firstAndMiddleName = "John James"
        husband.lastname = "Jamison"
        husband.birthDate = datetime.datetime(1980,1,1)
        husband.familyIdSpouse = "F2"
        husband.spouse = ["W2", "W1"]
        individual_dict[husband.id] = husband

        wife1 = individual.Individual()
        wife1.id = "W1"
        wife1.firstAndMiddleName = "Jane Janet"
        wife1.lastname = "Jamison"
        wife1.familyIdSpouse = "F1"
        wife1.birthDate = datetime.datetime(1981,1,1)
        individual_dict.__setitem__(wife1.id, wife1)
        
        wife2 = individual.Individual()
        wife2.id = "W2"
        wife2.firstAndMiddleName = "Mary Ann"
        wife2.lastname = "Jamison"
        wife2.familyIdSpouse = "F2"
        wife2.birthDate = datetime.datetime(1980,1,1)
        individual_dict.__setitem__(wife2.id, wife2)

        familyF1 = family.Family()
        familyF1.id = "F1"
        familyF1.marriageDate = datetime.datetime(2000,1,1)
        familyF1.divorcedDate= datetime.datetime(2002,7,7)       
        familyF1.husbandId = husband.id
        familyF1.wifeId = wife1.id

        familyF2 = family.Family()
        familyF2.id = "F2"
        familyF2.marriageDate = datetime.datetime(2005,10,1)    
        familyF2.husbandId = husband.id
        familyF2.wifeId = wife2.id

        families_dict = {}
        families_dict[familyF1.id] = familyF1
        families_dict[familyF2.id] = familyF2


        self.assertFalse(is_bigamy(husband, families_dict, individual_dict))



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()