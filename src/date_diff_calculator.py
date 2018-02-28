'''
Created on Feb 25, 2018

@author: esthe
'''
import datetime
from dateutil import relativedelta
#calculates the delta between two dates in requested units days or years
def calculateDateDifference(calcStartDate, calcEndDate, requestedDateUnit):
    startDate = calcStartDate
    endDate = calcEndDate
    if startDate is None:
        startDate = datetime.datetime.now()
    if endDate is None:
        endDate = datetime.datetime.now()
    dateDelta = relativedelta.relativedelta(endDate, startDate)
 
    if requestedDateUnit is "years":
        return dateDelta.years
    
    elif requestedDateUnit is "days":
        return dateDelta.days
    else:
        return dateDelta
##is Second Number Bigger takes two integers and returns true if the second number is bigger than the first
def isSecondNumberBigger(firstNumber, secondNumber):
    return (secondNumber > firstNumber)