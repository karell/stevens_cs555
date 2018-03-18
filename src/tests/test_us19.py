"""
test_us19 module
performs unit tests for user story #19
"""
import unittest
import sys

sys.path.append('../')

import individual
import family
import cousins_married

# -----------------------------------------------------------------------------
# User Story #19: First cousins should not marry. First cousins are identified
#                 by being children of the same generation with the same
#                 grandparents.
# -----------------------------------------------------------------------------

class TestUS19CousinsMarried(unittest.TestCase):
    """
    Class TestUS19CousinsMarried
    Contains methods that perform unit tests to determine if a marriage is of
    first cousins.
    """

    def test_cousins_married(self):
        """
        function test_CousinsMarried
        builds a set of records that mimic a marriage of cousins and tests
        the is_marriage_of_cousins function.
        """
        # Generation 1 - Grandparents
        grand_father = individual.Individual()
        grand_father.id = "GF"
        grand_father.firstAndMiddleName = "John James"
        grand_father.lastname = "Jamison"

        grand_mother = individual.Individual()
        grand_mother.id = "GM"
        grand_mother.firstAndMiddleName = "Jane Janet"
        grand_mother.lastname = "Jamison"

        # Generation 2 - Parents
        father_1 = individual.Individual()
        father_1.id = "F1"
        father_1.firstAndMiddleName = "James Jonas"
        father_1.lastname = "Jamison"

        mother_1 = individual.Individual()
        mother_1.id = "M1"
        mother_1.firstAndMiddleName = "Janet Judy"
        mother_1.lastname = "Jamison"

        father_2 = individual.Individual()
        father_2.id = "F2"
        father_2.firstAndMiddleName = "Jack Jeffrey"
        father_2.lastname = "Jamison"

        mother_2 = individual.Individual()
        mother_2.id = "M2"
        mother_2.firstAndLastName = "Jennifer Julia"
        mother_2.lastname = "Jamison"

        # Generation 3 - Cousins
        cousin_1 = individual.Individual()
        cousin_1.id = "C1"
        cousin_1.firstAndMiddleName = "Jacob Jarad"
        cousin_1.lastname = "Jamison"

        cousin_2 = individual.Individual()
        cousin_2.id = "C2"
        cousin_2.firstAndMiddleName = "Jessica Joyce"
        cousin_2.lastname = "Jamison"

        # Families - tie them all together
        gen_1_family = family.Family()
        gen_1_family.id = "G1F1"
        gen_1_family.husbandId = grand_father.id
        gen_1_family.wifeId = grand_mother.id
        gen_1_family.children.append(father_1.id)
        gen_1_family.children.append(father_2.id)

        gen_2_family_1 = family.Family()
        gen_2_family_1.id = "G2F1"
        gen_2_family_1.husbandId = father_1.id
        gen_2_family_1.wifeId = mother_1.id
        gen_2_family_1.children.append(cousin_1.id)

        gen_2_family_2 = family.Family()
        gen_2_family_2.id = "G2F2"
        gen_2_family_2.husbandId = father_2.id
        gen_2_family_2.wifeId = mother_2.id
        gen_2_family_2.children.append(cousin_2.id)

        gen_3_family = family.Family()
        gen_3_family.id = "G3F1"
        gen_3_family.husbandId = cousin_1.id
        gen_3_family.wifeId = cousin_2.id

        families_dict = {}
        families_dict[gen_1_family.id] = gen_1_family
        families_dict[gen_2_family_1.id] = gen_2_family_1
        families_dict[gen_2_family_2.id] = gen_2_family_2
        families_dict[gen_3_family.id] = gen_3_family

        self.assertTrue(cousins_married.is_marriage_of_cousins( \
            gen_3_family, families_dict))

if __name__ == '__main__':
    unittest.main()
