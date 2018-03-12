"""
Siblings Married Module
Tests whether a marriage is of siblings.
"""
import ErrorLogger

def is_marriage_of_siblings(family, families):
    """
    ---------------------------------------------------------------------------
    is_marriage_of_siblings
    ----------------
    This function checks whether siblings have married. A family's husband and
    wife both cannot be children of the same family.

    Parameters
    ----------
    family:   The family object to test whether the husband and wife are
              siblings of another family object.
    families: A Dictionary object that contains the Family objects as compiled
              from the GEDCOM file.

    Returns
    -------
    ValueError: When there are no entries in the families dictionary
    True:       When siblings have been deteremined to have married
    False:      When the marriage is not of siblings.
    ---------------------------------------------------------------------------
    """

    # If the supplied dictionary has no entries, raise a ValueError exception
    if not families:
        raise ValueError

    # Walk through the collection of families and determine if the husband
    # and wife of the provided family object are siblings.
    for f_idx in families:
        if not family.id == families[f_idx].id:
            husband_found = False
            wife_found = False
            for sibling in families[f_idx].children:
                if sibling == family.husbandId:
                    husband_found = True
                if sibling == family.wifeId:
                    wife_found = True
            if husband_found and wife_found:
                ErrorLogger.__logError__(ErrorLogger._FAMILY, "US18", family.id, \
                    "Marriage is of siblings of family " + families[f_idx].id)
                return True

    # If we get this far then the marriage is not of siblings.True
    return False
