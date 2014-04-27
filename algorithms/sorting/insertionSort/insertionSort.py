# Insertion Sort implementation
# Execute as python -m insertionSort.insertionSort <input file> from one directory up

from datetime import datetime
import sys
from baseSort import baseSort

class insertionSort(baseSort):
	
	'''
	The invariant for Insertion Sort is following
		For every undesorted element in the array it is assumed that the array 0 .. x where x is unsorted elements position, is already sorted.

	This current implementation has O(n^2) complexity.
	'''
	def sort(self, input):

		# Start from the second element in list
		for startIndex in range(1, len(input)):
			print "-- Begin next iteration --"
			numberToSort = input[startIndex]
			print "Need to place %d at right place from the front " % numberToSort
			for sortedIndex in range(startIndex - 1, -1, -1):
				print "Comparing %d with %d" % (input[sortedIndex], numberToSort)
				if input[sortedIndex] >  numberToSort:
					temp = input[sortedIndex]
					input[sortedIndex] = numberToSort
					input[sortedIndex + 1] = temp
					print "Swapped %d and %d" % (temp, numberToSort)
				else:
					break;
		return input

'''
MAIN FUNCTION
'''

c = insertionSort()
c.setUpSort()