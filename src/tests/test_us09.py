import unittest
import datetime
import sys

sys.path.append('../')

import individual
import family

# -----------------------------------------------------------------------------
# User Story #09: Child should be born before the death of the mother and at
#                 least nine months after the death of the father.
# -----------------------------------------------------------------------------

def CreateFather(deathDate):
    father                    = individual.Individual()
    father.id                 = "H1"
    father.firstAndMiddleName = "John James"
    father.lastname           = "Jamison"
    father.deathDate          = deathDate

    return father

def CreateMother(deathDate):
    mother                    = individual.Individual()
    mother.id                 = "W1"
    mother.firstAndMiddleNAme = "Jane Janet"
    mother.lastname           = "Jamison"
    mother.deathDate          = deathDate

    return mother

def CreateChild(id,birthDate,first):
    child                    = individual.Individual()
    child.id                 = id
    child.firstAndMiddleNAme = first
    child.lastname           = "Jamison"
    child.birthDate          = birthDate

    return child

def CreateFamily(mother,father):
    theFamily                  = family.Family()
    theFamily.id               = "F1"
    theFamily.husbandId        = father.id
    theFamily.wifeId           = mother.id

    return theFamily

class Test_BirthAfterDeath(unittest.TestCase):

    def test_BirthIsAfterDeath(self):
        mother    = CreateMother(datetime.date(2000,9,2))
        father    = CreateFather(datetime.date(2000,1,1))
        child     = CreateChild("C1",datetime.date(2000,9,1),"Jimmy John")
        theFamily = CreateFamily(mother,father)
        theFamily.children.append(child)

        individualsDict             = {}
        individualsDict[mother.id] = mother
        individualsDict[father.id] = father
        individualsDict[child.id]  = child

        self.assertTrue(theFamily.IsBirthAfterDeath(individualsDict,child))
    
    def test_BirthIsNotAfterDeathOfMother(self):
        mother    = CreateMother(datetime.date(2000,8,31))
        father    = CreateFather(datetime.date(2000,1,1))
        child     = CreateChild("C1",datetime.date(2000,9,1),"Jimmy John")
        theFamily = CreateFamily(mother,father)
        theFamily.children.append(child)

        individualsDict             = {}
        individualsDict[mother.id] = mother
        individualsDict[father.id] = father
        individualsDict[child.id]  = child

        self.assertFalse(theFamily.IsBirthAfterDeath(individualsDict,child))
    
    def test_BirthIsNotAfterDeathOfFather(self):
        mother    = CreateMother(datetime.date(2000,9,1))
        father    = CreateFather(datetime.date(2000,1,2))
        child     = CreateChild("C1",datetime.date(2000,9,1),"Jimmy John")
        theFamily = CreateFamily(mother,father)
        theFamily.children.append(child)

        individualsDict             = {}
        individualsDict[mother.id] = mother
        individualsDict[father.id] = father
        individualsDict[child.id]  = child

        self.assertFalse(theFamily.IsBirthAfterDeath(individualsDict,child))
    
if __name__ == '__main__':
    unittest.main()
