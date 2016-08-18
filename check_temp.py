#!/bin/python

import serial
import sys

ser = serial.Serial("/dev/ttyACM2", 9600)

currentTemp = ser.readline()

currentTemp = int(currentTemp)

print currentTemp

if currentTemp >= 15 and currentTemp < 35:
	print 'OK - Room Tempature is: ', currentTemp
	sys.exit(0)
elif currentTemp >= 35 and currentTemp < 38:
	print 'WARNING - Room Tempature is: ', currentTemp
	sys.exit(1)
elif currentTemp >= 38:
	print 'CRITICAL - Room Tempature is: ', currentTemp
	sys.exit(2)
else:
	print 'UNKNOWN'
	sys.exit(3)
