"""
unique_child_names module
checks whether children of a family have unique first names (US#25)
@author Keith Roseberry
"""
import ErrorLogger
import family
import individual

# -----------------------------------------------------------------------------
# User Story #25: The first names of all children in a family must be unique.
# -----------------------------------------------------------------------------

def are_child_names_unique(the_family, all_individuals):
    """
    function are_child_names_unique
    determines whether the first names of the children of the provided family
    have unique first names
    returns true: children first names are unique
    returns false: at least one child has the same first name as another child
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
