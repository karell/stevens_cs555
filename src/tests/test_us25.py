"""
test_us25 module
performs unit tests for user story #25
@author Keith Roseberry
"""
import unittest
import sys

sys.path.append('../')

import individual
import family
import unique_child_names

# -----------------------------------------------------------------------------
# User Story #25: The first names of all children in a family must be unique.
# -----------------------------------------------------------------------------

class TestUS25FirstNamesUnique(unittest.TestCase):
    """
    Class TestUS25FirstNamesUnique
    Contains methods that perform unit tests to determine if the first names
    of all children in a family are unique.
    """

    def test_first_names_unique(self):
        """
        function test_first_names_unique
        builds a set of records that construct a family where all children
        have unique first names (positive test).
        """
        # Generation 1 - Parents
        father_1 = individual.Individual()
        father_1.id = "F1"
        father_1.firstAndMiddleName = "James Jonas"
        father_1.lastname = "Jamison"

        mother_1 = individual.Individual()
        mother_1.id = "M1"
        mother_1.firstAndMiddleName = "Janet Judy"
        mother_1.lastname = "Jamison"

        # Generation 2 - Children
        child_1 = individual.Individual()
        child_1.id = "C1"
        child_1.firstAndMiddleName = "Jacob Jarad"
        child_1.lastname = "Jamison"

        child_2 = individual.Individual()
        child_2.id = "C2"
        child_2.firstAndMiddleName = "Jessica Joyce"
        child_2.lastname = "Jamison"

        child_3 = individual.Individual()
        child_3.id = "C3"
        child_3.firstAndMiddleName = "Jeremy Jackson"
        child_3.lastname = "Jamison"

        # Family - tie them all together
        family_1 = family.Family()
        family_1.id = "G1F1"
        family_1.husbandId = father_1.id
        family_1.wifeId = mother_1.id
        family_1.children.append(child_1.id)
        family_1.children.append(child_2.id)
        family_1.children.append(child_3.id)

        individuals_dict = {}
        individuals_dict[child_1.id] = child_1
        individuals_dict[child_2.id] = child_2
        individuals_dict[child_3.id] = child_3

        self.assertTrue(unique_child_names.are_child_names_unique( \
            family_1, individuals_dict))

    def test_first_names_not_unique(self):
        """
        function test_first_names_unique
        builds a set of records that construct a family where all children
        have unique first names (positive test).
        """
        # Generation 1 - Parents
        father_1 = individual.Individual()
        father_1.id = "F1"
        father_1.firstAndMiddleName = "James Jonas"
        father_1.lastname = "Jamison"

        mother_1 = individual.Individual()
        mother_1.id = "M1"
        mother_1.firstAndMiddleName = "Janet Judy"
        mother_1.lastname = "Jamison"

        # Generation 2 - Children
        child_1 = individual.Individual()
        child_1.id = "C1"
        child_1.firstAndMiddleName = "Jacob Jarad"
        child_1.lastname = "Jamison"

        child_2 = individual.Individual()
        child_2.id = "C2"
        child_2.firstAndMiddleName = "Jessica Joyce"
        child_2.lastname = "Jamison"

        child_3 = individual.Individual()
        child_3.id = "C3"
        child_3.firstAndMiddleName = "Jeremy Jackson"
        child_3.lastname = "Jamison"

        child_4 = individual.Individual()
        child_4.id = "C4"
        child_4.firstAndMiddleName = "Jeremy John"
        child_4.lastname = "Jamison"

        # Family - tie them all together
        family_1 = family.Family()
        family_1.id = "G1F1"
        family_1.husbandId = father_1.id
        family_1.wifeId = mother_1.id
        family_1.children.append(child_1.id)
        family_1.children.append(child_3.id)
        family_1.children.append(child_2.id)
        family_1.children.append(child_4.id)

        individuals_dict = {}
        individuals_dict[child_1.id] = child_1
        individuals_dict[child_2.id] = child_2
        individuals_dict[child_3.id] = child_3

        self.assertTrue(unique_child_names.are_child_names_unique( \
            family_1, individuals_dict))

if __name__ == '__main__':
    unittest.main()
