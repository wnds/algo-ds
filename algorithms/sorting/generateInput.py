# Sample file to generate input for sorting

from datetime import datetime
from random import sample
import sys

def genrateRandomDataTill(limit):
	
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


print "This program will generate a input file to be used for sorting."
print "Press 1 for random numbers."

try:
	option = int(raw_input('> '))
except Exception, e:
	print "This option is invalid"
	sys.exit(0)

if option == 1:
	print "OK. Random data will be generated. Tell me how many you want? "
	limit = raw_input('> ')
	genrateRandomDataTill(int(limit))
else:
	print "This option is invalid"
