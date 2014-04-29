import unittest
from InsertionSort import InsertionSort
from generateInput import SeedData
import os.path
import sys

class InsertionSortTest(unittest.TestCase):

    def setUp(self):
        sd = SeedData()
        self.fileName = sd.genrateRandomDataTill(10)

    def testFileExists(self):
        self.assertTrue(os.path.isfile(self.fileName))
        print "Checked that file %s exists" % self.fileName

    def testInsertionSortWith10Numbers(self):
    	sys.argv = ["", self.fileName]
    	inst = InsertionSort.InsertionSort()
    	inst.setUpSort()

    def tearDown(self):
    	os.remove(self.fileName)
