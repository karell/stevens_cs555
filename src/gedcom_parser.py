import sys # -- Used for command line arguments
import individual
import family
import parents_not_to_old
from datetime import datetime
from datetime import date
from prettytable import PrettyTable
from pymongo import MongoClient
from unique_individuals import AreIndividualsUnique # US23

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
def checkMaleLastNames(childsID, fatherLastName):
##make sure child exists in dictionary before assigning, if child doesn't exist return false
    if individualsDict.__contains__(childsID):
        child = individualsDict.get(childsID)
    else:
        return False
    
    if  child.gender == "M":
        if child.lastname != fatherLastName:
            print("US16: Child " + child.firstAndMiddleName + child.lastname + " does not match fathers lastname of "  + fatherLastName)                
            return False
        else:
            return True
    else:
        return True
##US22 All individual IDs should be unique and all family IDs should be unique
def isUniqueRecordId(recordId,parentDictionary):
    if recordId in parentDictionary:
        return False
    else:
      return True

##US03 Birth before death
def isBirthBeforeDeath(birthDate, deathDate):
    if birthDate is None:
        return False
    if deathDate is None:
        return True
    return birthDate < deathDate
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

for line in inputFile:
    lineSplit = line.split()
    if lineSplit[0] == "0" and len(lineSplit) > 2 and (lineSplit[2] == "INDI" or lineSplit[2] == "FAM"):
        if tmpObj is not None:
            if tmpObj.type == "I":
                if isUniqueRecordId(tmpObj.id,individualsDict):
                    #check birth before death
                    if isBirthBeforeDeath(tmpObj.birthDate,tmpObj.deathDate) != True:
                        print("US03: Birth Before Death")
                    individualsDict[tmpObj.id] = tmpObj
                else:
                    print("Duplicate individual found")  ## TODO: keep all records
            else:
                if isUniqueRecordId(tmpObj.id,familiesDict):
                    familiesDict[tmpObj.id] = tmpObj
                else:
                    print("Duplicate family found") ## TODO: keep all records
        tmpObj = None
        if lineSplit[2] == "INDI":
            tmpObj = individual.Individual()
        else:
            tmpObj = family.Family()
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
                if individual.compareDates(tmpObj.birthDate):
                    print ("Invalid birth date for " + tmpObj.name)
                    tmpObj.birthDate = None
            elif dateType == "DEAT":
                tmpObj.deathDate = parseStringtoDate(lineSplit[2],lineSplit[3],lineSplit[4])
                if individual.compareDates(tmpObj.deathDate):
                    print ("Invalid death date for " + tmpObj.name)
                    tmpObj.deathDate = None
                else:
                    tmpObj.alive = (tmpObj.deathDate is None) #for US03 - collect alive data
            elif dateType == "MARR":
                tmpObj.marriageDate = parseStringtoDate(lineSplit[2],lineSplit[3],lineSplit[4])
                if individual.compareDates(tmpObj.marriageDate):
                    print ("Invalid marriage date for " + tmpObj.name)
                    tmpObj.marriageDate = None
            elif dateType == "DIV":
                tmpObj.divorcedDate = parseStringtoDate(lineSplit[2],lineSplit[3],lineSplit[4])
                if individual.compareDates(tmpObj.divorcedDate):
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
    ##US 16 Make sure Male children have husbands last name, if they don't, don't add them to father as a child
    for j in familiesDict[i].children:
        checkMaleLastNames(j, indiObjHusband.lastname)
    ##US 12 Check mothers age difference less than 60 and fathers less than 80 from child
        if individualsDict.__contains__(j):
            childAge = individualsDict.get(j).birthDate
            if indiObjHusband.birthDate is not None and childAge is not None:
                if parents_not_to_old.isValidFatherAge(childAge, indiObjHusband.birthDate) is False:
                    print ("US12: Invalid Father Age: " + indiObjHusband.name + " is more than 80 years older than child: " + individualsDict.get(j).name)
            if indiObjWife.birthDate is not None and childAge is not None:
                if parents_not_to_old.isValidMotherAge(childAge, indiObjWife.birthDate) is False:
                    print ("US12: Invalid Mother Age: " + indiObjWife.name + " is more than 60 years older than child: " + individualsDict.get(j).name)
    
    individualsDict[familiesDict[i].husbandId].children = familiesDict[i].children
        
    individualsDict[familiesDict[i].wifeId].children = familiesDict[i].children
    #update the spouse id
    individualsDict[familiesDict[i].husbandId].spouse.append(familiesDict[i].wifeId)
    individualsDict[familiesDict[i].wifeId].spouse.append(familiesDict[i].husbandId)
    
    #Check marraige date against birth  ## What User Story is this? 
    if familiesDict[i].marriageDate is not None: 
        if indiObjHusband.birthDate is not None and familiesDict[i].marriageDate < indiObjHusband.birthDate:
            print ("Invalid marriage and birth dates for " + indiObjHusband.name)
            ## indiObjHusband.birthDate = None ## need to keep all records even if there are errors/anomolies
            ## familiesDict[i].marriageDate = None
        if indiObjWife.birthDate is not None and familiesDict[i].marriageDate < indiObjWife.birthDate:
            print ("Invalid marriage and birth dates for " + indiObjWife.name)
            ## indiObjWife.birthDate = None ## need to keep all records even if there are errors/anomolies
            ## familiesDict[i].marriageDate = None
        #story 05 - marriage before death
        if not familiesDict[i].marriageBeforeDeath(indiObjHusband.deathDate,indiObjWife.deathDate):
            print ("Invalid marriage date for family " + familiesDict[i].id)
    #story 06 divorce before death
    if familiesDict[i].divorcedDate is not None and \
        not familiesDict[i].divorceBeforeDeath(indiObjHusband.deathDate,indiObjWife.deathDate):
        print ("Invalid divorce date for family " + familiesDict[i].id)

    # User Story: US21: Check the genders of the husband and wife, if they exist.
    familiesDict[i].ValidateRoleGender(individualsDict)
    
    # Build the output prettytable. Convert the internal format of variables to
    # string format prior to adding a row to the output prettytable.
    familiesDict[i].toString()
    try:
        fam = familiesDict[i]
        outputtableF.add_row([fam.id,fam.marriageDateStr,fam.divorcedDateStr,fam.husbandId,fam.husbandName,fam.wifeId,fam.wifeName,str(fam.children)])
    except:
        print("Unable to add Family to collection")
    #save to db
    if DB_INIT is not None:
        FAMILIES.insert_one(familiesDict[i].__dict__)

for i in sorted(individualsDict.keys()):
    # Build the output prettytable. Convert the internal format of variables to
    # string format prior to adding a row to the output prettytable.
    individualsDict[i].toString()
    try:
        ind = individualsDict[i]
        outputtableI.add_row([ind.id,ind.firstAndMiddleName,ind.lastname,ind.gender,ind.birthDateStr,ind.calculateAge(),ind.alive,ind.deathDateStr,ind.childrenStr,ind.spouseStr])
    except:
        print("Unable to add Individual to collection")
    #save to db
    if DB_INIT is not None:
        INDVIDUALS.insert_one(individualsDict[i].__dict__)

# ----------
# US23 - Unique Individuals
# Check the list of individuals for any that are not unique.
# ----------
if AreIndividualsUnique(individualsDict):
    print("US23: All individuals in the GEDCOM file are unique.")
else:
    print("US23: Duplicate individuals were found in the GEDCOM file.")

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
