import unittest
import sys
sys.path.append('../')
import individual
import family
import datetime

class testSortSiblings(unittest.TestCase):
    
    def notSorted(self):
        child1 = individual.Individual()
        child1.birthDate = datetime.date(1990,1,1)
        child2 = individual.Individual()
        child2.birthDate = datetime.date(1993,1,1)
        child3 = individual.Individual()
        child3.birthDate = datetime.date(1980,1,1)
        myFamily = family.Family()

        myFamily.children.append(child1)
        myFamily.children.append(child2)
        myFamily.children.append(child3)
        gedcom_parser(sortChildren(myFamily.children))
        self.assertTrue((all(myFamily.children[i].birthDate <= myFamily.children[i+1].birthDate for i in range(len(myFamily.children)-1))))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("ERROR need GEDCOM file on command line")
    command_line = sys.argv[1]
    del sys.argv[1:]
    unittest.main()