from datetime import datetime
from datetime import date
from prettytable import PrettyTable

tags = {'INDI':'0','NAME':'1','SEX':'1','BIRT':'1','DEAT':'1','FAMC':'1','FAMS':'1','FAM':'0','MARR':'1','HUSB':'1','WIFE':'1','CHIL':'1','DIV':'1','DATE':'2','HEAD':'0','TRLR':'0','NOTE':'0'}
individualsDict = {}
familiesDict = {}
outputtableI = PrettyTable(["ID","Name","Gender","Birthday","Age","Alive","Death","Children","Spouse"])
outputtableF = PrettyTable(["ID","Married","Divorced","Husband ID","Husband Name","Wife ID","Wife Name","Children"])
#
class Individual:
    def __init__(self):
        self.type = "I"
        self.id = ""
        self.name = ""
        self.gender = ""
        self.birthDate = None
        self.deathDate = None
        self.children = []
        self.spouse = []
        self.familyIdChild = None
        self.familyIdSpouse = None
    
    def toString(self):
        alive = (self.deathDate is None)
        birthDateStr = "NA"
        if self.birthDate is not None:
            try:    
                birthDateStr = self.birthDate.strftime('%d %b %Y')
            except:
                print("Unable to convert Birth Date")
        deathDateStr = "NA"
        if self.deathDate is not None:
            deathDateStr = self.deathDate.strftime('%d %b %Y')
        childrenStr = "NA"
        if len(self.children) > 0:
            childrenStr = str(self.children)
        spouseStr = "NA"
        if len(self.children) > 0:
            spouseStr = str(self.spouse)
        try:
            outputtableI.add_row([self.id,self.name,self.gender,birthDateStr,self.calculateAge(),alive,deathDateStr,childrenStr,spouseStr])
        except:
            print("Unable to add Individual to collection")
    
    def calculateAge(self):
        today = date.today()
        age = -1
        if self.birthDate and self.deathDate:
            death = self.deathDate
            birth = self.birthDate
            age = death.year - birth.year - ((death.month, death.day) < (birth.month, birth.day))
        elif self.birthDate and self.deathDate is None:
            birth = self.birthDate
            age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return age

class Family:
    def __init__(self):
        self.type = "F"
        self.id = ""
        self.marriageDate = None
        self.divorcedDate = None
        self.husbandId = ""
        self.husbandName = ""
        self.wifeId = ""
        self.wifeName = ""
        self.children = []
    
    def toString(self):
        marriageDateStr = "NA"
        divorcedDateStr = "NA"
        if self.marriageDate is not None:
            marriageDateStr = self.marriageDate.strftime('%d %b %Y')
        if self.divorcedDate is not None:
            divorcedDateStr = self.divorcedDate.strftime('%d %b %Y')
        outputtableF.add_row([self.id,marriageDateStr,divorcedDateStr,self.husbandId,self.husbandName,self.wifeId,self.wifeName,str(self.children)])

def parseStringtoDate(day,month,year):
    retDate = None
    if (int(day) < 10):
        day = "0" + day
    try:
        retDate = datetime.strptime(day + " " + month + " " + year,'%d %b %Y')
    except ValueError:
        print("Wrong Date Format for " + day + " " + month + " " + year)
    return retDate

inFileName = input("Enter the input file name: ")

try:
	inputFile = open(inFileName)
except:
	print("Unable to open that input file. Please try again.")
	quit()

tmpObj = None
dateType = None

for line in inputFile:
    lineSplit = line.split()
    if lineSplit[0] == "0" and len(lineSplit) > 2 and (lineSplit[2] == "INDI" or lineSplit[2] == "FAM"):
        if tmpObj is not None:
            if tmpObj.type == "I":
                individualsDict[tmpObj.id] = tmpObj
            else:
                familiesDict[tmpObj.id] = tmpObj
        tmpObj = None
        if lineSplit[2] == "INDI":
            tmpObj = Individual()
        else:
            tmpObj = Family()
        tmpObj.id = lineSplit[1]
    elif lineSplit[1] in tags and (lineSplit[0] == "1" or lineSplit[0] == "2") and tags[lineSplit[1]] == lineSplit[0]:
        if lineSplit[1] == "NAME":
            tmpObj.name = ' '.join(lineSplit[2:])
        elif lineSplit[1] == "SEX":
            tmpObj.gender = lineSplit[2]
        elif lineSplit[1] == "BIRT" or lineSplit[1] == "DEAT" or lineSplit[1] == "MARR" or lineSplit[1] == "DIV":
            dateType = lineSplit[1]
        elif lineSplit[1] == "FAMC":
            tmpObj.familyIdChild = lineSplit[2]
        elif lineSplit[1] == "FAMS":
            tmpObj.familyIdSpouse = lineSplit[2]
        elif lineSplit[1] == "HUSB":
            tmpObj.husbandId = lineSplit[2]
        elif lineSplit[1] == "WIFE":
            tmpObj.wifeId = lineSplit[2]
        elif lineSplit[1] == "CHIL":
            tmpObj.children.append(lineSplit[2])
        elif lineSplit[1] == "DATE" and dateType is not None and len(lineSplit) > 4:
            if (dateType == "BIRT"):
                tmpObj.birthDate = parseStringtoDate(lineSplit[2],lineSplit[3],lineSplit[4])
            elif dateType == "DEAT":
                tmpObj.deathDate = parseStringtoDate(lineSplit[2],lineSplit[3],lineSplit[4])
            elif dateType == "MARR":
                tmpObj.marriageDate = parseStringtoDate(lineSplit[2],lineSplit[3],lineSplit[4])
            elif dateType == "DIV":
                tmpObj.divorcedDate = parseStringtoDate(lineSplit[2],lineSplit[3],lineSplit[4])
            dateType = None
            
if tmpObj is not None:
    if tmpObj.type == "I":
        individualsDict[tmpObj.id] = tmpObj
    else:
        familiesDict[tmpObj.id] = tmpObj

inputFile.close()

for i in sorted(familiesDict.keys()):
    #TODO should we add try/catch or can we assume that each family has wife/husband?
    indiObjHusband = individualsDict[familiesDict[i].husbandId]
    indiObjWife = individualsDict[familiesDict[i].wifeId]
    #update the names of husband and wife in the family object
    familiesDict[i].husbandName = indiObjHusband.name
    familiesDict[i].wifeName = indiObjWife.name
    #update the children of wife and husband objects
    individualsDict[familiesDict[i].husbandId].children = familiesDict[i].children
    individualsDict[familiesDict[i].wifeId].children = familiesDict[i].children
    #update the spouse id
    individualsDict[familiesDict[i].husbandId].spouse.append(familiesDict[i].wifeId)
    individualsDict[familiesDict[i].wifeId].spouse.append(familiesDict[i].husbandId)
    
    familiesDict[i].toString()

for i in sorted(individualsDict.keys()):
    individualsDict[i].toString()

print(outputtableI)
print(outputtableF)
