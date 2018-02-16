# ---------------------------------------------------------------------------
# Class Family
# This class encapsulates a Family definition from a GEDCOM file and
# provides functionality and validation associated with a Family.
# ---------------------------------------------------------------------------

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

