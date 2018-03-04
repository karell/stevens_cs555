import unittest
import datetime
import sys

sys.path.append('../')

import individual
import family

# -----------------------------------------------------------------------------
# User Story #10: Marriage should be 14 years after the birth of both spouses.
# -----------------------------------------------------------------------------

def CreateHusband(birthDate):
    husband                    = individual.Individual()
    husband.id                 = "H1"
    husband.birthDate          = birthDate
    husband.firstAndMiddleName = "John James"
    husband.lastname           = "Jamison"

    return husband

def CreateWife(birthDate):
    wife                       = individual.Individual()
    wife.id                    = "W1"
    wife.birthDate             = birthDate
    wife.firstAndMiddleNAme    = "Jane Janet"
    wife.lastname              = "Jamison"

    return wife

def CreateFamily(marriageDate,husband,wife):
    theFamily                  = family.Family()
    theFamily.id               = "F1"
    theFamily.husbandId        = husband.id
    theFamily.wifeId           = wife.id
    theFamily.marriageDate     = marriageDate

    return theFamily

class Test_MarriageAfter14(unittest.TestCase):

    def test_MarriageIsAfter14(self):
        husband   = CreateHusband(datetime.date(2000,1,1))
        wife      = CreateWife   (datetime.date(2000,1,1))
        theFamily = CreateFamily (datetime.date(2014,1,1),husband,wife)

        individualsDict             = {}
        individualsDict[husband.id] = husband
        individualsDict[wife.id]    = wife

        self.assertTrue(theFamily.IsMarriageAfter14())

    def test_MarriageIsNotAfter14Husband(self):
        husband   = CreateHusband(datetime.date(2001,1,1))
        wife      = CreateWife   (datetime.date(2000,1,1))
        theFamily = CreateFamily (datetime.date(2014,1,1),husband,wife)

        individualsDict             = {}
        individualsDict[husband.id] = husband
        individualsDict[wife.id]    = wife

        self.assertFalse(theFamily.IsMarriageAfter14())

    def test_MarriageIsNotAfter14Wife(self):
        husband   = CreateHusband(datetime.date(2000,1,1))
        wife      = CreateWife   (datetime.date(2001,1,1))
        theFamily = CreateFamily (datetime.date(2014,1,1),husband,wife)

        individualsDict             = {}
        individualsDict[husband.id] = husband
        individualsDict[wife.id]    = wife

        self.assertFalse(theFamily.IsMarriageAfter14())

    def test_BirthDateNotSetHusband(self):
        husband   = CreateHusband(None)
        wife      = CreateWife   (datetime.date(2000,1,1))
        theFamily = CreateFamily (datetime.date(2014,1,1),husband,wife)

        individualsDict             = {}
        individualsDict[husband.id] = husband
        individualsDict[wife.id]    = wife

        self.assertEqual(theFamily.IsMarriageAfter14(),"error")

    def test_BirthDateNotSetWife(self):
        husband   = CreateHusband(datetime.date(2000,1,1))
        wife      = CreateWife   (None)
        theFamily = CreateFamily (datetime.date(2014,1,1),husband,wife)

        individualsDict             = {}
        individualsDict[husband.id] = husband
        individualsDict[wife.id]    = wife

        self.assertEqual(theFamily.IsMarriageAfter14(),"error")

    def test_MarriageDateNotSet(self):
        husband   = CreateHusband(datetime.date(2000,1,1))
        wife      = CreateWife   (datetime.date(2000,1,1))
        theFamily = CreateFamily (None,husband,wife)

        individualsDict             = {}
        individualsDict[husband.id] = husband
        individualsDict[wife.id]    = wife

        self.assertEqual(theFamily.IsMarriageAfter14(),"error")
    
if __name__ == '__main__':
    unittest.main()
