
#US32 families with multiple births list
#returns false or the date of multiple births
def hasMultipleBirths(siblingDates):
    retValue = True
    datesDict = {}
    for d in siblingDates:
        if d in datesDict:
            datesDict[d] = datesDict.get(d) + 1
        else:#if we did not find this date, we first check if we have date within day of already found dates
            found = False
            for d2 in datesDict:
                delta = d2 - d
                if (abs(delta.days) < 2):
                    datesDict[d2] = datesDict.get(d2) + 1
                    found = True 
            if not found:
                datesDict[d] = 1
    for birthDate in datesDict.keys():
        if datesDict[birthDate] > 1:
            return birthDate.strftime('%d %b %Y')
    return False  