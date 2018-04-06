import unittest
import sys
from datetime import datetime

sys.path.append('../')
sys.argv.append("../inputB.ged")

import sibling_records


class Test_familyHasMultipleBirths(unittest.TestCase):

    def test_NotMultipleBirths(self):
        birthdate1 = datetime.now()
        birthdate2 = datetime(2009, 10, 5, 18, 00)
        self.assertFalse(sibling_records.hasMultipleBirths([birthdate1,birthdate2]))
    
    def test_MultipleBirths(self):
        birthdate1 = datetime.now()
        birthdate2 = datetime.now()
        birthdate3 = datetime(2009, 10, 5, 18, 00)
        self.assertTrue(sibling_records.hasMultipleBirths([birthdate1,birthdate2,birthdate3]))

if __name__ == "__main__":
        if len(sys.argv) != 2:
                sys.exit("ERROR need GEDCOM file on command line")
        command_line = sys.argv[1]
        del sys.argv[1:]
        unittest.main()
        