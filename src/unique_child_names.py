"""
unique_child_names module
checks whether children of a family have unique first names (US#25)
@author Keith Roseberry
"""
import ErrorLogger

# -----------------------------------------------------------------------------
# User Story #25: The first names of all children in a family must be unique.
# -----------------------------------------------------------------------------

def are_child_names_unique(the_family, all_individuals):
    """
    ---------------------------------------------------------------------------
    This function checks whether the first names of all children in the
    provided Family object are unique. User Story #25.

    Parameters
    ----------
    the_family:      The family object to test whether the child first names
                     are unique.
    all_individuals: A dictionary object that contains all of the individual
                     records in the GEDCOM file.

    Returns
    -------
    True:  When the child first names are unique.
    False: When at least one child first name is duplicated.
    ---------------------------------------------------------------------------
    """
    unique = True
    child_first_names = []
    for the_child_id in the_family.children:
        if the_child_id in all_individuals:
            the_child = all_individuals[the_child_id]
            first_name = the_child.firstAndMiddleName[0:the_child.firstAndMiddleName.find(' ')]
            if first_name in child_first_names:
                unique = False
                ErrorLogger.__logError__( \
                    ErrorLogger._FAMILY, "US25", the_family.id, \
                    "Child name " + first_name + " is not unique.")
            else:
                child_first_names.append(first_name)
        else:
            print("US25 error: Child " +
                  the_child_id +
                  " is not in the Individuals dictionary.")

    return unique
