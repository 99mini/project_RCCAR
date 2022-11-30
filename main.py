import serial
import cv2
import numpy as np

import time
base_path = '/dev/serial/by-id/'
by_id = 'usb-Arduino__www.arduino.cc__0043_758303334383510102E1-if00'
ser = serial.Serial(base_path+by_id, 9600)

print('start')

directions = ['G','B','L','R']
while True:
	for direction in directions:
		cmd = ("%c\n" %direction).encode('ascii')
		print("My cmd is %s" % cmd)
		ser.write(cmd)

		# For debugging, read cmd from arduino    
		# read_serial=ser.readline()
		# print(read_serial)

