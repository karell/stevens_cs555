import unittest
import sys
sys.path.append('../')
import individual
import family
import datetime
import gedcom_parser

class testSiblingsSpace(unittest.TestCase):
    def test_alldifferentDates(self):
        date1 = datetime.date(1990,1,1)
        date2 = datetime.date(1991,1,1)
        date3 = datetime.date(1992,1,1)
        siblingsDates = (date1,date2,date3)
        self.assertTrue(gedcom_parser.verifySiblingsSpace(siblingsDates))

    def test_someDifferentDatesSameYear(self):
        date1 = datetime.date(1990,1,1)
        date2 = datetime.date(1990,11,1)
        date3 = datetime.date(1991,12,1)
        siblingsDates = (date1,date2,date3)
        self.assertTrue(gedcom_parser.verifySiblingsSpace(siblingsDates))

    def test_allSameDates(self):
        date1 = datetime.date(1990,1,1)
        date2 = datetime.date(1990,1,1)
        date3 = datetime.date(1990,1,1)
        siblingsDates = (date1,date2,date3)
        self.assertFalse(gedcom_parser.verifySiblingsSpace(siblingsDates))
    
    def test_someWithDayDifference(self):
        date1 = datetime.date(1990,1,2)
        date2 = datetime.date(1990,1,1)
        date3 = datetime.date(1990,1,2)
        siblingsDates = (date1,date2,date3)
        self.assertFalse(gedcom_parser.verifySiblingsSpace(siblingsDates))
    
    def test_someWithMonthsDifference(self):
        date1 = datetime.date(1990,1,1)
        date2 = datetime.date(1990,6,1)
        date3 = datetime.date(1992,1,2)
        siblingsDates = (date1,date2,date3)
        self.assertFalse(gedcom_parser.verifySiblingsSpace(siblingsDates))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("ERROR need GEDCOM file on command line")
    command_line = sys.argv[1]
    del sys.argv[1:]
    unittest.main()
        