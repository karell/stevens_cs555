import unittest
import sys
sys.path.append('../')
sys.argv.append("../inputB.ged")

import individual

class Test_SingleAliveOver30(unittest.TestCase):

    def test_singleAliveOver30(self):
        ind = individual.Individual()
        ind.age = 31
        ind.alive = True
        self.assertTrue(ind.isSingleAliveOver30())
    
    def test_singleDeadOver30(self):
        ind = individual.Individual()
        ind.age = 7
        self.assertFalse(ind.isSingleAliveOver30())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("ERROR need GEDCOM file on command line")
    command_line = sys.argv[1]
    del sys.argv[1:]
    unittest.main()