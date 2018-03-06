import unittest
import datetime
import sys

sys.path.append('../')

import individual
import family

# -----------------------------------------------------------------------------
# User Story #26: All family roles (spouse, child) specified in an individual record 
# should have corresponding entries in the corresponding family records. Likewise, 
# all individual roles (spouse, child) specified in family records should have corresponding 
# entries in the corresponding  individual's records.  I.e. the information in the 
# individual and family records should be consistent.
# -----------------------------------------------------------------------------

class Test_CorrespondingEntries(unittest.TestCase):

    def test_IndividualIdExists(self):
        self.assertFalse(False)

if __name__ == "__main__":
        if len(sys.argv) != 2:
                sys.exit("ERROR need GEDCOM file on command line")
        command_line = sys.argv[1]
        del sys.argv[1:]
        unittest.main()