'''
Created on Apr 6, 2018

@author: esther
'''

import individual
import ErrorLogger

def listMarriedIndividuals(individuals):
    individualsDict = {}
    allIndividualsDict = individuals
     
    for i in allIndividualsDict:
        checkPerson = allIndividualsDict[i]
        if ((len(checkPerson.spouse) > 0) and checkPerson.alive is True) and checkPerson.deathDate is None:
            individualsDict.__setitem__(checkPerson.id, checkPerson)
            
        else:
            ErrorLogger.__logAnomaly__(ErrorLogger._INDIVIDUAL,"US30", checkPerson.id, "Living, But Not Married")
    return individualsDict

def listDeceasedIndividuals(individuals):
    individualsDict = {}
    allIndividualsDict = individuals
   
    for i in allIndividualsDict:
        checkPerson = allIndividualsDict[i]
        if (checkPerson.alive is False) or checkPerson.deathDate is not None:
            individualsDict.__setitem__(checkPerson.id, checkPerson)
            
        else:
            ErrorLogger.__logAnomaly__(ErrorLogger._INDIVIDUAL,"US29", checkPerson.id, "Person is not Deceased")
    return individualsDict