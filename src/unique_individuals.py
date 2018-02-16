import individual

# ---------------------------------------------------------------------------
# Unique Individuals
# ------------------
# This file contains functionality to ensure that there is no more than one
# individual with the same name and birth date in the collection (gedcom
# file).
#
# Parameters
# ----------
# individuals: A Dictionary object that contains the individuals as compiled
#              from the GEDCOM file.
#
# Returns
# -------
# ValueError: When there are no entries in the individuals dictionary
# True:       When all individuals are unique
# False:      When at least one individual is duplicated in the individuals
#             dictionary (note that they ID values by necessity must be
#             unique)
# ---------------------------------------------------------------------------

def AreIndividualsUnique(individuals):
    result = False # Default to non-uniqueness

    # If the supplied dictionary has no entries, raise a ValueError exception
    if len(individuals) == 0:
        raise ValueError

    # If the supplied dictionary has exactly one entry, then this one entry
    # is considered unique.
    if len(individuals) == 1:
        result = True
    else:

        # Walk through the dictionary and look for a duplicate. If one is
        # found, then we can abort the search and return a False result.
        duplicateFound = False
        for i1 in individuals:
            fName1 = individuals[i1].firstAndMiddleName
            lName1 = individuals[i1].lastname
            bDate1 = individuals[i1].birthDate

            print("\n")
            print("Checking " + i1 + ": " + fName1 + " " + lName1 + ", born on " + bDate1.strftime("%d-%b-%Y") + ":")

            for i2 in individuals:

                # Skip if the individual ID is the same (checking the same dict
                # entry).
                if not i1 == i2:

                    fName2 = individuals[i2].firstAndMiddleName
                    lName2 = individuals[i2].lastname
                    bDate2 = individuals[i2].birthDate

                    print("--- with " + i2 + ": " + fName2 + " " + lName2 + ", born on " + bDate2.strftime("%d-%b-%Y") + ":")
                    if fName1 == fName2 and lName1 == lName2 and bDate1 == bDate2:
                        duplicateFound = True
                        break

            if duplicateFound:
                break

        # Only set the result to True if no duplicates were found.
        if not duplicateFound:
            result = True
    
    return result
