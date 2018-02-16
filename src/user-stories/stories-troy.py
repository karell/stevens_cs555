##US22 All individual IDs should be unique and all family IDs should be unique
def isUniqueRecordId(recordId,parentDictionary):
    if recordId in parentDictionary:
        return False
    else:
      return True