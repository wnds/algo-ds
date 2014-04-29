from datetime import datetime
import sys
import abc

class basesort:

	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def sort(self, input):
		pass

	def setUpSort(self):

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

		startTime = datetime.now()
		print "Performing Sort: Start at %s" % startTime

		fileData = file.readlines()

		input = []
		for x in fileData:
			input.append(int(x))

		sortedData = self.sort(input)	
		print sortedData

		endTime = datetime.now()
		print "Performed Sort: End at %s" % endTime

		print "Time elapsed " + str(endTime - startTime)
		return sortedData