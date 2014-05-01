import unittest
from mergesort import mergesort
from generateinput import seeddata
import os.path
import sys

class mergesorttest(unittest.TestCase):

    def testMergeSortWithEvenCount(self):

        sd = seeddata()
        self.fileName = sd.genrateRandomDataTill(10)
        self.assertTrue(os.path.isfile(self.fileName))
        print "Checked that file %s exists" % self.fileName
    	sys.argv = ["", self.fileName]
    	inst = mergesort.mergesort()
    	sortedData = inst.setUpSort()

        file = open(self.fileName)
        inputData = file.readlines()

        input = []
        for x in inputData:
            input.append(int(x))

        input.sort()

        self.assertTrue(sortedData == input)

    def testMergeSortWithOddCount(self):

        sd = seeddata()
        self.fileName = sd.genrateRandomDataTill(9)
        self.assertTrue(os.path.isfile(self.fileName))
        print "Checked that file %s exists" % self.fileName
        sys.argv = ["", self.fileName]
        inst = mergesort.mergesort()
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
