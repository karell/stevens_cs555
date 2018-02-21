'''
Created on Feb 20, 2018

@author: esthe
'''
##US12 - Pair Programming
##Mother less than 60 Father less than 80

from dateutil.relativedelta import relativedelta

def isValidFatherAge(childBirthDate, fatherBirthDate):
    ageDifference = relativedelta(childBirthDate, fatherBirthDate).years
    if ageDifference >= 80:
        return False
    else:
        return True

def isValidMotherAge(childBirthDate, motherBirthDate):
    ageDifference = relativedelta(childBirthDate, motherBirthDate).years
    if ageDifference >= 60:
        return False
    else:
        return True

