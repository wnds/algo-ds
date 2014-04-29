import unittest
from insertionSort import insertionSort
from generateInput import SeedData
import os.path
import sys

class insertionSortTest(unittest.TestCase):

    def setUp(self):
        sd = SeedData()
        self.fileName = sd.genrateRandomDataTill(10)

    def testFileExists(self):
        self.assertTrue(os.path.isfile(self.fileName))
        print "Checked that file %s exists" % self.fileName

    def testInsertionSortWith10Numbers(self):
    	sys.argv = ["", self.fileName]
    	inst = insertionSort.insertionSort()
    	inst.setUpSort()

    def tearDown(self):
    	os.remove(self.fileName)
