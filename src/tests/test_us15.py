"""
test_us55 module
performs unit tests for user story #15
@author Keith Roseberry
"""
import unittest
import sys

sys.path.append('../')

import individual
import family
import sibling_count

# -----------------------------------------------------------------------------
# User Story #15: Less than 15 siblings in a family.
# -----------------------------------------------------------------------------

def _create_individual(ind_id, f_name, l_name):
    child = individual.Individual()
    child.id = ind_id
    child.firstAndLastName = f_name
    child.lastname = l_name
    return child

def _create_family():
    # Generation 1 - Parents
    father = _create_individual("F1", "James Jonas", "Jamison")
    mother = _create_individual("M1", "Janet Judy", "Jamison")

    # Generation 2 - Children
    child_01 = _create_individual("C01", "Jacob", "Jamison")
    child_02 = _create_individual("C02", "Jarod", "Jamison")
    child_03 = _create_individual("C03", "Jessica", "Jamison")
    child_04 = _create_individual("C04", "Joyce", "Jamison")
    child_05 = _create_individual("C05", "Jeremy", "Jamison")
    child_06 = _create_individual("C06", "Jackson", "Jamison")
    child_07 = _create_individual("C07", "Jaden", "Jamison")
    child_08 = _create_individual("C08", "Jaeger", "Jamison")
    child_09 = _create_individual("C09", "Jan", "Jamison")
    child_10 = _create_individual("C10", "Jansen", "Jamison")
    child_11 = _create_individual("C11", "Jarrett", "Jamison")
    child_12 = _create_individual("C12", "Jason", "Jamison")
    child_13 = _create_individual("C13", "Jax", "Jamison")
    child_14 = _create_individual("C14", "Jean", "Jamison")

    # Family - tie them all together
    family_1 = family.Family()
    family_1.id = "G1F1"
    family_1.husbandId = father.id
    family_1.wifeId = mother.id
    family_1.children.append(child_01.id)
    family_1.children.append(child_02.id)
    family_1.children.append(child_03.id)
    family_1.children.append(child_04.id)
    family_1.children.append(child_05.id)
    family_1.children.append(child_06.id)
    family_1.children.append(child_07.id)
    family_1.children.append(child_08.id)
    family_1.children.append(child_09.id)
    family_1.children.append(child_10.id)
    family_1.children.append(child_11.id)
    family_1.children.append(child_12.id)
    family_1.children.append(child_13.id)
    family_1.children.append(child_14.id)

    return family_1

class TestUS15LessThan15Siblings(unittest.TestCase):
    """
    Class TestUS15NoMoreThan15Siblings
    Contains methods that perform unit tests to determine if a familiy contains
    more than 14 siblings.
    """

    def test_too_many_siblings(self):
        """
        function test_too_many_siblings
        builds a set of records that construct a family with 15 siblings.
        """
        a_family = _create_family()
        child_15 = _create_individual("C15", "Jeffrey", "Jamison")
        a_family.children.append(child_15.id)

        self.assertFalse(sibling_count.less_than_15_siblings(a_family))

    def test_not_too_many_siblings(self):
        """
        function test_not_too_many_siblings
        builds a set of records that construct a family with 14 siblings.
        """
        a_family = _create_family()

        self.assertTrue(sibling_count.less_than_15_siblings(a_family))

if __name__ == '__main__':
    unittest.main()
