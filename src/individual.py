# ---------------------------------------------------------------------------
# Class Individual
# This class encapsulates an Individual definition from a GEDCOM file and
# provides functionality and validation associated with an individual.
# ---------------------------------------------------------------------------
import ErrorLogger
import date_diff_calculator
from datetime import date
from datetime import datetime

class Individual:
    def __init__(self):
        self.type = "I"
        self.id = ""
        self.firstAndMiddleName = ""
        self.lastname = ""
        self.name = ""
        self.gender = ""
        self.birthDate = None
        self.deathDate = None
        self.children = []
        self.spouse = []
        self.familyIdChild = None
        self.familyIdSpouse = None
        self.birthDateStr = "NA"
        self.deathDateStr = "NA"
        self.childrenStr = "NA"
        self.spouseStr = "NA"
        self.age = -1
        self.alive = False

    def toString(self):
        self.alive = (self.deathDate is None)
        if self.birthDate is not None:
            try:
                self.birthDateStr = self.birthDate.strftime('%d %b %Y')
            except:
                ErrorLogger.__logError__(ErrorLogger._INDIVIDUAL,"N/A", self.id, "Unrecognizable birth date.")
        if self.deathDate is not None:
            self.deathDateStr = self.deathDate.strftime('%d %b %Y')
        if len(self.children) > 0:
            self.childrenStr = str(self.children)
            
##2/15/18 testing found error if statement below should be checking for spouse, not children
        if len(self.spouse) > 0:
            self.spouseStr = str(self.spouse)

    def calculateAge(self):
        today = date.today()
        calculatedAge = date_diff_calculator.calculateDateDifference(self.birthDate, self.deathDate, "years")
        if calculatedAge is not None:
            self.age = str(calculatedAge)
        else:
            self.age = -1
        ##US7 call isAgeLessThan150
        self.isAgeLessThan150()
        return self.age    
    
##US7 determine if age is less than 150
    def isAgeLessThan150(self):
        individualAge = self.age
        if not date_diff_calculator.isSecondNumberBigger(int(individualAge), 150):
            ErrorLogger.__logAnomaly__(ErrorLogger._INDIVIDUAL,"US07", self.id, "Older than 150")
            return False
        else:
            return True
#For story 01 - generic function to compare input date with current date, return true if input date is bigger than current date
def compareDates(tmpDate):
    return tmpDate > datetime.now()


        

