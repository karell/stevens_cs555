import sys
import unittest
import datetime

sys.path.append('../')

import individual
import unique_individuals

def createIndividual1():
    # Individual 1: Charles Roseberry, 09/26/1941
    ind                    = individual.Individual()
    ind.firstAndMiddleName = 'Charles'
    ind.lastname           = 'Roseberry'
    ind.birthDate          = datetime.date(1941,9,26)

    return ind

def createIndividual2():
    # Individual 2: Charles Roseberry, 08/16/1966
    ind                    = individual.Individual()
    ind.firstAndMiddleName = 'Charles'
    ind.lastname           = 'Roseberry'
    ind.birthDate          = datetime.date(1966,8,16)

    return ind

def createIndividual3():
    # Individual 3: Thomas Roseberry, 08/16/1966
    ind                    = individual.Individual()
    ind.firstAndMiddleName = 'Thomas'
    ind.lastname           = 'Roseberry'
    ind.birthDate          = datetime.date(1966,8,16)

    return ind

class testUS23(unittest.TestCase):

    # Test that a ValueError exception is raised when the dictionary of
    # individuals is empty.
    def testNoEntries(self):
        individualsDict = {}

        with self.assertRaises(ValueError):
            unique_individuals.AreIndividualsUnique(individualsDict)

    # Test that a single entry in the individuals dictionary is considered
    # uniqueness.
    def testSingleEntry(self):
        individualsDict = {}

        individualsDict['@I01@'] = createIndividual1()
        
        self.assertTrue(unique_individuals.AreIndividualsUnique(individualsDict))

    # Test that two entries with same name, different birth dates are unique.
    def testTwoWithDifferentBirthDateSameNamesAreUnique(self):
        individualsDict = {}

        individualsDict['@I01@'] = createIndividual1()
        individualsDict['@I02@'] = createIndividual2()

        self.assertTrue(unique_individuals.AreIndividualsUnique(individualsDict))

    # Test that two identical entries are not unique.
    def testTwoIdenticalAreNotUnique(self):
        individualsDict = {}

        individualsDict['@I01@'] = createIndividual1()
        individualsDict['@I02@'] = createIndividual1() # double of Individual 1

        self.assertFalse(unique_individuals.AreIndividualsUnique(individualsDict))

    # Test that two entries with same birth date, different first names are unique.
    def testTwoWithSameBirthDateDifferentFirstNamesAreUnique(self):
        individualsDict = {}

        individualsDict['@I02@'] = createIndividual2()
        individualsDict['@I03@'] = createIndividual3()

        self.assertTrue(unique_individuals.AreIndividualsUnique(individualsDict))

    # Test that all three entries are unique.
    def testThreeUnique(self):
        individualsDict = {}

        individualsDict['@I01@'] = createIndividual1()
        individualsDict['@I02@'] = createIndividual2()
        individualsDict['@I03@'] = createIndividual3()

        self.assertTrue(unique_individuals.AreIndividualsUnique(individualsDict))

if __name__ == '__main__':
    unittest.main()

