# ---------------------------------------------------------------------------
# Class Family
# This class encapsulates a Family definition from a GEDCOM file and
# provides functionality and validation associated with a Family.
# ---------------------------------------------------------------------------

import individual

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
    # UserStory: US23
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
                    print ("US21: Family " + self.id + ", Husband " + self.husbandId + " is not male.")
            except:
                print("US21: Family " + self.id + ", Husband " + self.husbandId + " not found as an individual.")

        if self.wifeId is not None and self.wifeId != "":
            try:
                if individuals[self.wifeId].gender != 'F':
                    result = False
                    print ("US21: Family " + self.id + ", Wife " + self.wifeId + " is not female.")
            except:
                print("US21: Family " + self.id + ", Wife " + self.wifeId + " not found as an individual.")

        return result

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