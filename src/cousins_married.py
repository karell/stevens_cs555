"""
Cousins Married Module
Tests whether a marriage is of first cousins (US19).
"""
import ErrorLogger

def is_marriage_of_cousins(family, families):
    """
    ---------------------------------------------------------------------------
    is_marriage_of_cousins
    ----------------
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
        if gen_2_up_husband_father is not None and gen_2_up_wife_father is not None \
            and gen_2_up_husband_father.id == gen_2_up_wife_father.id:
            ErrorLogger.__logError__(ErrorLogger._FAMILY, "US19", family.id, \
                "Marriage is of cousins of family " + gen_2_up_husband_father.id)
            return True
        if gen_2_up_husband_father is not None and gen_2_up_wife_mother is not None \
            and gen_2_up_husband_father.id == gen_2_up_wife_father.id:
            ErrorLogger.__logError__(ErrorLogger._FAMILY, "US19", family.id, \
                "Marriage is of cousins of family " + gen_2_up_husband_father.id)
            return True
        if gen_2_up_husband_mother is not None and gen_2_up_wife_father is not None \
            and gen_2_up_husband_mother.id == gen_2_up_wife_father.id:
            ErrorLogger.__logError__(ErrorLogger._FAMILY, "US19", family.id, \
                "Marriage is of cousins of family " + gen_2_up_husband_mother.id)
            return True
        if gen_2_up_husband_mother is not None and gen_2_up_wife_mother is not None \
            and gen_2_up_husband_mother.id == gen_2_up_wife_mother.id:
            ErrorLogger.__logError__(ErrorLogger._FAMILY, "US19", family.id, \
                "Marriage is of cousins of family " + gen_2_up_husband_mother.id)
            return True

    # If we get this far then the marriage is not of cousins.
    return False
