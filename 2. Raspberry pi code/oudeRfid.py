import math
import serial
import struct

serial = serial.Serial("/dev/ttyAMA0" , baudrate=9600)
while True:
	serial.write("!RW")
	serial.write("\x01")
	serial.write("\x20")
	if serial.inWaiting > 0:
		card = serial.read()
		if result.encode('hex') !="0":
			card = serial.read(size=4)
			print card.encode('hex')
serial.flushInput()
serial.close()