import unittest
from insertionsort import insertionsort
from generateinput import seeddata
import os.path
import sys

class insertionsorttest(unittest.TestCase):

    def setUp(self):
        sd = seeddata()
        self.fileName = sd.genrateRandomDataTill(10)

    def testFileExists(self):
        self.assertTrue(os.path.isfile(self.fileName))
        print "Checked that file %s exists" % self.fileName

    def testInsertionSort(self):
    	sys.argv = ["", self.fileName]
    	inst = insertionsort.insertionsort()
    	sortedData = inst.setUpSort()

        file = open(self.fileName)
        inputData = file.readlines()

        input = []
        for x in inputData:
            input.append(int(x))

        input.sort()

        self.assertTrue(sortedData == input)

    def tearDown(self):
    	os.remove(self.fileName)
