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

def find_family_of_child(child_id, families):
    """
    ---------------------------------------------------------------------------
    find_family_of_child
    --------------------
    This function finds the family in which the child identifier is in the
    children array.
    ---------------------------------------------------------------------------
    """
    family_object = None
    for f_idx in families:
        for c_id in families[f_idx].children:
            if child_id == c_id:
                family_object = families[f_idx]
    return family_object

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
    gen_1_up_husband = find_family_of_child(family.husbandId, families)

    # Find the previous generation family of the wife (the family that has
    # the wife's parents).
    gen_1_up_wife = find_family_of_child(family.wifeId, families)

    # If the husband's parent's family and the wife's parent's family have both
    # been found, then continue.
    if gen_1_up_husband is not None and gen_1_up_wife is not None:

        # Find the next generation up families of the father and mother of the
        # husband (the families that have the parents of the husband's father
        # and mother).
        gen_2_up_husband_father = find_family_of_child(gen_1_up_husband.husbandId, families)
        gen_2_up_husband_mother = find_family_of_child(gen_1_up_husband.wifeId, families)

        # Find the next generation up families of the father and mother of the
        # wife (the families that have the parents of the wife's father and
        # mother).
        gen_2_up_wife_father = find_family_of_child(gen_1_up_wife.husbandId, families)
        gen_2_up_wife_mother = find_family_of_child(gen_1_up_wife.wifeId, families)

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
