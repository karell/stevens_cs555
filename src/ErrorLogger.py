'''
Created on Feb 23, 2018

@author: esthe
'''
import logging
import logging.config

from logging import FileHandler
logger = logging.getLogger('gedcomLogger')
fileHandler = logging.FileHandler('gedcomError.log', 'w')



def __initLogger__():
#        logger.config.dictConfig(GEDCOM_LOGGER)
        logger.addHandler(fileHandler)
        logger.setLevel("INFO")
        


def __logAnomaly__(userStory, id, messsage):
        msg = userStory + ": "+ str(id) + ": "+ messsage
        logger.info(msg)
                
def __logError__(userStory, id, messsage):
        msg = userStory + ": "+ str(id) + ": "+ messsage
        logger.error(msg)

                