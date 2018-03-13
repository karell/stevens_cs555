"""
Cousins Married Module
Tests whether a marriage is of first cousins (US19).
"""
import ErrorLogger

def is_same_family(family_1, family_2):
    """
    ---------------------------------------------------------------------------
    is_same_family
    --------------
    This function checks if the families supplied have the same identifiers.
   ----------------------------------------------------------------------------
    """
    return family_1 is not None and family_2 is not None and \
           family_1.id == family_2.id

def log_error(family_id, grand_family_id):
    """
    ---------------------------------------------------------------------------
    log_error
    ---------
    This function logs an error to the error log with the user story id and the
    ids of the families specified.
    ---------------------------------------------------------------------------
    """
    ErrorLogger.__logError__(ErrorLogger._FAMILY, "US19", family_id, \
        "Marriage is of cousins of family " + grand_family_id)

def is_marriage_of_cousins(family, families):
    """
    ---------------------------------------------------------------------------
    is_marriage_of_cousins
    ----------------------
    This function checks whether first cousins have married. This is determined
    by checking whether the husband and wife of a Family object can be traced
    back to the same grandparents.

    Parameters
    ----------
    family:   The family object to test whether the husband and wife are
              cousins.
    families: A Dictionary object that contains the Family objects as compiled
              from the GEDCOM file.

    Returns
    -------
    ValueError: When there are no entries in the families dictionary
    True:       When cousins have been deteremined to have married
    False:      When the marriage is not of cousins.
    ---------------------------------------------------------------------------
    """

    # If the supplied dictionary has no entries, raise a ValueError exception
    if not families:
        raise ValueError

    # Find the previous generation family of the husband (the family that has
    # the husband's parents).
    gen_1_up_husband = None
    for f_idx in families:
        for childId in families[f_idx].children:
            if family.husbandId == childId:
                gen_1_up_husband = families[f_idx]

    # Find the previous generation family of the wife (the family that has
    # the wife's parents).
    gen_1_up_wife = None
    for f_idx in families:
        for childId in families[f_idx].children:
            if family.wifeId == childId:
                gen_1_up_wife = families[f_idx]

    # If the husband's parent's family and the wife's parent's family have both
    # been found, then continue.
    if gen_1_up_husband is not None and gen_1_up_wife is not None:

        # Find the next generation up families of the father and mother of the
        # husband (the families that have the parents of the husband's father
        # and mother).
        gen_2_up_husband_father = None
        for f_idx in families:
            for childId in families[f_idx].children:
                if gen_1_up_husband.husbandId == childId:
                    gen_2_up_husband_father = families[f_idx]

        gen_2_up_husband_mother = None
        for f_idx in families:
            for childId in families[f_idx].children:
                if gen_1_up_husband.wifeId == childId:
                    gen_2_up_husband_mother = families[f_idx]

        # Find the next generation up families of the father and mother of the
        # wife (the families that have the parents of the wife's father and
        # mother).
        gen_2_up_wife_father = None
        for f_idx in families:
            for childId in families[f_idx].children:
                if gen_1_up_wife.husbandId == childId:
                    gen_2_up_wife_father = families[f_idx]

        gen_2_up_wife_mother = None
        for f_idx in families:
            for childId in families[f_idx].children:
                if gen_1_up_wife.wifeId == childId:
                    gen_2_up_wife_mother = families[f_idx]

        # Compare if any of the found families in the second generation up are
        # the same. If yes, then the marriage is of cousins.
        if is_same_family(gen_2_up_husband_father, gen_2_up_wife_father):
            log_error(family.id, gen_2_up_husband_father.id)
            return True
        if is_same_family(gen_2_up_husband_father, gen_2_up_wife_mother):
            log_error(family.id, gen_2_up_husband_father.id)
            return True
        if is_same_family(gen_2_up_husband_mother, gen_2_up_wife_father):
            log_error(family.id, gen_2_up_husband_mother.id)
            return True
        if is_same_family(gen_2_up_husband_mother, gen_2_up_wife_mother):
            log_error(family.id, gen_2_up_husband_mother.id)
            return True

    # If we get this far then the marriage is not of cousins.
    return False
