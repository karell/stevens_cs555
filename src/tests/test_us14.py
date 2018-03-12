import unittest
import sys
sys.path.append('../')
import individual
import family
import datetime
import gedcom_parser

class testFiveSiblings(unittest.TestCase):
    def test_allFivearedifferentDates(self):
        date1 = datetime.date(1990,1,1)
        date2 = datetime.date(1991,1,1)
        date3 = datetime.date(1992,1,1)
        date4 = datetime.date(1993,1,1)
        date5 = datetime.date(1994,1,1)
        date6 = datetime.date(1995,1,1)
        siblingsDates = (date1,date2,date3,date4,date5,date6)
        self.assertTrue(gedcom_parser.verifySiblingsDates(siblingsDates))

    def test_someDifferentDates(self):
        date1 = datetime.date(1990,1,1)
        date2 = datetime.date(1990,1,1)
        date3 = datetime.date(1990,1,1)
        date4 = datetime.date(1993,1,1)
        date5 = datetime.date(1994,1,1)
        date6 = datetime.date(1995,1,1)
        siblingsDates = (date1,date2,date3,date4,date5,date6)
        self.assertTrue(gedcom_parser.verifySiblingsDates(siblingsDates))

    def test_allSameDates(self):
        date1 = datetime.date(1990,1,1)
        date2 = datetime.date(1990,1,1)
        date3 = datetime.date(1990,1,1)
        date4 = datetime.date(1990,1,1)
        date5 = datetime.date(1990,1,1)
        date6 = datetime.date(1990,1,1)
        siblingsDates = (date1,date2,date3,date4,date5,date6)
        self.assertFalse(gedcom_parser.verifySiblingsDates(siblingsDates))
    
    def test_someWithDayDifference(self):
        date1 = datetime.date(1990,1,2)
        date2 = datetime.date(1990,1,1)
        date3 = datetime.date(1990,1,2)
        date4 = datetime.date(1990,1,1)
        date5 = datetime.date(1990,1,1)
        date6 = datetime.date(1990,1,1)
        siblingsDates = (date1,date2,date3,date4,date5,date6)
        self.assertFalse(gedcom_parser.verifySiblingsDates(siblingsDates))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("ERROR need GEDCOM file on command line")
    command_line = sys.argv[1]
    del sys.argv[1:]
    unittest.main()
        