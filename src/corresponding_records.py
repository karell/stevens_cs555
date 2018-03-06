import ErrorLogger

def validateFamilyRoles(family, individualDic):
    if family.husbandId not in individualDic and family.wifeId not in individualDic:
        return False
    if family.husbandId in individualDic:
        husb = individualDic[family.husbandId]
        if len(family.children) == len(husb.children):
            if not childrenExistInFamily(husb.children,family.children):
                return False
        else:
            return False
    if family.wifeId in individualDic:
        wife = individualDic[family.wifeId]
        if len(family.children) == len(wife.children):
            if not childrenExistInFamily(wife.children,family.children):
                return False
        else:
            return False

    return familyMembersExist(family,individualDic)

def childrenExistInFamily(parentsChildren, familyChildren):
    for parentChild in parentsChildren:
        childFound = False
        for familyChild in familyChildren:
            if familyChild == parentChild:
                childFound = True
                break
        if childFound == False:
            return False
    return True

def validSpouseExists(individId, spouseId, familyDict):

    spouseFound = False
    for i in sorted(familyDict.keys()):
        if familyDict[i].husbandId == individId:
            if spouseId == familyDict[i].wifeId:
                spouseFound = True
        if familyDict[i].wifeId == individId:
            if spouseId == familyDict[i].husbandId:
                spouseFound = True
    return spouseFound

def isIndividualInFamily(individualId, family):
    if family.husbandId == individualId:
        return True
    if family.wifeId == individualId:
        return True
    for childId in family.children:
        if childId == individualId:
            return True
    return False

def familyMembersExist(family, individualDict): 
    if family.husbandId not in individualDict:
        return False
    if family.wifeId not in individualDict:
        return False
    for childId in family.children:
        if individualDict.get(childId) is None:
            return False
    return True

def oneForOneFamilyIndividualRecords(individualDict, familyDict):
    missingIndividuals = []
    for i in sorted(individualDict.keys()):
        individ = individualDict[i]
        individExists = False
        for j in sorted(familyDict.keys()):
            if isIndividualInFamily(individ.id,familyDict[j]):
                individExists = True
        if individExists == False:
            ErrorLogger.__logError__(ErrorLogger._INDIVIDUAL,"US26",individ.id,"Individual does not exist in family")
            missingIndividuals.append(individ.id)
    missedFamilies = []
    for i in sorted(familyDict.keys()):
        fam = familyDict[i]
        if not familyMembersExist(fam,individualDict):
            ErrorLogger.__logError__(ErrorLogger._FAMILY, "US26", fam.id, "Family members don't exist in individuals")
            missedFamilies.append(fam.id)
    if len(missingIndividuals) < 1 and len(missedFamilies) < 1:
      return True
    else:
      return False


#US26 
def validateCorrespondingRecords(individualDict, familyDict):

    errors = 0
    for i in sorted(individualDict.keys()):
        individ = individualDict[i]
        if len(individ.spouse) > 0:
            #validate spouse is in family
            spouseCount = 0
            for spouseId in individ.spouse:
                if validSpouseExists(individ.id, spouseId, familyDict):
                    spouseCount = spouseCount + 1
            if spouseCount != len(individ.spouse):
                errors = errors + 1
                ErrorLogger.__logError__(ErrorLogger._INDIVIDUAL, "US26", individ.id, "Family records do not contain spouse")
        
        if len(individ.children) > 0:
            #validate children exists in fam
            childrenFoundInFamily = False
            for j in sorted(familyDict.keys()):
                if childrenExistInFamily(individ.children,familyDict[j].children):
                    childrenFoundInFamily = True
            if childrenFoundInFamily == False:
                errors = errors + 1
                ErrorLogger.__logError__(ErrorLogger._FAMILY, "US26", individ.id, "Family records do not contain children")
    return oneForOneFamilyIndividualRecords(individualDict,familyDict) and errors == 0
