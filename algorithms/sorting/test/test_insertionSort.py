import unittest
from insertionSort import insertionSort
from generateInput import SeedData
import os.path

class insertionSortTest(unittest.TestCase):

    def setUp(self):
        sd = SeedData()
        self.fileName = sd.genrateRandomDataTill(23)

    def testFileExists(self):
        self.assertTrue(os.path.isfile(self.fileName));
        print "Checked that file %s exists" % self.fileName