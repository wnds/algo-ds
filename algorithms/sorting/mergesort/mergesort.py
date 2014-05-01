# Insertion Sort implementation

from datetime import datetime
import sys
from basesort import basesort

class mergesort(basesort):
	
	'''
	Merge sort is based on divide and conquer paradigm. We keep on subdividing array until there is only 
	one element in the subarray after which array is considerd as sorted. Most of the actual works gets
	done in the merge method which is used to join subarray to create big array.
	'''

	def sort(self, input):

		
		numberOfElements = len(input)
		print input
		#print numberOfElements

		# If only one element in the array then it is considerd as sorted
		if numberOfElements == 1:
			return input;

		#print "for left 0 %d" % (numberOfElements/2)
		leftArray = self.sort(input[0:numberOfElements/2])
		#print leftArray
		#print "for right %d %d" % ((numberOfElements/2),numberOfElements)
		rightArray = self.sort(input[(numberOfElements/2):numberOfElements])
		#print rightArray

		"""
		Both the left array and right array are considerd sorted at this point
		"""
		sortedData = []
		leftIndex = 0
		rightIndex = 0	

		while (leftIndex != len(leftArray) and rightIndex != len(rightArray)):
			print "%d %d " % (leftIndex, rightIndex)
			if leftArray[leftIndex] < rightArray[rightIndex]:
				sortedData.append(leftArray[leftIndex])
				leftIndex += 1
			elif leftArray[leftIndex] > rightArray[rightIndex]:
				sortedData.append(rightArray[rightIndex])
				rightIndex += 1

		if leftIndex != len(leftArray):
			sortedData += leftArray[leftIndex:len(leftArray)]
		elif rightIndex != len(rightArray): 
			sortedData += rightArray[rightIndex:len(rightArray)]

		return sortedData

'''
MAIN FUNCTION
'''
if __name__ == '__main__':
	c = mergesort()
	c.setUpSort()