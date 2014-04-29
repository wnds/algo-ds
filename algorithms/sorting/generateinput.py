# Sample file to generate input for sorting

from datetime import datetime
from random import sample
import sys

class seeddata():

	def genrateRandomDataTill(self, limit):
		
		fileName = datetime.now().strftime("%d_%m_%y_%I%M%S") + ".txt"
		# Setting range of numbers to a high value by multiplying with some constant
		data =  sample(xrange(limit * 8), limit)
		file = open(fileName,"w")

		for idx, val in enumerate(data):
			if idx != 0:
				file.write("\n")
			file.write(str(val))
		file.close()

		print "Generated file with name [%s]" % fileName

		return fileName

if __name__ == '__main__':

	print "This program will generate a input file to be used for sorting."

	if len(sys.argv) == 2:
		script, limit = sys.argv
		print "Got argument as %d " % int(limit)
	else:
		print "Random data will be generated. Tell me how many you want ?"

		try:
			limit = int(raw_input('> '))
		except Exception, e:
			print "The number entered is invalid"
			sys.exit(0)

	i = seeddata()
	i.genrateRandomDataTill(int(limit))