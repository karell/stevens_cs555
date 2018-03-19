import ErrorLogger

def validParentDecendantMarriages(familyDic, individualDic):
  #check each spouse and see if they're a decendant
    for i in sorted(familyDic.keys()):
        if len(familyDic[i].children) > 0:
            if isDecendant(familyDic[i].husbandId, familyDic[i].children, individualDic):
                #husband is a decendant
                ErrorLogger.__logAnomaly__(ErrorLogger._FAMILY,"US17", i, "Husband has marriage with decendant")
            if isDecendant(familyDic[i].wifeId, familyDic[i].children, individualDic):
                #wife is a decendant 
                ErrorLogger.__logAnomaly__(ErrorLogger._FAMILY,"US17", i,"Wife has marriage with decendant")

def validUncleAuntMarriages(familyDic, individualDic):
  # check every child of each family and make sure that for all of their siblings,
  # their spouse is not a sibling child or sibling child's child...etc
    for i in sorted(familyDic.keys()):
        if len(familyDic[i].children) > 1:
            for child in familyDic[i].children:
                # for each child, check sibling children recursively
                siblings = createSiblingList(child, familyDic[i].children)
                if isDecendant(child, siblings, individualDic):
                    # married neice or nephew (second, third, fourth and so on neices and nephews)
                    ErrorLogger.__logAnomaly__(ErrorLogger._FAMILY, "US20", i, child + " married to a neice or nephew")

def isDecendant(userId, decendantChildren, individualDic):

    if len(decendantChildren) > 0:
        for i in decendantChildren:
            if userId in individualDic[i].spouse:
                return True
            # check if the child has children and recursively check
            if len(individualDic[i].children) > 0:
                if isDecendant(userId, individualDic[i].children, individualDic):
                    return True
    return False

def createSiblingList(userId, children):
    siblings = list(children)
    siblings.remove(userId)
    return siblings