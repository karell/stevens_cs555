# ---------------------------------------------------------------------------
# Class Family
# This class encapsulates a Family definition from a GEDCOM file and
# provides functionality and validation associated with a Family.
# ---------------------------------------------------------------------------

import individual
import dateutil.relativedelta
import ErrorLogger
import date_diff_calculator

class Family:
    def __init__(self):
        self.type = "F"
        self.id = ""
        self.marriageDate = None
        self.marriageDateStr = "NA"
        self.divorcedDate = None
        self.divorcedDateStr = "NA"
        self.husbandId = ""
        self.husbandName = ""
        self.wifeId = ""
        self.wifeName = ""
        self.children = []
        ##Adding Lastname and for US16
        self.lastName = ""
        self.gender = ""

    def toString(self):
        if self.marriageDate is not None:
            self.marriageDateStr = self.marriageDate.strftime('%d %b %Y')
        if self.divorcedDate is not None:
            self.divorcedDateStr = self.divorcedDate.strftime('%d %b %Y')

    # ----------
    # UserStory: US21
    # Function:  ValidateRoleGender
    # Purpose:   To check the genders of the Husband and Wife of the family.
    # Returns:   True  = Husband (if exists) is male and
    #                    Wife (if exists) is female.
    #            False = Husband (if exists) is not male or
    #                    Wife (if exists) is not female.
    # ----------
    def ValidateRoleGender(self,individuals):
        result = True

        if self.husbandId is not None and self.husbandId != "":
            try:
                if individuals[self.husbandId].gender != 'M':
                    result = False
                    #print ("US21: Family " + self.id + ", Husband " + self.husbandId + " is not male.")
            except:
                print("US21: Family " + self.id + ", Husband " + self.husbandId + " not found as an individual.")

        if self.wifeId is not None and self.wifeId != "":
            try:
                if individuals[self.wifeId].gender != 'F':
                    result = False
                    #print ("US21: Family " + self.id + ", Wife " + self.wifeId + " is not female.")
            except:
                print("US21: Family " + self.id + ", Wife " + self.wifeId + " not found as an individual.")

        return result

    # US10: Marriage at least 14 years after birth of husband and wife
    def IsMarriageAfter14(self,individuals):
        result = False
        husband = None
        wife = None
        if self.husbandId is not None:
            husband = individuals[self.husbandId]
        if self.wifeId is not None:
            wife = individuals[self.wifeId]
        if husband is not None and \
           wife    is not None and \
           self.marriageDate is not None and \
           husband.birthDate is not None and \
           wife.birthDate is not None:
            if dateutil.relativedelta.relativedelta(self.marriageDate,husband.birthDate).years >= 14 and \
               dateutil.relativedelta.relativedelta(self.marriageDate,wife.birthDate).years    >= 14:
                result = True
        else:
            result = "error"
        
        return result

    # US09: Birth of child must occur at least 9 months after the death
    #       of the father and after the death of the mother.
    def IsBirthAfterDeath(self,individuals,child):
        result          = True
        motherDeathDate = None
        fatherDeathDate = None

        # Validate the mother record
        if self.wifeId is not None:
            mother = individuals[self.wifeId]
            if mother is not None:
                motherDeathDate = mother.deathDate
            else:
                ErrorLogger.__logError__(ErrorLogger._FAMILY,"US09", self.id, str("Wife " + self.wifeId + " is not found as an Individual."))
                result = "error"

        # Validate the father record
        if self.husbandId is not None:
            father = individuals[self.husbandId]
            if father is not None:
                fatherDeathDate = father.deathDate
            else:
                ErrorLogger.__logError__(ErrorLogger._FAMILY,"US09", self.id, str("Husband " + self.husbandId + " is not found as an Individual."))
                result = "error"

        # Validate the child record and compare dates
        if child.birthDate is not None:
            if motherDeathDate is not None:
                if child.birthDate > mother.deathDate:
                    ErrorLogger.__logError__(ErrorLogger._FAMILY,"US09", self.id, str("Child " + child.id + " born on " + str(child.birthDate) + " is after mother's death date of " + str(motherDeathDate)))
                    result = False
            if fatherDeathDate is not None:
                deltaFather = dateutil.relativedelta.relativedelta(fatherDeathDate,child.birthDate)
                if deltaFather.years < 0 or (deltaFather.years == 0 and deltaFather.months > -9):
                    ErrorLogger.__logError__(ErrorLogger._FAMILY,"US09", self.id, str("Child " + child.id + " born on " + str(child.birthDate) + " is less than 9 months after father's death date of " + str(fatherDeathDate)))
                    result = False
        else:
            ErrorLogger.__logError__(ErrorLogger._FAMILY,"US09", self.id, str("Child " + child.id + " has no birth date."))
            result = "error"

        return result

    # US04: Marriage before divorce
    def marriageBeforeDivorce(self):
        if (self.marriageDate and self.divorcedDate is None) or (self.divorcedDate is None and self.marriageDate is None):
            return True
        if self.marriageDate is None:
            return False
        return self.marriageDate < self.divorcedDate
    
    #story 05
    def marriageBeforeDeath(self,deathDateHusband,deathDateWife):
        return self.compareDates(self.marriageDate,deathDateHusband,deathDateWife)
    #story 06
    def divorceBeforeDeath(self,deathDateHusband,deathDateWife):
        return self.compareDates(self.divorcedDate,deathDateHusband,deathDateWife)
    #for both story 05 and 06
    def compareDates(self,date1,date2,date3):
        retValue = True
        if date1 is not None:
            retValue = True if date2 is None else date1 < date2
            if retValue: 
                retValue = True if date3 is None else date1 < date3
        return retValue
    
     # US08: Birth of child must occur at least 9 months after the death
    #       of the father and after the death of the mother.
    def IsBirthAfterMarriage(self,individuals,child):
        result = True
        marriageDate = None
        divorceDate = None

        # Validate the mother record
        if self.wifeId is not None:
            mother = individuals[self.wifeId]
            marriageDate = self.marriageDate
            divorceDate = self.divorcedDate
           
        # Validate the father record
        if self.husbandId is not None:
            father = individuals[self.husbandId]
        
        # Validate the child record and compare dates
        if child.birthDate is not None:
            if marriageDate is not None:
                marriageDiff = date_diff_calculator.calculateDateDifference(marriageDate, child.birthDate, "months")
                if marriageDiff < 9:
                    ErrorLogger.__logError__(ErrorLogger._FAMILY,"US08", self.id, str("Child " + child.id + " born on " + str(child.birthDate) + " is before marriage date of " + str(marriageDate)))
                    result = False
            if divorceDate is not None:
                divorceDiff = date_diff_calculator.calculateDateDifference(divorceDate, child.birthDate, "months")
                if divorceDiff > 9:
                    ErrorLogger.__logError__(ErrorLogger._FAMILY,"US08", self.id, str("Child " + child.id + " born on " + str(child.birthDate) + " is more than 9 months after divorce date of " + str(divorceDate)))
                    result = False
        else:
            ErrorLogger.__logError__(ErrorLogger._FAMILY,"US08", self.id, str("Child " + child.id + " has no birth date."))
            result = "error"

        return result   