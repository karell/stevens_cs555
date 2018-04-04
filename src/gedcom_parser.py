import sys   # -- Used for command line arguments
import individual
import family
import parents_not_to_old
import ErrorLogger
import random
import unique_record_id
import corresponding_records

from datetime import datetime
from prettytable import PrettyTable
from pymongo import MongoClient
from unique_individuals import AreIndividualsUnique   # US23
from siblings_married import is_marriage_of_siblings   # US18
from cousins_married import is_marriage_of_cousins   # US19
from family_relationships import validParentDecendantMarriages
from family_relationships import validUncleAuntMarriages
from bigamy import is_bigamy

DB_INIT = None
try:
    # DB Constant definition
    CLIENT = MongoClient(serverSelectionTimeoutMS=5)
    DB = CLIENT.GEDCOM
    INDVIDUALS = DB.individuals
    FAMILIES = DB.families
    ERRORS = DB.errors
    # clear collections
    INDVIDUALS.drop()
    FAMILIES.drop()
    ERRORS.drop()
    DB_INIT = True
except:
    print("Database instance is not running.")

errorlogger = ErrorLogger
errorlogger.__initLogger__()
tags = {'INDI':'0','NAME':'1','SEX':'1','BIRT':'1','DEAT':'1','FAMC':'1','FAMS':'1','FAM':'0','MARR':'1','HUSB':'1','WIFE':'1','CHIL':'1','DIV':'1','DATE':'2','HEAD':'0','TRLR':'0','NOTE':'0'}
individualsDict = {}
familiesDict = {}
outputtableI = PrettyTable(["ID","First Name", "LastName","Gender","Birthday","Age","Alive","Death","Children","Spouse"])
outputtableF = PrettyTable(["ID","Married","Divorced","Husband ID","Husband Name","Wife ID","Wife Name","Children"])

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
            errorlogger.__logAnomaly__(ErrorLogger._INDIVIDUAL,"US16", child.id, \
                str("Father's Last Name of " + fatherLastName + " doesn't match childs's Last Name of " + child.lastname))             
            return False
        else:
            return True
    else:
        return True



##US03 Birth before death
def isBirthBeforeDeath(birthDate, deathDate):
    if birthDate is None:
        return False
    if deathDate is None:
        return True
    return birthDate < deathDate   

#US14 no more than 5 siblings born the same day
def verifySiblingsDates(allDates):
    retValue = True
    datesDict = {}
    for d in allDates:
        if d in datesDict:
            datesDict[d] = datesDict.get(d) + 1
            if datesDict[d] > 5:
                return False
        else:#if we did not find this date, we first check if we have date within day of already found dates
            found = False
            for d2 in datesDict:
                delta = d2 - d
                if (abs(delta.days) < 2):
                    datesDict[d2] = datesDict.get(d2) + 1
                    found = True
                    if datesDict[d2] > 5:
                        retValue = False
                        break    
            if not found:
                datesDict[d] = 1
                
    return retValue  
#US13 Siblings need to be more than 8 months apart or less than 2 days
def verifySiblingsSpace(allDates):
    retValue = True
    datesSet = set()
    for d in allDates:
        if d in datesSet:
            retValue = False
            break
        else:
            found = False
            for d2 in datesSet:
                delta = d2 - d
                if abs(delta.days) > 1 and abs(delta.days) < 280:
                    retValue = False
                    break 
            if retValue:
                datesSet.add(d)
            else:
                break
                
    return retValue

#US 28 - sort children by their birth date
def sortChildren(children):
    try:
        childern = sorted(children, key=lambda individual: individual.birthDate)
    except:
        errorlogger.__logError__(ErrorLogger._FAMILY,'US28', children[0].id, "Sort children by birth date")


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
                if not unique_record_id.isUniqueRecordId(tmpObj.id,individualsDict):
                    errorlogger.__logError__(ErrorLogger._INDIVIDUAL, "US22", tmpObj.id, "Record ID is not unique")
                    tmpObj.id = tmpObj.id + str(random.randint(1,99999))
                individualsDict[tmpObj.id] = tmpObj
                    #check birth before death
                if isBirthBeforeDeath(tmpObj.birthDate,tmpObj.deathDate) != True:
                        errorlogger.__logError__(ErrorLogger._INDIVIDUAL,"US03", tmpObj.id, "Birth Before Death")                      
                
            else:
                if not unique_record_id.isUniqueRecordId(tmpObj.id,familiesDict):
                    errorlogger.__logError__(ErrorLogger._FAMILY, "US22", tmpObj.id, "Record ID is not unique")
                    tmpObj.id = tmpObj.id + str(random.randint(1,99999))
                familiesDict[tmpObj.id] = tmpObj

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
                    errorlogger.__logError__(ErrorLogger._INDIVIDUAL,"US01", tmpObj.id, "Invalid birth date")
                    tmpObj.birthDate = None
            elif dateType == "DEAT":
                tmpObj.deathDate = parseStringtoDate(lineSplit[2],lineSplit[3],lineSplit[4])
                if individual.compareDates(tmpObj.deathDate):
                    errorlogger.__logError__(ErrorLogger._INDIVIDUAL,"US01", tmpObj.id, "Invalid death date")
                    tmpObj.deathDate = None
                else:
                    tmpObj.alive = (tmpObj.deathDate is None) #for US03 - collect alive data
            elif dateType == "MARR":
                tmpObj.marriageDate = parseStringtoDate(lineSplit[2],lineSplit[3],lineSplit[4])
                if individual.compareDates(tmpObj.marriageDate):
                    errorlogger.__logError__(ErrorLogger._FAMILY,"US02", tmpObj.id, "Invalid marriage date")
                    tmpObj.marriageDate = None
            elif dateType == "DIV":
                tmpObj.divorcedDate = parseStringtoDate(lineSplit[2],lineSplit[3],lineSplit[4])
                if individual.compareDates(tmpObj.divorcedDate):
                    errorlogger.__logError__(ErrorLogger._FAMILY,"US??", tmpObj.id, "Invalid divorce date")
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
                    errorlogger.__logError__(ErrorLogger._FAMILY,"US12", individualsDict.get(j).id, str("Invalid Father Age: " + indiObjHusband.name + " is more than 80 years older than child: " + individualsDict.get(j).name))
            if indiObjWife.birthDate is not None and childAge is not None:
                if parents_not_to_old.isValidMotherAge(childAge, indiObjWife.birthDate) is False:
                    errorlogger.__logError__(ErrorLogger._FAMILY,"US12", individualsDict.get(j).id, str("Invalid Mother Age: " + indiObjWife.name + " is more than 60 years older than child: " + individualsDict.get(j).name))
            ##US 09 Birth of child must be after death of mother and 9 months after death of father
            familiesDict[i].IsBirthAfterDeath(individualsDict,individualsDict.get(j))
            ##US 08 Birth of child must be after marriage date and 10 months after divorce
            familiesDict[i].IsBirthAfterMarriage(individualsDict,individualsDict.get(j))

    
    individualsDict[familiesDict[i].husbandId].children = familiesDict[i].children
        
    individualsDict[familiesDict[i].wifeId].children = familiesDict[i].children
    #update the spouse id
    individualsDict[familiesDict[i].husbandId].spouse.append(familiesDict[i].wifeId)
    individualsDict[familiesDict[i].wifeId].spouse.append(familiesDict[i].husbandId)
    # US11 check for bigamy
    is_bigamy(indiObjHusband, familiesDict, individualsDict)
    
    #Check marraige date against birth US02
    if familiesDict[i].marriageDate is not None: 
        if indiObjHusband.birthDate is not None and familiesDict[i].marriageDate < indiObjHusband.birthDate:
            errorlogger.__logError__(ErrorLogger._FAMILY,"US02", indiObjHusband.id, "Invalid marriage and birth dates")
            ## indiObjHusband.birthDate = None ## need to keep all records even if there are errors/anomolies
            ## familiesDict[i].marriageDate = None
        if indiObjWife.birthDate is not None and familiesDict[i].marriageDate < indiObjWife.birthDate:
            errorlogger.__logError__(ErrorLogger._FAMILY,"US02", indiObjWife.id, "Invalid marriage and birth dates")
            ## indiObjWife.birthDate = None ## need to keep all records even if there are errors/anomolies
            ## familiesDict[i].marriageDate = None
        #story 05 - marriage before death
        if not familiesDict[i].marriageBeforeDeath(indiObjHusband.deathDate,indiObjWife.deathDate):
            errorlogger.__logError__(ErrorLogger._FAMILY,"US05", familiesDict[i].id, "Invalid marriage date. Marriage before death.")
    #story 06 divorce before death
    if familiesDict[i].divorcedDate is not None and \
        not familiesDict[i].divorceBeforeDeath(indiObjHusband.deathDate,indiObjWife.deathDate):
        errorlogger.__logError__(ErrorLogger._FAMILY,"US06", familiesDict[i].id, "Invalid divorce date")

    # User Story: US21: Check the genders of the husband and wife, if they exist.
    if familiesDict[i].ValidateRoleGender(individualsDict) is False:
        errorlogger.__logAnomaly__(ErrorLogger._FAMILY, "US21", familiesDict[i].id, "Invalid parent genders")
  
    # US04
    if not familiesDict[i].marriageBeforeDivorce():
        errorlogger.__logError__(ErrorLogger._FAMILY,'US04', familiesDict[i].id, "Marriage before divorce date")

    # US10
    validMarriageDate = familiesDict[i].IsMarriageAfter14(individualsDict)
    if validMarriageDate == "error":
        errorlogger.__logError__(ErrorLogger._FAMILY, "US10", familiesDict[i].id, "Unable to validate marriage date")
    else:
        if not validMarriageDate:
            errorlogger.__logError__(ErrorLogger._FAMILY, "US10", familiesDict[i].id, "Marriage is less than 14 years after birth of husband and/or wife")
   
    #User Story 14: check siblings birth dates
    if len(familiesDict[i].children) > 5:
        testDates = []
        for child in familiesDict[i].children:
            try:
                if individualsDict[child].birthDate is not None:
                    testDates.append(individualsDict[child].birthDate)
            except:
                #print("Child does id does not exist in individual dictionary")
                errorlogger.__logError__(ErrorLogger._INDIVIDUAL, "US14", child.id, "Child does id does not exist in individual dictionary")
        if not verifySiblingsDates(testDates):
            #print ("Invalid birth dates for family " + familiesDict[i].id)
            errorlogger.__logError__(ErrorLogger._FAMILY, "US14", familiesDict[i].id, "Invalid Birth Dates for Family")

    #User Story 13: check siblings spacing
    if len(familiesDict[i].children) > 1:
        testDates = []
        for child in familiesDict[i].children:
            try:
                if individualsDict[child].birthDate is not None:
                    testDates.append(individualsDict[child].birthDate)
            except:
                #print("Child does id does not exist in individual dictionary")
                errorlogger.__logError__(ErrorLogger._INDIVIDUAL, "US13", child.id, "Child does id does not exist in individual dictionary")
        if not verifySiblingsSpace(testDates):
            #print ("Invalid siblings space for family " + familiesDict[i].id)
            errorlogger.__logError__(ErrorLogger._FAMILY, "US13", familiesDict[i].id, "Invalid Sibling Spacing in Family")
        #US 28 - sort children by their birth date
        sortChildren(familiesDict[i].children)

    # User Story 18: Check for married siblings
    is_marriage_of_siblings(familiesDict[i], familiesDict)
    
   

    # User Story 19: Check for married cousins
    is_marriage_of_cousins(familiesDict[i], familiesDict)
    
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
        outputtableI.add_row([ind.id,ind.firstAndMiddleName,ind.lastname,ind.gender,ind.birthDateStr,ind.age,ind.alive,ind.deathDateStr,ind.childrenStr,ind.spouseStr])
    except:
        print("Unable to add Individual to collection")
    #save to db
    if DB_INIT is not None:
        INDVIDUALS.insert_one(individualsDict[i].__dict__)

# ----------
# US23 - Unique Individuals
# Check the list of individuals for any that are not unique.
# ----------
if not AreIndividualsUnique(individualsDict):
    errorlogger.__logError__(ErrorLogger._GENERAL,"US23", "N/A", "Duplicate individuals were found in the GEDCOM file.")

# ----------
# US26 - Corresponding record
# Record existing in family and indiv. dictionary.
# ----------
corresponding_records.validateCorrespondingRecords(individualsDict, familiesDict)

# ----------
# US17 - 
# No marriages to descendants	Parents should not marry any of their descendants
# ----------
validParentDecendantMarriages(familiesDict,individualsDict)

# ----------
# US20 - 
# Aunts and uncles	Aunts and uncles should not marry their nieces or nephews
# ----------
validUncleAuntMarriages(familiesDict,individualsDict)
# ----------
# Print out the Individuals and Families in table format.
# ----------
# print(outputtableI)
# print(outputtableF)

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
outputFile.write("\n\n")
for i in sorted(errorlogger._logMessages):
    outputFile.write("\n")
    outputFile.write(i)
# ----------
# Print out the errors and anomalies.
# ----------
# errorlogger.__printLogMessages__()
