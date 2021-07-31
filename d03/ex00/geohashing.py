#!/usr/bin/env python3

import sys
import antigravity

def geohashing(argv):
	if (len(argv) != 4):
		sys.exit("It requires 3 arguments !(latitude, longitude, date-dow)")
	try:
		lat = float(argv[1])
	except:
		sys.exit("The type of latitude argument is float !")
	try:
		longi = float(argv[2])
	except:
		sys.exit("The type of longitude argment is float !")
	try:
		date_dow = argv[3].encode('ascii')
	except:
		sys.exit("The type of date-dow is string !")

	antigravity.geohash(lat, longi, date_dow)

if __name__ == '__main__':
	geohashing(sys.argv)