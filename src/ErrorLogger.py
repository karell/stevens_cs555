'''
Created on Feb 23, 2018

@author: esthe
'''
import logging
import logging.config

from logging import FileHandler
logger = logging.getLogger('gedcomLogger')
fileHandler = logging.FileHandler('gedcomError.log', 'w')

_logMessages = []
_ANOMALY     = "ANOMALY"
_ERROR       = "ERROR"

def __initLogger__():
#        logger.config.dictConfig(GEDCOM_LOGGER)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        
def __logAnomaly__(userStory, id, messsage):
        msg = userStory + ": "+ str(id) + ": "+ messsage
        logger.info(_ANOMALY + ": " + msg)
        _logMessages.append(_ANOMALY + ": " + msg)
                
def __logError__(userStory, id, messsage):
        msg = userStory + ": "+ str(id) + ": "+ messsage
        logger.error(_ERROR + ": " + msg)
        _logMessages.append(_ERROR + ": " + msg)

def __printLogMessages__():
        for message in _logMessages:
                print(message)
