'''
Created on Mar 18, 2018

@author: esther
'''
import unittest
import datetime
import sys

sys.path.append('../')

import individual
import family

# -----------------------------------------------------------------------------
# User Story #08: Children should be born after marriage of parents 
#                (and not more than 9 months after their divorce)
# -----------------------------------------------------------------------------

def CreateFather():
    father                    = individual.Individual()
    father.id                 = "H1"
    father.firstAndMiddleName = "John James"
    father.lastname           = "Jamison"
  

    return father

def CreateMother():
    mother                    = individual.Individual()
    mother.id                 = "W1"
    mother.firstAndMiddleNAme = "Jane Janet"
    mother.lastname           = "Jamison"
    return mother

def CreateChild(id,birthDate,first):
    child                    = individual.Individual()
    child.id                 = id
    child.firstAndMiddleNAme = first
    child.lastname           = "Jamison"
    child.birthDate          = birthDate

    return child

def CreateFamily(mother,father, marriageDate, divorceDate):
    theFamily                  = family.Family()
    theFamily.id               = "F1"
    theFamily.husbandId        = father.id
    theFamily.wifeId           = mother.id
    theFamily.marriageDate     = marriageDate
    theFamily.divorcedDate     = divorceDate
    return theFamily

class Test_BirthAfterMarriage(unittest.TestCase):

    def test_BirthIsAfterMarriage(self):
        mother    = CreateMother()
        father    = CreateFather()
        child     = CreateChild("C1",datetime.date(2000,10,1),"Jimmy John")
        theFamily = CreateFamily(mother,father, datetime.date(2000,1,30), datetime.date(2017,9,30))
        theFamily.children.append(child)

        individualsDict             = {}
        individualsDict[mother.id] = mother
        individualsDict[father.id] = father
        individualsDict[child.id]  = child

        self.assertTrue(theFamily.IsBirthAfterMarriage(individualsDict,child))
    
    def test_BirthIsNotTooLongAfterDivorce(self):
        mother    = CreateMother()
        father    = CreateFather()
        child     = CreateChild("C1",datetime.date(2000,10,1),"Jimmy John")
        theFamily = CreateFamily(mother,father, datetime.date(2000,1,30), datetime.date(2017,8,1))
        theFamily.children.append(child)

        individualsDict             = {}
        individualsDict[mother.id] = mother
        individualsDict[father.id] = father
        individualsDict[child.id]  = child

        self.assertTrue(theFamily.IsBirthBeforeDivorce(individualsDict,child))
    
if __name__ == '__main__':
    unittest.main()