# ---------------------------------------------------------------------------
# Class Individual
# This class encapsulates an Individual definition from a GEDCOM file and
# provides functionality and validation associated with an individual.
# ---------------------------------------------------------------------------

from datetime import date

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
                print("Unable to convert Birth Date")
        if self.deathDate is not None:
            self.deathDateStr = self.deathDate.strftime('%d %b %Y')
        if len(self.children) > 0:
            self.childrenStr = str(self.children)
        if len(self.children) > 0:
            self.spouseStr = str(self.spouse)

    def calculateAge(self):
        today = date.today()
        if self.birthDate and self.deathDate:
            death = self.deathDate
            birth = self.birthDate
            self.age = death.year - birth.year - ((death.month, death.day) < (birth.month, birth.day))
        elif self.birthDate and self.deathDate is None:
            birth = self.birthDate
            self.age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return self.age
