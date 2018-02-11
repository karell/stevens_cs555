import sys # -- Used for command line arguments
import individual

from datetime import datetime
from datetime import date
from prettytable import PrettyTable
from pymongo import MongoClient

DB_INIT = None
try:
  # DB Constant definition
  CLIENT = MongoClient(serverSelectionTimeoutMS=5)
  DB = CLIENT.GEDCOM
  INDVIDUALS = DB.individuals
  FAMILIES = DB.families
  # clear collections
  INDVIDUALS.drop()
  FAMILIES.drop()
  DB_INIT = True
except:
  print("DB instance is not running")

tags = {'INDI':'0','NAME':'1','SEX':'1','BIRT':'1','DEAT':'1','FAMC':'1','FAMS':'1','FAM':'0','MARR':'1','HUSB':'1','WIFE':'1','CHIL':'1','DIV':'1','DATE':'2','HEAD':'0','TRLR':'0','NOTE':'0'}
individualsDict = {}
familiesDict = {}
outputtableI = PrettyTable(["ID","First Name", "LastName","Gender","Birthday","Age","Alive","Death","Children","Spouse"])
outputtableF = PrettyTable(["ID","Married","Divorced","Husband ID","Husband Name","Wife ID","Wife Name","Children"])
#

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
        ##Adding Lastname and for US16
        self.lastName = ""
        self.gender = ""

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

##US16 Check Male Lastnames
def checkMaleLastNames(id, fatherLastName):
    person = individualsDict.get(id)
    if (person.lastname != fatherLastName):
        print("Child " + person.firstAndMiddleName + person.lastname + " does not match fathers lastname of "  + fatherLastName)                
    
# ----------
# Validate that there is only one argument on the command line. This means there
# are two arguments total - the first is the name of the script.
# ----------
if len(sys.argv) == 2:
	inFileName = sys.argv[1]
	try:
		inputFile = open(inFileName)
	except:
		print("Unable to open that input file. Please try again.")
		quit()
else:
	print("Error! Invalid arguments.")
	print("Specify the input file name on the command line.")
	quit()

tmpObj = None
dateType = None

CurrentDate = datetime.now()

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
            tmpObj = individual.Individual()
        else:
            tmpObj = Family()
        tmpObj.id = lineSplit[1]
    elif lineSplit[1] in tags and (lineSplit[0] == "1" or lineSplit[0] == "2") and tags[lineSplit[1]] == lineSplit[0]:
        if lineSplit[1] == "NAME":
            tmpObj.name = ' '.join(lineSplit[2:])
## FOR User Story 16, Need to separate last names
            tmpObj.firstAndMiddleName = ' '.join(lineSplit[2:]).split(sep="/", maxsplit=2).__getitem__(0)
            tmpObj.lastname =  ' '.join(lineSplit[2:]).split(sep="/", maxsplit=2).__getitem__(1)
            
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
                if tmpObj.birthDate > CurrentDate:
                    print ("Invalid birth date for " + tmpObj.name)
                    tmpObj.birthDate = None
            elif dateType == "DEAT":
                tmpObj.deathDate = parseStringtoDate(lineSplit[2],lineSplit[3],lineSplit[4])
                if tmpObj.deathDate > CurrentDate:
                    print ("Invalid death date for " + tmpObj.name)
                    tmpObj.deathDate = None
            elif dateType == "MARR":
                tmpObj.marriageDate = parseStringtoDate(lineSplit[2],lineSplit[3],lineSplit[4])
                if tmpObj.marriageDate > CurrentDate:
                    print ("Invalid marriage date for " + tmpObj.name)
                    tmpObj.marriageDate = None
            elif dateType == "DIV":
                tmpObj.divorcedDate = parseStringtoDate(lineSplit[2],lineSplit[3],lineSplit[4])
                if tmpObj.divorcedDate > CurrentDate:
                    print ("Invalid divorced date for " + tmpObj.name)
                    tmpObj.divorcedDate = None
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
    
    #Check marraige date against birth
    if familiesDict[i].marriageDate is not None: 
        if indiObjHusband.birthDate is not None and familiesDict[i].marriageDate < indiObjHusband.birthDate:
            print ("Invalid marriage and birth dates for " + indiObjHusband.name)
            indiObjHusband.birthDate = None
            familiesDict[i].marriageDate = None
        if indiObjWife.birthDate is not None and familiesDict[i].marriageDate < indiObjWife.birthDate:
            print ("Invalid marriage and birth dates for " + indiObjWife.name)
            indiObjWife.birthDate = None
            familiesDict[i].marriageDate = None

    familiesDict[i].toString()
    #save to db
    if DB_INIT is not None:
        FAMILIES.insert_one(familiesDict[i].__dict__)

for i in sorted(individualsDict.keys()):
    individualsDict[i].toString()
    try:
        ind = individualsDict[i]
        outputtableI.add_row([ind.id,ind.firstAndMiddleName,ind.lastname,ind.gender,ind.birthDateStr,ind.calculateAge(),ind.alive,ind.deathDateStr,ind.childrenStr,ind.spouseStr])
    except:
        print("Unable to add Individual to collection")
    #save to db
    if DB_INIT is not None:
        INDVIDUALS.insert_one(individualsDict[i].__dict__)

print(outputtableI)
print(outputtableF)

# ----------
# Output both tables to a text file.
# ----------
try:
	outputFile = open("output_gedcom_tables.txt","w")
except:
	print("Unable to open the output file.")
	quit()

outputFile.write(outputtableI.get_string())
outputFile.write("\n")
outputFile.write(outputtableF.get_string())
