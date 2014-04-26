from datetime import datetime
import sys

def sort(file):
	startTime = datetime.now()
	print "Performing Insertion Sort: Start at %s" % startTime

	fileData = file.readlines()

	input = []
	for x in fileData:
		input.append(int(x))

	sortedData = insertionSort(input)	
	print sortedData

	endTime = datetime.now()
	print "Performed Insertion Sort: End at %s" % endTime

	print "Time elapsed " + str(endTime - startTime)

'''
The invariant for Insertion Sort is following
	For every undesorted element in the array it is assumed that the array 0 .. x where x is unsorted elements position, is already sorted.

This current implementation has O(n^2) complexity.
'''
def insertionSort(input):

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

if len(sys.argv) == 2:
	script, fileName = sys.argv
	print "File with unsorted data is %s" % fileName
else:
	print "Please provide location of input file"
	fileName = raw_input('> ')

try:
	file = open(fileName)
except Exception, e:
	print "Could not open file %s. Exiting" % fileName
	sys.exit(0)

sort(file)

