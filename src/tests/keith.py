import sys
import unittest
import datetime

sys.path.append('../')

import individual
import unique_individuals
import family

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

def createMaleHusband():
    # Individual: Male Husband has male gender
    ind                    = individual.Individual()
    ind.gender             = 'M'
    ind.firstAndMiddleNAme = 'Male'
    ind.lastname           = 'Husband'

    return ind

def createFemaleHusband():
    # Individual: Female Husband has female gender
    ind                    = individual.Individual()
    ind.gender             = 'F'
    ind.firstAndMiddleNAme = 'Female'
    ind.lastname           = 'Husband'

    return ind

def createFemaleWife():
    # Individual: Female Wife has female gender
    ind                    = individual.Individual()
    ind.gender             = 'F'
    ind.firstAndMiddleNAme = 'Female'
    ind.lastname           = 'Wife'

    return ind

def createMaleWife():
    # Individual: Male Wife has male gender
    ind                    = individual.Individual()
    ind.gender             = 'M'
    ind.firstAndMiddleNAme = 'Male'
    ind.lastname           = 'Wife'

    return ind

# Class "testUS21" contains all the tests for User Story #21, which is to
# check that a husband's gender is male and a wife's gender is female.
class testUS21(unittest.TestCase):

    # Test that a Husband that is male passes the gender check.
    def testMaleHusband(self):
        individualsDict = {}

        individualsDict['@I01@'] = createMaleHusband()

        fam           = family.Family()
        fam.id        = '@F01@'
        fam.husbandId = '@I01@'

        self.assertTrue(fam.ValidateRoleGender(individualsDict))

    # Test that a Husband that is female fails the gender check.
    def testFemaleHusband(self):
        individualsDict = {}

        individualsDict['@I01@'] = createFemaleHusband()

        fam           = family.Family()
        fam.id        = '@F01@'
        fam.husbandId = '@I01@'

        self.assertFalse(fam.ValidateRoleGender(individualsDict))

    # Test that a Wife that is female passes the gender check.
    def testFemaleWife(self):
        individualsDict = {}

        individualsDict['@I01@'] = createFemaleWife()

        fam        = family.Family()
        fam.id     = '@F01@'
        fam.wifeId = '@I01@'

        self.assertTrue(fam.ValidateRoleGender(individualsDict))

    # Test that a Wife that is male fails the gender check.
    def testMaleWife(self):
        individualsDict = {}

        individualsDict['@I01@'] = createMaleWife()

        fam        = family.Family()
        fam.id     = '@F01@'
        fam.wifeId = '@I01@'

        self.assertFalse(fam.ValidateRoleGender(individualsDict))

    # Test that no husband/wife entries passes the gender check.
    def testNoHusband(self):
        individualsDict = {}

        individualsDict['@I01@'] = createIndividual1()

        fam    = family.Family()
        fam.id = '@F01@'

        self.assertTrue(fam.ValidateRoleGender(individualsDict))

    # Test husband with no gender set fails the gender check.
    def testHusbandNoGender(self):
        individualsDict = {}

        individualsDict['@I01@'] = createIndividual1()

        fam           = family.Family()
        fam.id        = '@F01@'
        fam.husbandId = '@I01@'

        self.assertFalse(fam.ValidateRoleGender(individualsDict))

    # Test wife with no gender set fails the gender check.
    def testWifeNoGender(self):
        individualsDict = {}

        individualsDict['@I01@'] = createIndividual1()

        fam        = family.Family()
        fam.id     = '@F01@'
        fam.wifeId = '@I01@'

        self.assertFalse(fam.ValidateRoleGender(individualsDict))

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

