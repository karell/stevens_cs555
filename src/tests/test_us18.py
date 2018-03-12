"""
test_us18 module
performs unit tests for user story #18
"""
import unittest
import sys

sys.path.append('../')

import individual
import family
import siblings_married

# -----------------------------------------------------------------------------
# User Story #18: The husband and wife should not both be in the children
#                 array of any other family.
# -----------------------------------------------------------------------------

class TestUS18SiblingsMarried(unittest.TestCase):
    """
    Class Test_US18_Siblings_Married
    Contains methods that perform unit tests to determine if a marriage is of
    siblgins.
    """

    def test_siblings_married(self):
        """
        function test_SiblingsMarried
        builds a set of records that mimic a marriage of siblings and tests
        the is_marriage_of_siblings function.
        """
        husband = individual.Individual()
        husband.id = "H1"
        husband.firstAndMiddleName = "John James"
        husband.lastname = "Jamison"

        wife = individual.Individual()
        wife.id = "W1"
        wife.firstAndMiddleName = "Jane Janet"
        wife.lastname = "Jamison"

        family_with_children = family.Family()
        family_with_children.id = "F1"
        family_with_children.children.append(husband)
        family_with_children.children.append(wife)

        family_siblings_married = family.Family()
        family_siblings_married.id = "F2"
        family_siblings_married.husbandId = husband.id
        family_siblings_married.wifeId = wife.id

        families_dict = {}
        families_dict[family_with_children.id] = family_with_children

        self.assertTrue(siblings_married.is_marriage_of_siblings( \
            family_siblings_married, families_dict))

if __name__ == '__main__':
    unittest.main()
