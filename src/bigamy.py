'''
Created on Mar 24, 2018

@author: esther
'''
"""
Bigamy Module
Tests whether there is Bigamy.
"""
import datetime
import family
import individual
import ErrorLogger

def is_bigamy(individual, families, individuals):
    """
    ---------------------------------------------------------------------------
    is_bigamy
    ----------------
    This function checks whether a husband is married to multiple wives at the same time.

    Parameters
    ----------
    family:   The family object to test whether the husband of a family has multiple wives
    families: A Dictionary object that contains the Family objects as compiled
              from the GEDCOM file.
    individuals: A Dictionary object that contains the individual objects to use to look up the husband, and see if he has other wives

    Returns
    -------
    True:       When husband has multiple wives at the same time
    False:      When only married to one wife at a time or not married
    ---------------------------------------------------------------------------
    """
    result = False
    testPerson = individual
    #print ("Spouse:")
    #print(individual.spouse)
    
    if testPerson.spouse is None or len(testPerson.spouse) <= 1:
        return result
    
    spouses = testPerson.spouse
    
    if spouses is not None and spouses is not 'NA'  and len(spouses) > 1:
        marriageDates = []
        divorceDates = []
       
        for i in spouses:
            #print (i)
            spouseIndividual = individuals.get(i)
            #print (spouseIndividual.toString())
            #print (spouseIndividual.familyIdSpouse)
            family = families.get(spouseIndividual.familyIdSpouse)
            #print(family.id)
            spouseDictionary = {family.husbandId: family.wifeId, family.wifeId: family.husbandId}
            if family.marriageDate is not None:
                marriageDate = family.marriageDate
            divorceDate = family.divorcedDate
            
            if marriageDate is None:
                marriageDate = datetime.date.today()
            if divorceDate is None or divorceDate == 'NA':
                divorceDate = datetime.datetime.today()
                if individuals.get(individual.id).deathDate is not None:
                    #print ("DEATH: " + str(individuals.get(individual.id).deathDate))
                    divorceDate = individuals.get(individual.id).deathDate
               
            #print(marriageDate)
            #print("Div: " + str(divorceDate))
            marriageDates.append(marriageDate)
            divorceDates.append(divorceDate)
        for m in range(0, len(marriageDates)):
            for d in range(0, len(divorceDates)):
                if marriageDates[d] < marriageDates[m] < divorceDates[d]:
                    result = True
                    ErrorLogger.__logAnomaly__(ErrorLogger._INDIVIDUAL,"US11", individual.id, "Possible Bigamy")
        for d in range(0, len(divorceDates)):
            for m in range(0, len(marriageDates)):
                if marriageDates[m] < divorceDates[d] < divorceDates[m]:
                    result = True
                    ErrorLogger.__logAnomaly__(ErrorLogger._INDIVIDUAL,"US11", individual.id, "Possible Bigamy")
    return result
 

