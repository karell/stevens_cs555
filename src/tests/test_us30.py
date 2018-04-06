'''
Created on Apr 6, 2018

@author: esther
'''
import unittest
import sys
sys.path.append('../')
import individual
import family
import datetime
import create_list_individual_characteristic


class TestDeceasedList(unittest.TestCase):
    def test_listOnlyAliveMarriedTrue(self):
        individual_dict = {}
        person1 = individual.Individual()
        person1.id = "H1"
        person1.birthDate = datetime.datetime(1980,1,1)
        person1.firstAndMiddleName = "John James"
        person1.lastname = "Jamison"
        person1.spouse = ["W2"]
        person1.familyIdSpouse  = "F1"
        person1.alive = True
        individual_dict.__setitem__(person1.id, person1)

        person2 = individual.Individual()
        person2.id = "W1"
        person2.firstAndMiddleName = "Jane Janet"
        person2.lastname = "Jamison"
        person2.familyIdSpouse = "F1"
        person2.spouse = ["F1"]
        person2.birthDate = datetime.datetime(1981,1,1)
        person2.alive = True
       
        
        individual_dict.__setitem__(person2.id, person2)
        
        person3 = individual.Individual()
        person3.id = "W2"
        person3.firstAndMiddleName = "Mary Ann"
        person3.lastname = "Jamison"
        person3.familyIdSpouse = "F2"
        person3.spouse = ["F1"]
        person3.birthDate = datetime.datetime(1980,1,1)
        person3.alive = True
   
        individual_dict.__setitem__(person3.id, person3)

        testDict = create_list_individual_characteristic.listMarriedIndividuals(individual_dict)

        self.assertDictEqual(individual_dict, testDict)

    def test_listOnlyDeceaseSubset(self):
        individual_dict = {}
        person1 = individual.Individual()
        person1.id = "H1"
        person1.birthDate = datetime.datetime(1980,1,1)
        person1.firstAndMiddleName = "John James"
        person1.lastname = "Jamison"
        person1.spouse = ["W2"]
        person1.familyIdSpouse  = "F1"
        person1.alive = True
        individual_dict.__setitem__(person1.id, person1)

        person2 = individual.Individual()
        person2.id = "W1"
        person2.firstAndMiddleName = "Jane Janet"
        person2.lastname = "Jamison"
        person2.familyIdSpouse = "F1"
        person2.spouse = ["F1"]
        person2.birthDate = datetime.datetime(1981,1,1)
        person2.alive = True
       
        
        individual_dict.__setitem__(person2.id, person2)
        
        person3 = individual.Individual()
        person3.id = "W2"
        person3.firstAndMiddleName = "Mary Ann"
        person3.lastname = "Jamison"
        person3.birthDate = datetime.datetime(1980,1,1)
        person3.alive = True
   
        individual_dict.__setitem__(person3.id, person3)

        testDict = create_list_individual_characteristic.listMarriedIndividuals(individual_dict)

        self.assertDictContainsSubset(testDict, individual_dict)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()